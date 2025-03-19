import os
import datetime
from tkinter import filedialog

directory=filedialog.askdirectory(title="Choose directory")
files=os.listdir(directory)
for file in files:
    path = f"{directory}/{file}"
    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)
    c_datestamp = datetime.datetime.fromtimestamp(ti_c)
    m_datestamp = datetime.datetime.fromtimestamp(ti_m)
    print(f"File: {path}\nCreated: {c_datestamp}\nModified: {m_datestamp}\n{ti_c}\n{ti_m}\n{abs(ti_m-ti_c)}\n\n")

