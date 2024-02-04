import os
import shutil
import pyzipper
from pathlib import Path


def createEncryptedBackup(source_dir, dest_dir, zip_filename, mpQueue):
    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    temp_dir = os.path.join(dest_dir, "_temp_backup")
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
        with pyzipper.AESZipFile(
            zip_filepath,
            "w",
            compression=pyzipper.ZIP_LZMA,
            encryption=pyzipper.WZ_AES,
        ) as zipf:
            zipf.setpassword(bytes("rkCSz2Cxl1NyLSly6gxlhjUC", "utf-8"))
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname=arcname)

        # Need to Change file extension if possible... (Not implemented.)

        print(f"Backup successfully created at: {zip_filepath}")
        result = mpQueue.get()
        result["success"] = True
        mpQueue.put(result)
    except Exception as e:
        print(e)
    finally:
        shutil.rmtree(temp_dir)


def readEncryptedBackup(backup_file_path, destination_path):
    with pyzipper.AESZipFile(backup_file_path) as ef:
        ef.setpassword(bytes("rkCSz2Cxl1NyLSly6gxlhjUC", "utf-8"))
        # Need a check for availabe disk space.
        extractPath = os.path.join(
            destination_path,
            "Restored_" + os.path.splitext(os.path.basename(backup_file_path))[0],
        )
        Path(extractPath).mkdir(parents=True)
        ef.extractall(extractPath)
    return


# backup_eb_ --> [0:10]
def retrieveBackupZips(lookout_dir):
    backupZips = []
    try:
        for root, dirs, files in os.walk(lookout_dir):
            for file in files:
                fileExten = os.path.splitext(file)[1]
                fileIniti = os.path.splitext(file)[0][0:10]
                if fileIniti == "backup_eb_" and fileExten == ".zip":
                    filePath = Path.joinpath(Path(root), file)
                    backupZips.append(filePath.as_posix())

            break
        # print(backupZips)
        return backupZips
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    # readEncryptedBackup("C:/Users/prath/OneDrive/Desktop/dest/backup_2024-01-15_21-27-06.zip","C:/Users/prath/OneDrive/Desktop/dest")
    # retrieveBackupZips("C:/Users/prath/OneDrive/Desktop/dest")
    pass
