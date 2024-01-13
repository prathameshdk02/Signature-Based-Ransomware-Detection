import os
import shutil
import pyzipper
import datetime
from pathlib import Path

def createEncryptedBackup(source_dir, dest_dir, zip_filename, password, mpQueue):
    password = bytes(password,'utf-8')

    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    temp_dir = os.path.join(dest_dir, '_temp_backup')
    Path(temp_dir).mkdir(parents=True, exist_ok=True)

    try:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                dest_path = os.path.join(temp_dir, relative_path)
                Path(os.path.dirname(dest_path)).mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, dest_path)


        zip_filepath = os.path.join(dest_dir, zip_filename)
        with pyzipper.AESZipFile(zip_filepath, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES,) as zipf:
            zipf.setpassword(password)
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname=arcname)

        print(f'Backup successfully created at: {zip_filepath}')
        result = mpQueue.get()
        result["success"] = True
        mpQueue.put(result)
    except Exception as e:
        print(e)
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    source_directory = "C:/Users/prath/OneDrive/Desktop/AutoBackup/source"
    destination_directory = "C:/Users/prath/OneDrive/Desktop/AutoBackup/dest"

    backup_password = "your_strong_password"

    current_datetime = datetime.datetime.now()
    timestamp_string = current_datetime.strftime("%Y%m%d_%H%M%S")
    zip_filename = f"backup_{timestamp_string}.zip"

    createEncryptedBackup(source_directory, destination_directory, zip_filename, backup_password)
