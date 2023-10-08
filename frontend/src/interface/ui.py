import customtkinter as ctk
from customtkinter import filedialog
from tkinter import IntVar
from PIL import Image, ImageTk

import hashlib
from pathlib import Path
from datetime import datetime
from time import time
import requests


# Frame Foreground Colors
baseFrameFG = "#dfdfdf"
baseFrameChildFG = "#ebebeb"
baseFrameChildBC = "#b7b7b7"
frameLabelFG = "#0078d4"
frameLabelTextColor = "#dce4ee"
frameTextColorPrimary = "grey"
frameTextColorSecondary = "#6f6f6f"

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk(fg_color=baseFrameFG)

app.title("Ransomware Detection")
app.resizable(False, False)
app.geometry("900x500")


# Fonts
fontFrameLabelBold = ctk.CTkFont("Segoe UI", 13, "bold")
fontFrameLabel = ctk.CTkFont("Segoe UI", 13)
baseFramePadY = (10, 10)
baseFramePadX = (10, 10)

baseFrameLeft = ctk.CTkFrame(app, corner_radius=12, fg_color=baseFrameFG)
baseFrameLeft.pack(side="left", fill="both", pady=baseFramePadY, padx=baseFramePadX)

baseFrameMid = ctk.CTkFrame(app, width=400, fg_color=baseFrameFG)
baseFrameMid.pack(side="left", fill="both", expand=True, pady=baseFramePadY)

baseFrameRight = ctk.CTkFrame(
    app,
    corner_radius=12,
    fg_color=baseFrameFG,
)
baseFrameRight.pack(side="left", fill="both", pady=baseFramePadY, padx=baseFramePadX)

# Child Frames of baseFrameLeft
baseFrameLeft1 = ctk.CTkFrame(
    baseFrameLeft,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=225,
)
baseFrameLeft1.pack(side="top", fill="both", pady=(0, 5))

baseFrameLeft2 = ctk.CTkFrame(
    baseFrameLeft,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
)
baseFrameLeft2.pack(side="top", fill="both", pady=(5, 0))

# Child frames of baseFrameMid
baseFrameMid1 = ctk.CTkFrame(
    baseFrameMid,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=185,
    width=400,
)
baseFrameMid1.pack(side="top", fill="x", ipadx=5, ipady=5, pady=(0, 5))

baseFrameMid2 = ctk.CTkFrame(
    baseFrameMid,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=155,
    width=400,
)
baseFrameMid2.pack(side="top", fill="x", pady=(5, 5))

baseFrameMid3 = ctk.CTkFrame(
    baseFrameMid,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=155,
    width=400,
)
baseFrameMid3.pack(side="top", fill="x", pady=(5, 5))

# Input File Details Pane..
frameLabelLeft2 = ctk.CTkLabel(
    baseFrameLeft1,
    text="Selected Files.",
    font=fontFrameLabelBold,
    width=100,
    height=30,
    fg_color="white",
    text_color=frameTextColorPrimary,
    padx=10,
    corner_radius=8,
)
frameLabelLeft2.place(x=70, y=10)

frameLabelLeft1 = ctk.CTkLabel(
    baseFrameLeft1,
    text="Details",
    font=fontFrameLabelBold,
    width=60,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    padx=10,
    corner_radius=8,
)
frameLabelLeft1.place(x=0, y=10)

detailLabelName = ctk.CTkLabel(
    baseFrameLeft1,
    text="Name:",
    font=fontFrameLabelBold,
    width=30,
    height=20,
    text_color=frameTextColorSecondary,
)
detailLabelName.place(x=10, y=50)

detailLabelExten = ctk.CTkLabel(
    baseFrameLeft1,
    text="Extension:",
    font=fontFrameLabelBold,
    width=30,
    height=20,
    text_color=frameTextColorSecondary,
)
detailLabelExten.place(x=10, y=70)

detailLabelAccess = ctk.CTkLabel(
    baseFrameLeft1,
    text="Creation:",
    font=fontFrameLabelBold,
    width=30,
    height=20,
    text_color=frameTextColorSecondary,
)
detailLabelAccess.place(x=10, y=90)

detailLabelSize = ctk.CTkLabel(
    baseFrameLeft1,
    text="Size:",
    font=fontFrameLabelBold,
    width=30,
    height=20,
    text_color=frameTextColorSecondary,
)
detailLabelSize.place(x=10, y=110)

detailLabelSHA = ctk.CTkLabel(
    baseFrameLeft1,
    text="SHA-256:",
    font=fontFrameLabelBold,
    width=30,
    height=20,
    text_color=frameTextColorSecondary,
)
detailLabelSHA.place(x=10, y=130)

# Actual Detail Values (Updated Dynamically)

detailValueName = ctk.CTkLabel(
    baseFrameLeft1,
    text="No File Selected.",
    font=fontFrameLabel,
    height=20,
    text_color=frameTextColorSecondary,
)
detailValueName.place(x=60, y=50)

detailValueExten = ctk.CTkLabel(
    baseFrameLeft1,
    text="No File Selected.",
    font=fontFrameLabel,
    height=20,
    text_color=frameTextColorSecondary,
)
detailValueExten.place(x=80, y=70)

detailValueCreation = ctk.CTkLabel(
    baseFrameLeft1,
    text="No File Selected.",
    font=fontFrameLabel,
    height=20,
    text_color=frameTextColorSecondary,
)
detailValueCreation.place(x=70, y=90)

detailValueSize = ctk.CTkLabel(
    baseFrameLeft1,
    text="No File Selected.",
    font=fontFrameLabel,
    height=20,
    text_color=frameTextColorSecondary,
)
detailValueSize.place(x=45, y=110)

detailValueSHA = ctk.CTkLabel(
    baseFrameLeft1,
    text="No File Selected.",
    font=fontFrameLabel,
    height=20,
    text_color=frameTextColorSecondary,
)
detailValueSHA.place(x=10, y=150)


def getFileStats(path):
    file = Path(path)
    detailValueName.configure(text=file.name)
    detailValueExten.configure(text=file.suffix)
    detailValueCreation.configure(
        text=datetime.strftime(
            datetime.fromtimestamp(file.stat().st_ctime), "%d-%m-%Y, %H:%M"
        )
    )
    detailValueSize.configure(text=file.stat().st_size)
    detailValueSHA.configure(text=hashlib.sha256(file.read_bytes()).hexdigest())


def getPrevFileStats():
    currentFileIndex = inputFiles.index(inputComboSelected.get())
    if currentFileIndex == 0:
        currentFileIndex = len(inputFiles) - 1
    else:
        currentFileIndex -= 1

    inputComboSelected.set(inputFiles[currentFileIndex])
    getFileStats(inputFiles[currentFileIndex])


def getNextFileStats():
    currentFileIndex = inputFiles.index(inputComboSelected.get())
    if currentFileIndex == len(inputFiles) - 1:
        currentFileIndex = 0
    else:
        currentFileIndex += 1

    inputComboSelected.set(inputFiles[currentFileIndex])
    getFileStats(inputFiles[currentFileIndex])


filePrevButton = ctk.CTkButton(
    baseFrameLeft1,
    corner_radius=4,
    text="<",
    width=35,
    height=30,
    fg_color=frameLabelFG,
    anchor="center",
    font=ctk.CTkFont("Arial", 15, "bold"),
    command=getPrevFileStats,
)
filePrevButton.place(x=10, y=185)

fileNextButton = ctk.CTkButton(
    baseFrameLeft1,
    corner_radius=4,
    text=">",
    width=35,
    height=30,
    fg_color=frameLabelFG,
    anchor="center",
    font=ctk.CTkFont("Arial", 15, "bold"),
    command=getNextFileStats,
)
fileNextButton.place(x=155, y=185)


# Input Frame Content
frameLabelMid2 = ctk.CTkLabel(
    baseFrameMid1,
    text="Select one or more files for input.",
    font=fontFrameLabelBold,
    width=250,
    height=30,
    fg_color="white",
    text_color=frameTextColorPrimary,
    padx=10,
    corner_radius=8,
)
frameLabelMid2.place(x=65, y=10)

frameLabelMid1 = ctk.CTkLabel(
    baseFrameMid1,
    text="Input",
    font=fontFrameLabelBold,
    width=75,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
frameLabelMid1.place(x=0, y=10)


def comboBoxHandler(choice):
    getFileStats(choice)


inputFiles = []
inputComboSelected = ctk.StringVar(value="")

# Add Callback later for deleting entries...
inputComboBox = ctk.CTkComboBox(
    baseFrameMid1,
    width=320,
    height=30,
    values=inputFiles,
    state="disabled",
    variable=inputComboSelected,
    font=fontFrameLabel,
    dropdown_font=fontFrameLabel,
    command=comboBoxHandler,
)
inputComboBox.place(x=15, y=55)


def openFile():
    global inputFiles
    inputFiles = list(filedialog.askopenfilenames())

    if len(inputFiles) != 0:
        inputComboBox.configure(
            values=inputFiles, state="normal", button_color=frameLabelFG
        )
        if len(inputFiles) == 1:
            frameLabelLeft2.configure(text="Selected File.")
            fileNextButton.configure(state="disabled")
            filePrevButton.configure(state="disabled")
        else:
            fileNextButton.configure(state="normal")
            filePrevButton.configure(state="normal")

        inputComboSelected.set(inputFiles[0])
        getFileStats(inputComboSelected.get())


chooseButton = ctk.CTkButton(
    baseFrameMid1,
    corner_radius=6,
    text="Select",
    width=70,
    height=30,
    fg_color=frameLabelFG,
    anchor="center",
    font=fontFrameLabelBold,
    command=openFile,
)
chooseButton.place(x=345, y=55)

# Input Frame Scan Options..
frameLabelMid4 = ctk.CTkLabel(
    baseFrameMid1,
    text="Choose scan options.",
    font=fontFrameLabelBold,
    width=150,
    height=30,
    fg_color="white",
    text_color=frameTextColorPrimary,
    corner_radius=8,
    padx=10,
)
frameLabelMid4.place(x=70, y=100)

frameLabelMid3 = ctk.CTkLabel(
    baseFrameMid1,
    text="Options",
    font=fontFrameLabelBold,
    width=75,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
frameLabelMid3.place(x=0, y=100)


# Scan Option Radio Buttons...
scanRadio_var = IntVar(value=1)
scanRadioSingle = ctk.CTkRadioButton(
    baseFrameMid1,
    text="Single File Scan",
    variable=scanRadio_var,
    value=1,
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
)
scanRadioSingle.place(x=20, y=148)

scanRadioMultiple = ctk.CTkRadioButton(
    baseFrameMid1,
    text="Multiple File Scan",
    variable=scanRadio_var,
    value=2,
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
)
scanRadioMultiple.place(x=170, y=148)

# Results Rendering Code..

scanResults = {}

# To be Refactored...
def renderScanResults(result):
    # Render the Child Frame...
    baseFrameRight1 = ctk.CTkFrame(
        baseFrameRight,
        corner_radius=12,
        fg_color=baseFrameChildFG,
        border_color=baseFrameChildBC,
        border_width=1,
    )
    baseFrameRight1.pack(side="top", expand=True, fill="both")

    if result["isSafe"]:
        # Render Safe Results...
        frameLabelRight1 = ctk.CTkLabel(
            baseFrameRight1,
            text="Results",
            font=fontFrameLabelBold,
            width=80,
            height=30,
            fg_color=frameLabelFG,
            text_color=frameLabelTextColor,
            corner_radius=4,
        )
        frameLabelRight1.place(x=0, y=10)

        safeImage = ctk.CTkImage(
            Image.open(__file__ + "/../../../assets/img/safe.png"), size=(125, 125)
        )
        safeImageLabel = ctk.CTkLabel(baseFrameRight1, image=safeImage, text="")
        safeImageLabel.place(x=35, y=60)

        safeResultsLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Safe",
            width=100,
            text_color="#017dcc",
            font=ctk.CTkFont("Segoe UI", 34, "bold"),
        )
        safeResultsLabel.place(x=55, y=195)

        safeResultsSubLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="The file looks Safe.",
            text_color=frameTextColorSecondary,
            font=fontFrameLabelBold,
        )
        safeResultsSubLabel.place(x=45, y=237)

        safeScanDetailsSubLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Scan Details",
            font=fontFrameLabelBold,
            width=120,
            height=30,
            fg_color="white",
            text_color=frameTextColorPrimary,
            corner_radius=4,
        )
        safeScanDetailsSubLabel.place(x=68, y=290)

        safeScanDetailsLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Info.",
            font=fontFrameLabelBold,
            width=75,
            height=30,
            fg_color=frameLabelFG,
            text_color=frameLabelTextColor,
            corner_radius=4,
        )
        safeScanDetailsLabel.place(x=0, y=290)

        # Safe Scan Statistics...

        scanStatsStatus = ctk.CTkLabel(
            baseFrameRight1,
            text="File Name:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsStatus.place(x=10, y=330)

        scanStatsStatus = ctk.CTkLabel(
            baseFrameRight1,
            text="Status:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsStatus.place(x=10, y=350)

        scanStatsRansom = ctk.CTkLabel(
            baseFrameRight1,
            text="Ransomware:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsRansom.place(x=10, y=370)

        scanStatsSeverity = ctk.CTkLabel(
            baseFrameRight1,
            text="Severity:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsSeverity.place(x=10, y=390)

        scanStatsElapse = ctk.CTkLabel(
            baseFrameRight1,
            text="Elapsed Time:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsElapse.place(x=10, y=410)

        scanStatsSize = ctk.CTkLabel(
            baseFrameRight1,
            text="Size:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsSize.place(x=10, y=430)
    else:
        frameLabelRight1 = ctk.CTkLabel(
            baseFrameRight1,
            text="Results",
            font=fontFrameLabelBold,
            width=80,
            height=30,
            fg_color=frameLabelFG,
            text_color=frameLabelTextColor,
            corner_radius=4,
        )
        frameLabelRight1.place(x=0, y=10)

        unsafeImage = ctk.CTkImage(
            Image.open(__file__ + "/../../../assets/img/unsafe.png"), size=(125, 125)
        )
        unsafeImageLabel = ctk.CTkLabel(baseFrameRight1, image=unsafeImage, text="")
        unsafeImageLabel.place(x=35, y=60)

        unsafeResultsLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Alert!",
            width=100,
            text_color="#017dcc",
            font=ctk.CTkFont("Segoe UI", 34, "bold"),
        )
        unsafeResultsLabel.place(x=55, y=195)

        unsafeResultsSubLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="The file isn't Safe.",
            text_color=frameTextColorSecondary,
            font=fontFrameLabelBold,
        )
        unsafeResultsSubLabel.place(x=45, y=237)

        unsafeScanDetailsSubLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Scan Details",
            font=fontFrameLabelBold,
            width=120,
            height=30,
            fg_color="white",
            text_color=frameTextColorPrimary,
            corner_radius=4,
        )
        unsafeScanDetailsSubLabel.place(x=68, y=290)

        unsafeScanDetailsLabel = ctk.CTkLabel(
            baseFrameRight1,
            text="Info.",
            font=fontFrameLabelBold,
            width=75,
            height=30,
            fg_color=frameLabelFG,
            text_color=frameLabelTextColor,
            corner_radius=4,
        )
        unsafeScanDetailsLabel.place(x=0, y=290)

        # Safe Scan Statistics...

        scanStatsStatus = ctk.CTkLabel(
            baseFrameRight1,
            text="File Name:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsStatus.place(x=10, y=330)

        scanStatsStatus = ctk.CTkLabel(
            baseFrameRight1,
            text="Status:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsStatus.place(x=10, y=350)

        scanStatsRansom = ctk.CTkLabel(
            baseFrameRight1,
            text="Ransomware:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsRansom.place(x=10, y=370)

        scanStatsSeverity = ctk.CTkLabel(
            baseFrameRight1,
            text="Severity:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsSeverity.place(x=10, y=390)

        scanStatsElapse = ctk.CTkLabel(
            baseFrameRight1,
            text="Elapsed Time:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsElapse.place(x=10, y=410)

        scanStatsSize = ctk.CTkLabel(
            baseFrameRight1,
            text="Size:",
            font=fontFrameLabelBold,
            text_color=frameTextColorSecondary,
            height=20,
        )
        scanStatsSize.place(x=10, y=430)

    elapseEnd = time()
    print(elapseEnd-elapseStart)    


def hashGen(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


elapseStart = 0
previouslyScanned = False

def scanNowHandler():
    # Calculate elapsed Time
    global elapseStart
    elapseStart = time()

    # Destroy Previous Frame...
    if not previouslyScanned:
        pass


    if scanRadio_var.get() == 1:
        # Single File Scan
        inputPath = inputComboSelected.get()
        hashObj = {"hash": f"${hashGen(inputPath)}"}
        # hashObj = {
        #     "hash": "acd7bea8e0e6e76c5ad0498411812695ea5a9809c8e75fdb5b149d3c3b99190c"
        # }
        singleResponse = requests.post("http://localhost:3000/scan", json=hashObj)
        scanResults[inputPath] = singleResponse.json()
        renderScanResults(scanResults[inputPath])
    else:
        # Multi File Scan
        for inputPath in inputFiles:
            hashObj = {"hash": f"${hashGen(inputPath)}"}
            singleResponse = requests.post("http://localhost:3000/scan", json=hashObj)
            # Don't Update Continually, just store the results...
            scanResults[inputPath] = singleResponse.json()

        renderScanResults(scanResults[inputComboSelected.get()])    


scanNowButton = ctk.CTkButton(
    baseFrameMid1,
    fg_color=frameLabelFG,
    text="Scan",
    font=fontFrameLabelBold,
    width=90,
    height=35,
    command=scanNowHandler,
)
scanNowButton.place(x=345, y=143)

# Results Frame...

baseFrameRight1 = ctk.CTkFrame(
    baseFrameRight,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
)
baseFrameRight1.pack(side="top", expand=True, fill="both")

frameLabelRight1 = ctk.CTkLabel(
    baseFrameRight1,
    text="Results",
    font=fontFrameLabelBold,
    width=80,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
frameLabelRight1.place(x=0, y=10)

resultsImage = ctk.CTkImage(
    Image.open(__file__ + "/../../../assets/img/default.png"), size=(125, 125)
)
resultsImageLabel = ctk.CTkLabel(baseFrameRight1, image=resultsImage, text="")
resultsImageLabel.place(x=35, y=60)

resultsLabel = ctk.CTkLabel(
    baseFrameRight1,
    text="Scan",
    width=100,
    text_color="#017dcc",
    font=ctk.CTkFont("Segoe UI", 34, "bold"),
)
resultsLabel.place(x=55, y=195)

resultsSubLabel = ctk.CTkLabel(
    baseFrameRight1,
    text="Results appear here.",
    text_color=frameTextColorSecondary,
    font=fontFrameLabelBold,
)
resultsSubLabel.place(x=45, y=237)

resultsScanDetailsSubLabel = ctk.CTkLabel(
    baseFrameRight1,
    text="Server Stats",
    font=fontFrameLabelBold,
    width=120,
    height=30,
    fg_color="white",
    text_color=frameTextColorPrimary,
    corner_radius=4,
)
resultsScanDetailsSubLabel.place(x=68, y=290)

resultsScanDetailsLabel = ctk.CTkLabel(
    baseFrameRight1,
    text="Info.",
    font=fontFrameLabelBold,
    width=75,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
resultsScanDetailsLabel.place(x=0, y=290)

# Server Statistics...

serverStatsLabelStatus = ctk.CTkLabel(
    baseFrameRight1,
    text="Status:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelStatus.place(x=10, y=330)

serverStatsLabelConn = ctk.CTkLabel(
    baseFrameRight1,
    text="Connection:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelConn.place(x=10, y=350)

serverStatsLabelUptime = ctk.CTkLabel(
    baseFrameRight1,
    text="Uptime:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelUptime.place(x=10, y=370)

serverStatsLabelSamples = ctk.CTkLabel(
    baseFrameRight1,
    text="Samples:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelSamples.place(x=10, y=390)

serverStatsLabelDomain = ctk.CTkLabel(
    baseFrameRight1,
    text="Domain:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelDomain.place(x=10, y=410)

serverStatsLabelBackend = ctk.CTkLabel(
    baseFrameRight1,
    text="Backend:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelBackend.place(x=10, y=430)


# Server Stats Actual Values
serverStatsStatus = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsStatus.place(x=60, y=330)

serverStatsConn = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsConn.place(x=93, y=350)

serverStatsUptime = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsUptime.place(x=68, y=370)

serverStatsSamples = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsSamples.place(x=73, y=390)

serverStatsDomain = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsDomain.place(x=70, y=410)

serverStatsBackend = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsBackend.place(x=73, y=430)

def getServerStats():
    response = {}
    try:
        response = requests.get('http://localhost:3000/initial').json()
    except:
        response = {
            "status": "Offline",
            "connection": "Failed",
            "uptime": "Unknown",
            "samples": "Unknown",
            "domain": "Unknown",
            "backend": "Unknown"
        }
    finally:
        serverStatsStatus.configure(text=response['status'])
        serverStatsConn.configure(text=response['connection'])
        serverStatsUptime.configure(text=response['uptime'])
        serverStatsSamples.configure(text=response['samples'])
        serverStatsDomain.configure(text=response['domain'])
        serverStatsBackend.configure(text=response['backend'])

getServerStats()

app.mainloop()

# Old Code...

# app.option_add("*Font", 'SegoeUIVariable')

# app.geometry("800x500")

# app.wm_attributes('-transparentcolor','black')

# transPath = __file__ + '/../../../assets/img/transparent.png'

# # Images
# transImg = Image.open(transPath)
# resTransImg = transImg.resize((100,100))
# transBg = ImageTk.PhotoImage(resTransImg)
# transBg1 = ctk.CTkImage.

# # Frames
# baseFrameLeft1 = ctk.CTkFrame(
#     app,
#     corner_radius=12,
#     border_color="black",
#     border_width=1,
#     width=200,
#     height=205,
#
# ).grid(row=0, column=0, padx=(10, 12), pady=(10, 5))

# baseFrameLeft2 = ctk.CTkFrame(
#     app,
#     corner_radius=12,
#     border_color="black",
#     border_width=1,
#     width=200,
#     height=205,
#
# ).grid(row=1, column=0, padx=(10, 12), pady=(5, 10))

# baseFrameMid = ctk.CTkFrame(
#     app, corner_radius=16, width=400, height=430, fg_color="#242424"
# ).grid(row=0, column=1, rowspan=2)

# baseFrameRight = ctk.CTkFrame(
#     app, corner_radius=16, border_color="blue", border_width=1, width=200, height=430
# ).grid(row=0, column=2, rowspan=2, padx=(10, 12), pady=(10, 10))


# # BaseFrameLeft Content
# labelInputDetails = ctk.CTkLabel(
#     baseFrameLeft1, text="Input Details", width=90, font=fontFrameLabelBold
# )
# labelInputDetails.place(x=25, y=0)

# labelBackupOptions = ctk.CTkLabel(
#     baseFrameLeft2, text="Backup Options", width=107, font=fontFrameLabelBold
# )
# labelBackupOptions.place(x=25, y=221)

# # BaseFrameMid Content
# bfmFrameTop = ctk.CTkFrame(
#     baseFrameMid,
#     corner_radius=16,
#     border_color="blue",
#     border_width=1,
# )
# bfmFrameTop.place(side="top")
