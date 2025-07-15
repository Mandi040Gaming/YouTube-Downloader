import os
import time

DOWNLOAD_FOLDER = "static/downloads"
MAX_AGE = 3600  # 1 Stunde


def cleanup():
    now = time.time()
    for file in os.listdir(DOWNLOAD_FOLDER):
        path = os.path.join(DOWNLOAD_FOLDER, file)
        if os.path.isfile(path) and now - os.path.getmtime(path) > MAX_AGE:
            os.remove(path)
            print("Gelöscht:", file)


if __name__ == "__main__":
    cleanup()
