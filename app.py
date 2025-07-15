from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import uuid
from utils import download_video, validate_youtube_url

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = "static/downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/info", methods=["POST"])
def info():
    data = request.get_json()
    url = data.get("url")

    if not url or not validate_youtube_url(url):
        return jsonify({"error": "Ungültiger Link"}), 400

    try:
        from yt_dlp import YoutubeDL
        with YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        return jsonify({
            "title": info.get("title"),
            "duration": info.get("duration"),
            "thumbnail": info.get("thumbnail"),
            "channel": info.get("uploader"),
            "is_playlist": "_type" in info and info["_type"] == "playlist"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    url = data.get("url")
    format = data.get("format", "mp4")
    quality = data.get("quality", "best")
    playlist = data.get("playlist", False)

    if not url or not validate_youtube_url(url):
        return jsonify({"error": "Ungültiger Link"}), 400

    uid = str(uuid.uuid4())
    try:
        result = download_video(
            url=url,
            format=format,
            quality=quality,
            uid=uid,
            download_folder=DOWNLOAD_FOLDER,
            playlist=playlist
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/file/<filename>")
def serve_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
