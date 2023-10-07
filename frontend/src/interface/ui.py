import customtkinter as ctk
from customtkinter import filedialog
from tkinter import IntVar

import hashlib
from pathlib import Path
from datetime import datetime
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
    app, corner_radius=12, border_color="blue", border_width=1, fg_color=baseFrameFG
)
baseFrameRight.pack(side="left", fill="both", pady=baseFramePadY, padx=baseFramePadX)

# Child Frames of baseFrameLeft
baseFrameLeft1 = ctk.CTkFrame(
    baseFrameLeft,
    corner_radius=12,
    fg_color=baseFrameChildFG,
    border_color=baseFrameChildBC,
    border_width=1,
    height=225
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
    detailValueCreation.configure(text=datetime.strftime(datetime.fromtimestamp(file.stat().st_ctime),"%d-%m-%Y, %H:%M"))
    detailValueSize.configure(text=file.stat().st_size)
    detailValueSHA.configure(text=hashlib.sha256(file.read_bytes()).hexdigest())


def getPrevFileStats():
    currentFileIndex = inputFiles.index(inputComboSelected.get())
    if currentFileIndex == 0:
        currentFileIndex = len(inputFiles)-1
    else:
        currentFileIndex -= 1
        
    inputComboSelected.set(inputFiles[currentFileIndex])    
    getFileStats(inputFiles[currentFileIndex])


def getNextFileStats():
    currentFileIndex = inputFiles.index(inputComboSelected.get())
    if currentFileIndex == len(inputFiles)-1:
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
    font=ctk.CTkFont('Arial',15,'bold'),
    command=getPrevFileStats
)
filePrevButton.place(x=10,y=185)

fileNextButton = ctk.CTkButton(
    baseFrameLeft1,
    corner_radius=4,
    text=">",
    width=35,
    height=30,
    fg_color=frameLabelFG,
    anchor="center",
    font=ctk.CTkFont('Arial',15,'bold'),
    command=getNextFileStats
)
fileNextButton.place(x=155,y=185)




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
    command=comboBoxHandler
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
            frameLabelLeft2.configure(text='Selected File.')
            fileNextButton.configure(state='disabled')
            filePrevButton.configure(state='disabled')
        else:
            fileNextButton.configure(state='normal')
            filePrevButton.configure(state='normal')   

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
    padx=10
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

def hashGen(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


responses = []
def scanNowHandler():
    if(scanRadio_var.get() == 1):
        # Single File Scan
        hashObj = {
            'hash': f'${hashGen(inputComboSelected.get())}'
        }
        singleResponse = requests.post('http://localhost:3000/scan',json=hashObj)
        print(singleResponse.json())
    else:
        # Multi File Scan
        for entry in inputFiles:
            hashGen(entry)

scanNowButton = ctk.CTkButton(
    baseFrameMid1,
    fg_color=frameLabelFG,
    text="Scan",
    font=fontFrameLabelBold,
    width=90,
    height=35,
    command=scanNowHandler
)
scanNowButton.place(x=345, y=143)

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
