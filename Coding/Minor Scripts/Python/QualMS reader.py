from tkinter import filedialog
import os

folder_choice=filedialog.askdirectory(title="Open a folder or something, idk")
print(f"Chosen folder: {folder_choice}")
files=os.listdir(folder_choice)
print(files)
for file in files:
    print(file)