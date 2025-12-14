import time
import sqlite3
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

WATCH_FOLDER = "data"
DB_FILE = "database.db"

# Convert filename to table name
def make_table_name(filename):
    name = os.path.splitext(os.path.basename(filename))[0]
    return "uploaded_" + name.lower().replace(" ", "_")

# UPLOAD CSV TO DATABASE (AUTO TABLE CREATION PER FILE)
def upload_csv_to_db(path):
    try:
        print(f"[INFO] Reading file: {path}")
        df = pd.read_csv(path)

        table_name = make_table_name(path)

        conn = sqlite3.connect(DB_FILE)

        # CREATE / REPLACE TABLE unique to file
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        conn.close()

        print(f"[SUCCESS] Uploaded into table → {table_name}")

    except Exception as e:
        print(f"[ERROR] Failed to upload {path}: {e}")


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        print(f"[DETECTED] New file → {event.src_path}")

        if event.src_path.endswith(".csv"):
            upload_csv_to_db(event.src_path)
        else:
            print("[SKIPPED] Not a CSV file")


if __name__ == "__main__":
    print("📌 File Listener Started!")
    print("📂 Monitoring folder:", WATCH_FOLDER)
    print("⏳ Waiting for new CSV files...\n")

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
