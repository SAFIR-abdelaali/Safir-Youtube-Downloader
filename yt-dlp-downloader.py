import os
import subprocess
import re
from urllib.parse import urlparse, parse_qs
import json

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def get_video_info(url):
    try:
        cmd = [
            'yt-dlp',
            '--skip-download',
            '--dump-json',
            url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error getting video info: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def download_content(url, output_path="downloads", audio_only=False, playlist=False):
    try:
        os.makedirs(output_path, exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            '--no-playlist' if not playlist else '--yes-playlist',
            '--quiet',
            '--no-warnings',
            '--progress'
        ]
        if audio_only:
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '0',
                '--embed-thumbnail'
            ])
        else:
            cmd.extend([
                '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                '--merge-output-format', 'mp4'
            ])
        cmd.append(url)
        print(f"Downloading {'audio' if audio_only else 'video'} from {url}...")
        subprocess.run(cmd, check=True)
        print("Download completed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def is_playlist(url):
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        return 'list' in query
    except Exception:
        return False

def main():
    print("El Hacho Downloader")
    print("Choose an option:")
    print("1. Download single video")
    print("2. Download single video as MP3")
    print("3. Download playlist videos")
    print("4. Download playlist as MP3s")
    print("5. Exit")
    
    try:
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "5":
            print("Exiting the program.")
            return 
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return
        url = input("Enter YouTube URL: ").strip()
        if not url:
            print("URL cannot be empty.")
            return
        output_dir = "downloads"
        playlist = is_playlist(url)
        if choice == "1":
            download_content(url, output_dir, False, False)
        elif choice == "2":
            download_content(url, output_dir, True, False)
        elif choice == "3":
            download_content(url, output_dir, False, True)
        elif choice == "4":
            download_content(url, output_dir, True, True)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()