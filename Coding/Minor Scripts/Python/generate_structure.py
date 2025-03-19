import os
from datetime import datetime
import tkinter as tk    #these modules are to do with the graphic user interface
from tkinter import ttk     #these modules are to do with the graphic user interface
from tkinter import filedialog  #these modules are to do with the graphic user interface
from tkinter import *   #these modules are to do with the graphic user interface


mainroot=tk.Tk()
mainroot.iconbitmap("Pharmaron_logo.ico")
parent_path=filedialog.askdirectory(initialdir=r"Y:\R_Sponsor", title='Select directory')
subdirs=["Drafts","Experimental","Experimental/Sample Prep","Labels","Structres","Report","Top Count","Updates"]
print(f"the selected directory was: {parent_path}")
for directory in subdirs:
    destination=os.path.join(parent_path, directory)
    print(destination)
    os.mkdir(destination)
print("done")