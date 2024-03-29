CREATE DATABASE youtube_analytics;
USE youtube_analytics;

CREATE TABLE channels (
    channel_id VARCHAR(255) PRIMARY KEY,
    channel_name VARCHAR(255),
    views INT,
    videos INT,
    subscribers INT
);

CREATE TABLE videos (
    video_id VARCHAR(255) PRIMARY KEY,
    channel_id VARCHAR(255),
    video_title VARCHAR(255),
    video_description TEXT,
    published_at DATETIME,
    video_duration INT,
    views INT,
    likes INT,
    comments INT,
    thumbnail_url VARCHAR(255),
	FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE
);

CREATE TABLE comments (
    comment_id VARCHAR(255) PRIMARY KEY,
    video_id VARCHAR(255),
    channel_id VARCHAR(255),
    comment_text TEXT,
    FOREIGN KEY (video_id) REFERENCES videos(video_id) ON DELETE CASCADE,
    FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE
);
