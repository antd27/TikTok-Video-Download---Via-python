import os
import yt_dlp

def download_tiktok_to_device(video_url):
    # Dynamically finds your Mac's Downloads folder
    download_folder = os.path.expanduser("~/Downloads")
    
    # Combines the folder path with the filename template
    output_path = os.path.join(download_folder, "%(id)s.%(ext)s")

    ydl_opts = {
        'outtmpl': output_path,
    }
    
    print(f"Downloading video to: {download_folder}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

url = "https://www.tiktok.com/@j.c.o.media/video/7465017760863636767?q=cars&t=1787337536392"
download_tiktok_to_device(url)
