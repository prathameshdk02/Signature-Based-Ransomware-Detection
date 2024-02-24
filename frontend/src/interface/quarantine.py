from cryptography.fernet import Fernet
import subprocess
import os
import json

encrypKey = b"DW0wxBrVDUNmsZVlbaigRPhDedXBPqIvUJ6_3Lyx6m0="

QUARANTINE_PATH = 'C:/SBRDS_Map/.quarantine'

def createMappingFolder():
    if os.name == "nt":
        os.makedirs("C:/SBRDS_Map/.quarantine", exist_ok=True)
        with open("C:/SBRDS_Map/filemap.mp", "w"):
            pass
        subprocess.run(["attrib", "+h", "C:/SBRDS_Map"], shell=True)


def checkMappingExistence():
    if os.name == "nt":
        return os.path.exists("C:/SBRDS_Map/filemap.mp")

def isPresentInMappings(fileObj, originalPathList):
    for obj in originalPathList:
        if obj['name'] == fileObj['name']:
            return True
    return False


def getMapData():
    with open("C:/SBRDS_Map/filemap.mp", "r") as mapFile:
        try:
            mappings = json.load(mapFile)
        except:
            mappings = []
            return mappings
                
        originalPathList = [
            {"name": mapping["name"], "ogLocation": mapping["ogLocation"]}
            for mapping in mappings
        ]

    return originalPathList        

def quarantineFiles(filePath_list):
    # Check for hidden Mapping Folder...
    if not checkMappingExistence():
        createMappingFolder()

    originalPathList = getMapData()

    # Setting up Fernet Cipher...
    fernetCipher = Fernet(encrypKey)

    for fp in filePath_list:
        # Quarantine Logic...
        fileNameWithExt = os.path.basename(fp)

        with open(fp, "rb") as file:
            # Read & Encrypt file data...
            fileData = file.read()
            encrypData = fernetCipher.encrypt(fileData)

            # Obtain final path including encrypted filename..
            destPath = os.path.join(QUARANTINE_PATH, fileNameWithExt)

            with open(destPath + ".mal", "wb") as wrtFile:
                wrtFile.write(encrypData)
                fileObj = {
                    'name': fileNameWithExt,
                    'ogLocation': fp
                }
                
                # Check if already present...
                if not isPresentInMappings(fileObj,originalPathList):
                    originalPathList.append(fileObj)

                print(f"File {fp} was quarantined at {QUARANTINE_PATH}")

        # Delete source file...
        try:
            os.remove(fp)
        except FileNotFoundError:
            print("File doesn't Exist!")
        except PermissionError:
            print("Permission Denied.") 

    with open("C:/SBRDS_Map/filemap.mp", "w") as mapFile:
        json.dump(originalPathList,mapFile)
        pass

    return

def removeFiles(filepath_list):
    for filepath in filepath_list:
        try:
            os.remove(filepath)
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print('Permission Denied.')


def liberateFiles(filename_list):
    originalPathList = getMapData()

    for filename in filename_list:
        # Get to the quarntined Files...
        quarnFilePath = os.path.join(QUARANTINE_PATH, filename)

        fernetCipher = Fernet(encrypKey)

        quarnFileOGPath = ''
        toRemoveIndex = []

        # check required for knowing if the file is present in originalPathList
        for mapIndex, mapping in enumerate(originalPathList):
            if mapping['name'] == filename:
                quarnFileOGPath = mapping['ogLocation']
                toRemoveIndex.append(mapIndex)

        with open(quarnFilePath + '.mal', 'rb') as quarnFile:
            encrypData = quarnFile.read()
            decrypData = fernetCipher.decrypt(encrypData)

            with open(quarnFileOGPath,'wb') as ogFile:
                ogFile.write(decrypData)
                print(f"Restored {filename} to {quarnFileOGPath}")

        # Remove mappings that were restored...
        for index in toRemoveIndex:
            originalPathList.pop(index)

        # remove quarantined files...
        

        # Update the map file
        with open("C:/SBRDS_Map/filemap.mp", "w") as mapFile:
            json.dump(originalPathList, mapFile)
            pass   

    return

def liberateAllFiles():
    originalPathList = getMapData()

    filename_list = []
    for mapping in originalPathList:
        filename_list.append(mapping["name"])

    liberateFiles(filename_list)    






if __name__ == "__main__":
    # fpList = ['C:/Users/prath/Downloads/Meslo.zip']
    # quarantineFiles(fpList)
    # liberateFiles(['Meslo.zip'])
    # print(checkMappingExistence())
    pass
