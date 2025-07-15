import os
import re
from yt_dlp import YoutubeDL


def validate_youtube_url(url):
    return re.match(r"(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+", url)


def download_video(url, format, quality, uid, download_folder, playlist=False):
    filename = f"{uid}.%(ext)s"
    filepath = os.path.join(download_folder, filename)

    ydl_opts = {
        "outtmpl": filepath,
        "quiet": True,
        "noplaylist": not playlist,
    }

    if format == "mp3":
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        })
    elif format == "mp4":
        ydl_opts.update({
            "format": quality if quality != "best" else "bestvideo+bestaudio/best",
            "merge_output_format": "mp4"
        })
    else:
        raise Exception("Unbekanntes Format")

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = "mp3" if format == "mp3" else "mp4"
        final_name = f"{uid}.{ext}"

    return {
        "success": True,
        "title": info.get("title", "Video"),
        "download_url": f"/file/{final_name}"
    }
