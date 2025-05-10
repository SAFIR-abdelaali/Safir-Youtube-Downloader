# El Hacho Downloader

A Python script for downloading YouTube videos and playlists in MP4 or MP3 format using `yt-dlp`.

## Features

- Download single videos (MP4 format)
- Extract audio from videos (MP3 format)
- Download entire playlists
- Automatic folder creation
- Clean filenames (removes invalid characters)
- Progress display during downloads

## Requirements

- Python 3.6+
- yt-dlp (`pip install yt-dlp`)

## Installation

1. Clone this repository or download the script
2. Install dependencies:
   ```bash
   pip install yt-dlp


## Usage (windows)
py youtube_downloader.py

## Output Files
All downloads are saved in a downloads folder in the same directory as the script:
Videos: [video-title].mp4
Audio: [video-title].mp3
The folder is created automatically if it doesn't exist.

## if ffmpeg not found
- Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/
- Choose the "ffmpeg-git-full.7z" version
- Extract the downloaded file
- Move the ffmpeg.exe, ffprobe.exe, and ffplay.exe files to the same folder as your Python script

## Honorable mention
You are allowed to modify this code as you wish, but give credits!

Enjoy downloading!