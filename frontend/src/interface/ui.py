import customtkinter as ctk
from customtkinter import filedialog
from tkinter import IntVar
from PIL import Image

import hashlib
from pathlib import Path
from datetime import datetime
from time import time, sleep
import requests

# Domain Name for Web Requests
domainName = "https://ransom-detect.cyclic.cloud/"
# domainName = "http://localhost:3000/"


# Frame Foreground Colors
baseFrameFG = "#dfdfdf"
baseFrameChildFG = "#ebebeb"
baseFrameChildBC = "#b7b7b7"
frameLabelFG = "#0078d4"
frameLabelTextColor = "#dce4ee"
frameTextColorPrimary = "grey"
frameTextColorSecondary = "#6f6f6f"


# Setting Appearance Modes
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# Initializing App
app = ctk.CTk(fg_color=baseFrameFG)


# Window Geometry & Title
app.title("Ransomware Detection")
app.resizable(False, False)
app.geometry("900x500")


# Custom Fonts
fontFrameLabelBold = ctk.CTkFont("Segoe UI", 13, "bold")
fontFrameLabel = ctk.CTkFont("Segoe UI", 13)
baseFramePadY = (10, 10)
baseFramePadX = (10, 10)


# Base Frames
baseFrameLeft = ctk.CTkFrame(app, corner_radius=12, fg_color=baseFrameFG)
baseFrameLeft.pack(side="left", fill="both", pady=baseFramePadY, padx=baseFramePadX)

baseFrameMid = ctk.CTkFrame(app, width=400, fg_color=baseFrameFG)
baseFrameMid.pack(side="left", fill="both", expand=True, pady=baseFramePadY)

baseFrameRight = ctk.CTkFrame(app, corner_radius=12, fg_color=baseFrameFG)
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
baseFrameMid1.pack(side="top", fill="x", pady=(0, 5))

baseFrameMid2 = ctk.CTkFrame(
    baseFrameMid,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=130,
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
    state="disabled",
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
    state="disabled",
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
    renderActiveDisplay("scan")
    resultNextButton.configure(state="disabled")

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


def scanRadioHandler():
    if scanRadio_var.get() == 2:
        resultNextButton.place(x=160, y=10)
    else:
        resultNextButton.place_forget()


# Scan Option Radio Buttons...
scanRadio_var = IntVar(value=1)
scanRadioSingle = ctk.CTkRadioButton(
    baseFrameMid1,
    text="Single File Scan",
    variable=scanRadio_var,
    value=1,
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    command=scanRadioHandler,
)
scanRadioSingle.place(x=20, y=148)

scanRadioMultiple = ctk.CTkRadioButton(
    baseFrameMid1,
    text="Multiple File Scan",
    variable=scanRadio_var,
    value=2,
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    command=scanRadioHandler,
)
scanRadioMultiple.place(x=170, y=148)

# Progress Bar Rendering...
frameLabelMid22 = ctk.CTkLabel(
    baseFrameMid2,
    text="Awaiting file input.",
    font=fontFrameLabelBold,
    width=150,
    height=30,
    fg_color="white",
    anchor='w',
    text_color=frameTextColorPrimary,
    corner_radius=8,
    padx=10,
)
frameLabelMid22.place(x=70, y=12)

frameLabelMid21 = ctk.CTkLabel(
    baseFrameMid2,
    text="Status",
    font=fontFrameLabelBold,
    width=75,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
frameLabelMid21.place(x=0, y=12)

statusProgressDesc = ctk.CTkLabel(
    baseFrameMid2,
    text="Idle",
    width=200,
    anchor='w',
    text_color=frameTextColorSecondary,
    font=fontFrameLabelBold,
)
statusProgressDesc.place(x=15, y=47)

statusProgressBar = ctk.CTkProgressBar(
    baseFrameMid2,
    width=400,
    height=30,
    orientation="horizontal",
    fg_color="white",
    corner_radius=1,
    mode="determinate",
    progress_color="#007edf",
    border_color="grey",
    border_width=1,
)
statusProgressBar.set(0)
statusProgressBar.place(x=15, y=77)

# Backup Option Rendering...
frameLabelMid32 = ctk.CTkLabel(
    baseFrameMid3,
    text="Choose Backup Options.",
    font=fontFrameLabelBold,
    height=30,
    fg_color="white",
    anchor='w',
    text_color=frameTextColorPrimary,
    corner_radius=8,
    padx=10,
)
frameLabelMid32.place(x=70, y=12)

frameLabelMid31 = ctk.CTkLabel(
    baseFrameMid3,
    text="Backup",
    font=fontFrameLabelBold,
    width=75,
    height=30,
    fg_color=frameLabelFG,
    text_color=frameLabelTextColor,
    corner_radius=4,
)
frameLabelMid31.place(x=0, y=12)

# Results Rendering...
scanResults = {}
elapseStart = 0
currentActiveDisplay = None


def renderActiveDisplay(display, results=None):
    global elapseEnd
    global currentActiveDisplay
    if display == "scan":
        if currentActiveDisplay == "scan":
            updateServerStats()
            return
        currentActiveDisplay = "scan"
        resultsImage = ctk.CTkImage(
            Image.open(__file__ + "/../../../assets/img/default.png"),
            size=(125, 125),
        )
        resultsImageLabel.configure(image=resultsImage, text="")
        resultsLabel.configure(text="Scan", text_color="#017dcc")
        resultsLabel.pack_forget()
        resultsLabel.place(x=55, y=195)
        resultsSubLabel.configure(text="Results appear here.")
        resultsScanDetailsSubLabel.configure(text="Server Stats.")
        serverStatsLabelStatus.configure(text="Status:")
        serverStatsLabelConn.configure(text="Connection:")
        serverStatsLabelUptime.configure(text="Uptime:")
        serverStatsLabelSamples.configure(text="Samples:")
        serverStatsLabelDomain.configure(text="Domain:")
        serverStatsLabelBackend.configure(text="Backend:")
        updateServerStats()
    elif display == "results":
        currentActiveDisplay = "results"

        resultsScanDetailsSubLabel.configure(text="Scan Details.")
        serverStatsLabelStatus.configure(text="Name:")
        serverStatsLabelConn.configure(text="Status:")
        serverStatsLabelUptime.configure(text="Ransomware:")
        serverStatsLabelSamples.configure(text="Severity:")
        serverStatsLabelDomain.configure(text="Elapsed Time:")
        serverStatsLabelBackend.configure(text="Size:")

        serverStatsStatus.place_forget()
        serverStatsConn.place_forget()
        serverStatsUptime.place_forget()
        serverStatsSamples.place_forget()
        serverStatsDomain.place_forget()
        serverStatsBackend.place_forget()

        if results["isSafe"]:
            resultsImage = ctk.CTkImage(
                Image.open(__file__ + "/../../../assets/img/safe.png"),
                size=(125, 125),
            )
            resultsImageLabel.configure(image=resultsImage, text="")
            resultsLabel.configure(text="Safe", text_color="#017dcc")
            resultsLabel.pack_forget()
            resultsLabel.place(x=55, y=195)
            resultsSubLabel.configure(text="The file looks Safe.")
            

            elapseEnd = time()
            elapse = elapseEnd - elapseStart

            serverStatsStatus.configure(text=results["fileName"])
            serverStatsConn.configure(text="Safe")
            serverStatsUptime.configure(text="No")
            serverStatsSamples.configure(text="None")
            serverStatsDomain.configure(text=str(round(elapse, 3)) + "s")
            serverStatsBackend.configure(text=str(results["fileSize"]) + " bytes")

        else:
            resultsImage = ctk.CTkImage(
                Image.open(__file__ + "/../../../assets/img/unsafe.png"),
                size=(125, 125),
            )
            resultsImageLabel.configure(image=resultsImage, text="")
            resultsLabel.configure(text="Alert", text_color="#ea510a")
            resultsLabel.pack_forget()
            resultsLabel.place(x=52, y=195)
            resultsSubLabel.configure(text="The file isn't Safe.")

            serverStatsStatus.configure(text=results["fileName"])
            serverStatsConn.configure(text="Malicious")
            serverStatsUptime.configure(text="Yes")
            elapseEnd = time()
            elapse = elapseEnd - elapseStart
            severity = "Medium" if results["size"] < 20000 else "High"
            serverStatsSamples.configure(text=severity)
            serverStatsDomain.configure(text=str(round(elapse, 3)) + "s")
            serverStatsBackend.configure(text=str(results["fileSize"]) + " bytes")

        serverStatsStatus.place(x=56, y=330)
        serverStatsConn.place(x=56, y=350)
        serverStatsUptime.place(x=96, y=370)
        serverStatsSamples.place(x=68, y=390)
        serverStatsBackend.place(x=42, y=410)
        serverStatsDomain.place(x=100, y=430)


def delay(seconds):
    app.update_idletasks()
    sleep(seconds)


progressSteps = 20
progressStepDelay = 0.015


# Computationally Expensive...
def setProgress(value, status=None, label=None):
    if label != None:
        # frameLabelMid22.configure(text="")
        # delay(0.001)
        frameLabelMid22.configure(
            text=label,
            width=150,
            height=30,
            anchor='w'
        )

    if status != None:
        statusProgressDesc.configure(
            text=status,
            width=200,
            anchor='w'
        )

    # Incrementing in 50 steps to get a animation effect...
    incrementValue = (value - statusProgressBar.get()) / progressSteps
    for i in range(progressSteps):
        currentValue = statusProgressBar.get()
        statusProgressBar.set(value=currentValue + incrementValue)
        delay(progressStepDelay)


def scanNowHandler():
    if len(inputFiles) == 0:
        return

    # Calculate elapsed Time
    global elapseStart
    elapseStart = time()

    setProgress(0.2, "Starting Scan..", "Processing..")
    if scanRadio_var.get() == 1:
        # Single File Scan
        inputPath = inputComboSelected.get()
        fileSample = Path(inputPath)
        hashObj = {
            "filename": f"{fileSample.name}",
            "size": fileSample.stat().st_size,
            "hash": f"{hashlib.sha256(fileSample.read_bytes()).hexdigest()}",
        }
        setProgress(0.4, "Scanning File..")
        # hashObj = {
        #     "filename": f'{fileSample.name}',
        #     "size": fileSample.stat().st_size,
        #     "hash": "acd7bea8e0e6e76c5ad0498411812695ea5a9809c8e75fdb5b149d3c3b99190c"
        # }
        singleResponse = requests.post(domainName + "scan", json=hashObj)
        scanResults[inputPath] = singleResponse.json()
        setProgress(0.8, "Rendering Results..")
        renderActiveDisplay("results", scanResults[inputPath])
        setProgress(1, "Done.", "Complete")
    else:
        # Multi File Scan
        if len(inputFiles) == 1:
            scanRadio_var.set(1)
            scanNowHandler()
            scanRadioHandler()
            return

        alertingResults = False
        alertCount = 0

        setProgress(0.4, "Scanning Multiple Files...")
        for inputPath in inputFiles:
            fileSample = Path(inputPath)
            hashObj = {
                "filename": f"{fileSample.name}",
                "size": fileSample.stat().st_size,
                "hash": f"{hashlib.sha256(fileSample.read_bytes()).hexdigest()}",
            }
            singleResponse = requests.post(domainName + "scan", json=hashObj)
            # Don't Update Continually, just store the results...
            scanResults[inputPath] = singleResponse.json()
            if scanResults[inputPath]["isSafe"] == False:
                alertingResults = True
                alertCount += 1

        setProgress(0.8, "Rendering Results..")
        renderActiveDisplay("results", scanResults[inputComboSelected.get()])
        setProgress(1, "Done.", "Complete.")

        if alertingResults:
            resultNextButton.configure(
                state="normal", fg_color="#ea510a", text=str(alertCount)
            )
        else:
            resultNextButton.configure(state="normal")

    delay(3)
    statusProgressBar.set(0)
    statusProgressDesc.configure(text="Idle")
    frameLabelMid22.configure(text="Awaiting file input.")


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


def getNextResult():
    currentFileIndex = inputFiles.index(inputComboSelected.get())
    if currentFileIndex == len(inputFiles) - 1:
        currentFileIndex = 0
    else:
        currentFileIndex += 1

    inputComboSelected.set(inputFiles[currentFileIndex])
    getFileStats(inputFiles[currentFileIndex])
    renderActiveDisplay("results", scanResults[inputFiles[currentFileIndex]])
    return


# Next Button for Multi Results...
resultNextButton = ctk.CTkButton(
    baseFrameRight1,
    corner_radius=4,
    text=">",
    width=35,
    height=30,
    fg_color=frameLabelFG,
    anchor="center",
    state="disabled",
    font=ctk.CTkFont("Arial", 15, "bold"),
    command=getNextResult,
)

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
serverStatsLabelDomain.place(x=10, y=430)

serverStatsLabelBackend = ctk.CTkLabel(
    baseFrameRight1,
    text="Backend:",
    font=fontFrameLabelBold,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsLabelBackend.place(x=10, y=410)


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
serverStatsDomain.place(x=12, y=450)

serverStatsBackend = ctk.CTkLabel(
    baseFrameRight1,
    text="Pending..",
    font=fontFrameLabel,
    text_color=frameTextColorSecondary,
    height=20,
)
serverStatsBackend.place(x=73, y=410)


def updateServerStats():
    response = {}
    try:
        response = requests.get(domainName + "initial").json()
    except:
        response = {
            "status": "Offline",
            "connection": "Failed",
            "uptime": "Unknown",
            "samples": "Unknown",
            "domain": "Unknown",
            "backend": "Unknown",
        }
    finally:
        serverStatsStatus.place_forget()
        serverStatsConn.place_forget()
        serverStatsUptime.place_forget()
        serverStatsSamples.place_forget()
        serverStatsDomain.place_forget()
        serverStatsBackend.place_forget()
        app.update_idletasks()
        
        serverStatsStatus.configure(text=response["status"])
        serverStatsConn.configure(text=response["connection"])
        serverStatsUptime.configure(text=response["uptime"])
        serverStatsSamples.configure(text=response["samples"])
        serverStatsDomain.configure(text=response["domain"])
        serverStatsBackend.configure(text=response["backend"])

        serverStatsStatus.place(x=60, y=330)
        serverStatsConn.place(x=93, y=350)
        serverStatsUptime.place(x=68, y=370)
        serverStatsSamples.place(x=73, y=390)
        serverStatsBackend.place(x=73, y=410)
        serverStatsDomain.place(x=10, y=449)


renderActiveDisplay("scan")

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
