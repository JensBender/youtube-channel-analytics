# Imports
from airflow.decorators import dag, task
from datetime import datetime, timedelta
import os
import pandas as pd
from googleapiclient.discovery import build
import mysql.connector
from sqlalchemy import create_engine
import re

# Get YouTube API key from docker environment
youtube_api_key = os.environ.get("YOUTUBE_API_KEY")

# Get AWS RDS MySQL server endpoint, username and password from docker environment
aws_mysql_endpoint = os.environ.get("AWS_MYSQL_ENDPOINT")
aws_mysql_user = os.environ.get("AWS_MYSQL_USER") 
aws_mysql_password = os.environ.get("AWS_MYSQL_PASSWORD")

# Define DAG arguments
default_args = {
    "owner": "Jens",
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}

# Define the DAG
@dag(
    dag_id="etl_pipeline",
    description="Extract data from YouTube API, transform, and load into MySQL database",
    start_date=datetime(2024, 7, 11),
    schedule_interval="0 0 * * *",
    catchup=False,
    tags=["Jens", "data engineering"],
    default_args=default_args
)
def etl_pipeline():
    # Extract data about YouTube channels, videos and comments from YouTube API
    @task
    def extract():
        # Build the YouTube service object
        youtube = build("youtube", "v3", developerKey=youtube_api_key)

        # Select channels
        channel_names = ["AlexTheAnalyst", "LukeBarousse", "Thuvu5"]

        # Initialize an empty list to store dictionaries for each channel
        channels_ls = []

        # Initialize an empty list to store uploads playlist IDs of all channels
        uploads_playlist_ids = []

        # Loop through each channel
        for channel_name in channel_names:
            # Get channel data using the YouTube Channels API
            # Note: Uses 1 out of 10.000 units from the daily usage limit 
            channel_data = youtube.channels().list(part="statistics,snippet,contentDetails", forHandle=channel_name).execute()  

            # Extract channel data in dictionary format
            channel_dict = {
                "channel_id": channel_data["items"][0]["id"],
                "channel_name": channel_data["items"][0]["snippet"]["title"],
                "views": int(channel_data["items"][0]["statistics"]["viewCount"]),
                "videos": int(channel_data["items"][0]["statistics"]["videoCount"]),
                "subscribers": int(channel_data["items"][0]["statistics"]["subscriberCount"])
            }
            
            try:
                # Try to get channel thumbnail in maximum resolution
                channel_dict["thumbnail_url"] = channel_data["items"][0]["snippet"]["thumbnails"]["maxres"]["url"]
            except KeyError:
                try:
                    # If maxres is not available, get high resolution
                    channel_dict["thumbnail_url"] = channel_data["items"][0]["snippet"]["thumbnails"]["high"]["url"]
                except KeyError:
                    # If high resolution is not available, get default resolution
                    channel_dict["thumbnail_url"] = channel_data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
            
            # Append channel data in dictionary format to the list
            channels_ls.append(channel_dict)
            
            # Append uploads playlist ID to the list 
            uploads_playlist_ids.append(channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"])

        # Convert list of dictionaries to pandas DataFrame
        channel_df = pd.DataFrame(channels_ls) 
        
        # Save pandas DataFrame as CSV file
        channel_df.to_csv("/opt/airflow/data/channel_df_extracted.csv")

        # Extract video data
        # Initialize an empty list to store dictionaries for each video
        videos_ls = []

        # Loop through each channel's uploads playlist
        for uploads_playlist_id in uploads_playlist_ids:
            # Initialize next_page_token to None
            next_page_token = None

            # Loop through each video in the playlist
            while True:
                # Get playlist data using the YouTube PlaylistItems API 
                # Note: Each loop uses 1 out of 10.000 units from the daily usage limit (1 unit for 50 videos)
                playlist_data = youtube.playlistItems().list(
                    part="snippet", 
                    playlistId=uploads_playlist_id, 
                    maxResults=50,
                    pageToken=next_page_token
                ).execute()

                # Initialize an empty list to store video IDs
                video_ids = []

                # Extract video IDs from the playlist data
                video_ids += [video_data["snippet"]["resourceId"]["videoId"] for video_data in playlist_data["items"]]

                # Get video data using the YouTube Videos API 
                # Note: Uses 1 out of 10.000 units from the daily usage limit (1 unit for 50 videos)
                video_data = youtube.videos().list(part="statistics,snippet,contentDetails", id=video_ids).execute()    

                # Loop through each video 
                for video in video_data["items"]:
                    # Extract video data in dictionary format
                    video_dict = {
                        "video_id": video["id"],
                        "channel_id": video["snippet"]["channelId"],
                        "video_title": video["snippet"]["title"],
                        "video_description": video["snippet"]["description"],
                        "published_at": datetime.strptime(video["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
                        "video_duration": video["contentDetails"]["duration"],
                        "views": int(video["statistics"]["viewCount"]),
                        "likes": int(video["statistics"]["likeCount"]),
                        "comments": int(video["statistics"]["commentCount"])
                    }

                    try:
                        # Try to get thumbnail in maximum resolution
                        video_dict["thumbnail_url"] = video["snippet"]["thumbnails"]["maxres"]["url"]
                    except KeyError:
                        try:
                            # If maxres is not available, get high resolution
                            video_dict["thumbnail_url"] = video["snippet"]["thumbnails"]["high"]["url"]
                        except KeyError:
                            # If high resolution is not available, get default resolution
                            video_dict["thumbnail_url"] = video["snippet"]["thumbnails"]["default"]["url"]

                    # Append video data in dictionary format to the list
                    videos_ls.append(video_dict)

                # Get the next page token
                next_page_token = playlist_data.get("nextPageToken")

                # Exit the loop if there are no more pages
                if next_page_token is None:
                    break
                
        # Convert list of dictionaries to pandas DataFrame
        videos_df = pd.DataFrame(videos_ls)  

        # Save pandas DataFrame as CSV file
        videos_df.to_csv("/opt/airflow/data/videos_df_extracted.csv")  

        # Extract comments data
        # Initialize an empty list to store comments
        comments_ls = []

        # Loop through each video
        for video_id in videos_df["video_id"].values:
            # Initialize next_page_token to None
            next_page_token = None

            # Loop through data batches of 100 comments 
            while True:
                try:
                    # Get data from 100 comments using the YouTube CommentThreads API 
                    # Note: Each loop uses 1 out of 10.000 units from the daily usage limit (1 unit for 100 comments)
                    comments_data = youtube.commentThreads().list(
                        part="snippet", 
                        videoId=video_id, 
                        maxResults=100,
                        pageToken=next_page_token
                    ).execute()
                # Handle error if e.g. video comments are disabled
                except Exception as e:
                    print(f"Failed to get comments for video {video_id}.")

                # Loop through each comment
                for comment in comments_data["items"]:
                    # Extract comment data in dictionary format
                    comment_dict = {
                        "comment_id": comment["snippet"]["topLevelComment"]["id"],
                        "video_id": comment["snippet"]["topLevelComment"]["snippet"]["videoId"],
                        "channel_id": comment["snippet"]["topLevelComment"]["snippet"]["channelId"],
                        "comment_text": comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                        "published_at": datetime.strptime(comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
                    }
                    # Append comment data dictionary to the list
                    comments_ls.append(comment_dict)

                # Get the next page token
                next_page_token = comments_data.get("nextPageToken")

                # Exit the loop if there are no more pages
                if next_page_token is None: 
                    break
                
        # Convert list of dictionaries to pandas DataFrame
        comments_df = pd.DataFrame(comments_ls)    

        # Save pandas DataFrame as CSV file
        comments_df.to_csv("/opt/airflow/data/comments_df_extracted.csv")  
    
    # Transform data
    @task 
    def transform():
        # Function to convert the YouTube video duration from ISO 8601 format (str) to seconds (int)
        def convert_iso8601_duration(duration):
            # Regular expression to match hours, minutes, and seconds
            time_extractor = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?')
            # Extract hours, minutes, and seconds
            extracted = time_extractor.match(duration)
            if extracted:
                hours = int(extracted.group(1)) if extracted.group(1) else 0
                minutes = int(extracted.group(2)) if extracted.group(2) else 0
                seconds = int(extracted.group(3)) if extracted.group(3) else 0
                # Return total seconds
                total_seconds = hours * 3600 + minutes * 60 + seconds
                return total_seconds
            else:
                return 0
            
        # Load CSV file into pandas DataFrame
        videos_df = pd.read_csv("/opt/airflow/data/videos_df_extracted.csv")
        
        # Convert video duration 
        videos_df["video_duration"] = videos_df["video_duration"].apply(convert_iso8601_duration)
        
        # Save pandas DataFrame as CSV file
        videos_df.to_csv("/opt/airflow/data/videos_df_transformed.csv")

    # Load data from Pandas DataFrames into MySQL tables
    @task 
    def load():
        # Load CSV files into pandas DataFrames
        channel_df = pd.read_csv("/opt/airflow/data/channel_df_extracted.csv")
        videos_df = pd.read_csv("/opt/airflow/data/videos_df_transformed.csv")
        comments_df = pd.read_csv("/opt/airflow/data/comments_df_extracted.csv")
        
        # Connect to AWS RDS MySQL server instance
        connection = mysql.connector.connect(
            host = aws_mysql_endpoint,
            port = 3306,
            user = aws_mysql_user,
            password = aws_mysql_password,
            database = "youtube_analytics"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Drop existing MySQL tables 
        tables_to_drop = ["comments", "videos", "channels"]
        for table in tables_to_drop:
            cursor.execute(f"DROP TABLE IF EXISTS {table};")
                
        try:
            # Create an SQLAlchemy engine for interacting with the MySQL database
            engine = create_engine(f"mysql+mysqlconnector://{aws_mysql_user}:{aws_mysql_password}@{aws_mysql_endpoint}:3306/youtube_analytics") 
            
            # Load the YouTube channels DataFrame into the MySQL channels table
            try:
                channel_df.to_sql("channels", con=engine, if_exists="replace", index=False)
                print("Channels data successfully loaded into AWS MySQL database.")
            except Exception as e:
                print("Error loading channels data:", e)
            
            # Load the YouTube videos DataFrame into the MySQL videos table
            try:
                videos_df.to_sql("videos", con=engine, if_exists="replace", index=False)
                print("Videos data successfully loaded into AWS MySQL database.")
            except Exception as e:
                print("Error loading videos data:", e)
            
            # Load the YouTube comments DataFrame into the MySQL comments table
            try:
                comments_df.to_sql("comments", con=engine, if_exists="replace", index=False)
                print("Comments data successfully loaded into AWS MySQL database.")
            except Exception as e:
                print("Error loading comments data:", e)
            
        except Exception as e:
            # Print error if exception occurs when connecting to the database 
            print("Error connecting to AWS MySQL database:", e)

        finally:
            # Close the cursor and connection to free up resources
            cursor.close()
            connection.close()

    # Define task dependencies
    extract = extract()
    transform = transform()
    load = load()
    extract >> transform >> load 

# Create DAG instance
etl_pipeline = etl_pipeline()
