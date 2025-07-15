# 🎬 YouTube Video & Audio Downloader (Flask + SocketIO)

Ein moderner YouTube-Downloader mit Vorschaufunktion, stylischem Webinterface und einfacher Bedienung – entwickelt mit ❤️ in Python & Flask.

---

## 🚀 Features

- 🔎 **Vorschau vor dem Download** (Titel, Thumbnail, Dauer, Kanal)
- 🎥 **Video- und Audio-Download** (MP4 & MP3)
- 📦 Playlist-Support (optional)
- 📁 Automatischer Dateiname + direkter Download-Link
- ✅ Unterstützt auch YouTube Shorts, Musikvideos & Livestreams (sofern erlaubt)

---

## 🖼 Vorschau

![screenshot](static/assets/screenshot.png)

---

## 🛠️ Installation (lokal)

### 1. Klone das Repository

```bash
git clone https://github.com/Mandi040Gaming/YouTube-Downloader
cd youtube-downloader
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. (Optional) `cookies.txt` für YouTube-Login hinzufügen

Manche Inhalte (z. B. Musikvideos, Altersbeschränkungen) erfordern Login.  
→ Exportiere deine Cookies mit der [Get cookies.txt Extension](https://chrome.google.com/webstore/detail/get-cookiestxt/oeopbcgkkoapgobdbedcemjljbihmemj)  
→ Speichere sie im Projekt als `cookies.txt`

---

## 🧪 Lokaler Start

```bash
python app.py
```

Dann öffne [http://localhost:5000](http://localhost:5000) im Browser.

---

## 🌐 Deployment (z. B. auf Render)

### 1. Benötigte Dateien:
- `requirements.txt`
- `Procfile` mit:
  ```
  web: gunicorn app:app --worker-class eventlet -w 1
  ```
- `render.yaml` (optional)

### 2. Wichtig:
- Nutze `gunicorn` + `eventlet` für SocketIO
- Füge `gunicorn` in `requirements.txt` ein

---

## ⚠️ Rechtlicher Hinweis

Dieses Projekt dient **ausschließlich zu Bildungszwecken**.  
Der Download urheberrechtlich geschützter Inhalte ohne Erlaubnis ist in vielen Ländern **verboten**.  
Bitte halte dich an die [YouTube-Nutzungsbedingungen](https://www.youtube.com/t/terms).

---

## 📄 Lizenz

MIT License – Nutz es, verbesser es, teile es! 😎

---

## ✨ Mitmachen

Pull Requests, Bug Reports & Feature-Ideen sind jederzeit willkommen!  
Dieses Projekt ist offen für die Community. 💙

---

## 👨‍💻 Autor

> Entwickelt von [Mandi040Gaming](https://github.com/Mandi040Gaming)
