import yt_dlp
from dotenv import load_dotenv
import os

def dl_video(url, pathVideo):
    load_dotenv()
    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "")

    try:
        # Opzioni di configurazione
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{pathVideo}/videodl.mp4' if pathVideo else 'videodl.mp4',
            'ffmpeg_location': FFMPEG_PATH
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download completed!")
        
    except Exception as e:
        print(f"error: {e}")