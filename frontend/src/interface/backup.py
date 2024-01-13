from tkinter import filedialog

import time
import json
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

STATE_FILE = "config.json"

class BackupHandler(FileSystemEventHandler):
    def __init__(self, src_dir, dest_dir):
        super().__init__()
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified. Starting backup...')
        self.backup(message="")

    def on_created(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been created. Starting backup...')
        self.backup(message="")

    def backup(self,message):
        try:
            shutil.copytree(self.src_dir, self.dest_dir, dirs_exist_ok=True)
            if message:
                print(message)
                return
            print('Backup Successful!')
        except Exception as e:
            print(f'Error occurred during backup:\n{e}')       

def loadObserverState():
    try:
        with open(STATE_FILE,"r") as stateFile:
            state = json.load(stateFile)
            return state
    except (FileNotFoundError):
        return None

def saveObserverState(state):
    with open(STATE_FILE,"w") as stateFile:
        json.dump(state,stateFile)


def startAutoBackup(src_dir, dest_dir):
    event_handler = BackupHandler(src_dir, dest_dir)
    observer = Observer()
    observer.schedule(event_handler, path=src_dir, recursive=True)
    observer.start()
    event_handler.backup(message='Initial Backup Successful...')
    print("Auto backup Started...")

    try:
        while True:
            time.sleep(1)
    except:
        observer.stop()
        print("Auto Backup Stopped.")
        observer.join()


# Will be done by the GUI
if __name__ == "__main__":
    # Specify your source and destination directories
    source_directory = filedialog.askdirectory(title='Select the directory for backup')
    destination_directory = filedialog.askdirectory(title='Select the location for backup')

    # Start the automatic backup system
    startAutoBackup(source_directory, destination_directory)
