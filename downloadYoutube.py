import os
import re
from pathlib import Path
from datetime import datetime
import yt_dlp

def sanitize_filename(name, max_length=150):
    """
    Sanitizes the video title to be used as a filename.
    Replaces spaces with underscores, removes invalid characters,
    and truncates to a maximum length.
    """
    name = re.sub(r'\s+', '_', name)  # Replace spaces with underscores
    name = re.sub(r'[\\/:"*?<>|]+', '', name)  # Remove invalid characters for file names
    return name[:max_length]  # Truncate to max_length

def fetch_video_title(link):
    """
    Fetches the video title from the YouTube link using yt-dlp.
    """
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link, download=False)
            return info.get('title', 'unknown_video')
    except Exception as e:
        print(f"✗ Could not fetch title for {link}. Error: {e}")
        return 'unknown_video'

def download_video(link, download_folder):
    """
    Downloads the video using yt-dlp with a sanitized title as the filename.
    """
    try:
        print(f"Fetching video title for: {link}...")
        title = fetch_video_title(link)
        sanitized_title = sanitize_filename(title)
        output_template = os.path.join(download_folder, f"{sanitized_title}.%(ext)s")

        print(f"Downloading: {link} as '{sanitized_title}'...")
        ydl_opts = {
            'outtmpl': output_template,
            'format': 'bestvideo+bestaudio/best',  # Best quality
            'merge_output_format': 'mp4'  # Ensures output is MP4
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print(f"✓ Successfully downloaded: {sanitized_title}\n")
        return True
    except Exception as e:
        print(f"✗ Failed to download {link}. Error: {e}\n")
        return False

def get_download_folder():
    """
    Creates a folder with the current date in the current directory.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    download_folder = os.path.join(os.getcwd(), current_date)

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Created folder: {download_folder}")
    return download_folder

def main():
    # file = input("Enter the text filename with the YouTube links: ").strip()
    file = "videos.txt"
    download_folder = get_download_folder()

    if not os.path.isfile(file):
        print(f"File '{file}' not found.")
        return

    with open(file, "r") as f:
        links = [line.strip() for line in f.readlines() if line.strip()]

    for idx, link in enumerate(links, start=1):
        print(f"Processing {idx}/{len(links)}...")
        download_video(link, download_folder)

if __name__ == "__main__":
    main()
