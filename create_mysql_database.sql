CREATE DATABASE youtube_analytics;
USE youtube_analytics;

CREATE TABLE channels (
    channel_name VARCHAR(255),
    channel_id VARCHAR(255),
    view_count INT,
    video_count INT,
    subscriber_count INT
);
