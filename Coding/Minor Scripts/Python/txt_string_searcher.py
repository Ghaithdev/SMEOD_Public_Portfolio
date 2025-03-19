import os
import re #Imports Regex expression compatibility
from datetime import datetime
import tkinter as tk    #these modules are to do with the graphic user interface
from tkinter import ttk     #these modules are to do with the graphic user interface
from tkinter import filedialog  #these modules are to do with the graphic user interface
from tkinter import *   #these modules are to do with the graphic user interface
from datetime import datetime,timezone  #these modules allow python to read the date and time, they are important to the randomization

mainroot=tk.Tk()
mainroot.iconbitmap("Pharmaron_logo.ico")
mainroot.title("QUAL_MS reader")
correct_file_extension=".txt"
results=[]
dated_results=[]
search_string="QUAL_MS \(([0-9]+)\)"

"""This function was built to allow the interpretation of dates as they appear in filenames currently.
It was built so as to allow the dates to be used in the output although this is likely not needed"""
def date_extract (filename):
    date=re.findall("[0-9]{2}[A-Z,a-z]{3}[0-9]{2}",filename)#reads date in format 'ddMmmyy
    if date:
        date=date[0]
        return date
    date2=re.findall("[0-9]{4}\-[0-9]{2}\-[0-9]{2}",filename)
    if date2:
        date=date2[0]
        year, month, day=date.split("-")
        date=datetime.strptime(f"{year}{month}{day}","%Y%m%d")
        date=datetime.strftime(date, '%d%b%y')
        return date
      
"""This function converts the output of the 'date extract' function to be read as a date object,
allowing for more ready use of mathmatical operations on it. This was created thinking that knowing
the earliest date a solution was used on would help locate its QUAL_MS log entry were there issues with
the other inputs"""
def date_conv(date):
    try:
        day=(date[:2])
        month=date[2:5]
        year=date[5:]
        date_string=f"{day}, {month}, {year}"
        date_inp_format='%d, %b, %y'#reads dates as 'dd, Mmm, yy'
        date_out_format="%Y-%m-%d"#outputs dates as yyyy-mm-dd
        numdate=datetime.strptime(date_string, date_inp_format)
        date_out=datetime.strftime(numdate,date_out_format)
        return(date_out)
    except(ValueError, TypeError):
        tk.messagebox.showerror(title="Date Error", message="The date in the filename was in an unexpected format.\nThe expected format is ddMmmyy\n No date will be used")#displays error msg
        return

"""The following function returns a folder selected by user input"""
def get_folder():
    while True:
        directory_path=filedialog.askdirectory(initialdir="/", title='Select directory')
        if not directory_path or directory_path == "":
            tk.messagebox.showerror(title="File Error", message="No folder selected")#displays error msg
            continue
        return directory_path

"""The following function returns the names of all the files in an inputted folder"""
def get_filenames(directory_path):
    files_to_open=[]
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            fname=(os.path.join(root, name))
            files_to_open.append(fname)
    return files_to_open

"""Returns the first Qual MS number from a given line of text if it exists"""
def read_qualms(line):
    qms=re.findall(search_string,line.strip())
    if qms:
        return qms#Returns only the first qual ms number all others are ignored
    else:
        return None

"""The follwoing function, called by the 'read_file' function, returns the <text> part of a line
containing the phrase '<text> QUAL_MS(<numbers>)'"""
def get_solution_name(line):
    text=re.findall("(.*)QUAL_MS \([0-9]+\)",line)[0]
    text=text.removesuffix("\n").removeprefix("\t").strip()
    text=text.replace("\t"," ")
    text=text.replace("Â","")
    return text



"""This function reads the file & returns a tuple containing the qms number and the
accompanying text. It takes a file name as its input"""
def read_file(phile):
    file_output=[]
    with open(phile,"r")as open_file:
        for line in open_file:
            qms=read_qualms(line)
            if not qms:
                continue
            qmsno=qms[0]
            text=get_solution_name(line)
            output_tup=(qmsno,text)
            file_output.append(output_tup)
        return file_output

"""This function takes a list of items and checks if they exist in the
results list, if not it adds them to a list of unique items & returns that
list"""
def check_duplicates(inp_list):
    novel_list=[]
    for item in inp_list:
        if not item in results:
            novel_list.append(item)
    return novel_list


files_to_open=get_filenames(get_folder())
for phile in files_to_open:
    date=date_conv(date_extract(phile))
    if not str(phile).endswith(correct_file_extension):
        continue
    with open(phile,"r", encoding="utf-8")as open_file:
        outputs=read_file(phile)
        if not check_duplicates:
            continue
        for item in check_duplicates(outputs):
            results.append(item)
            dated_results.append((item[0], item[1], date))


text_frame=tk.LabelFrame(mainroot,text="Results",labelanchor="n")
text_frame.grid(row=0,column=0, columnspan=3, sticky="nesw")
read_me=Text(text_frame, width=60, height=15, font=("Calibri",16))
read_me.pack()

n=1.0
for item in sorted(dated_results):
    text=f"Qual_MS: {item[0]}\nName: {item[1]}\nFirst used on date: {item[2]}\n\n"
    read_me.insert(n,text)
    n=n+4

#This mainloop is what allows the GUI to persist if this is deleted the window will only flash on screen
mainroot.mainloop()
