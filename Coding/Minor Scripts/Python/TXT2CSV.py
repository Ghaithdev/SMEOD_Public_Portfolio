from tkinter import filedialog
from os import listdir

def open_file(txt):
    with open(txt, 'r') as file:
        read_line(file)

def read_line(file):
    for line in file:
        text.append(line)

def convert(file, folder):
    for line in text:
        new_text=f"{69}, {line}\n"
        output.append(new_text)
    destination=filedialog.asksaveasfilename(initialdir=folder, initialfile=f"{file}.csv",filetypes = (("CSV files","*.CSV"),("All files","*.*")))
    with open(destination, "w+") as destination_file:
            destination_file.truncate()
    with open(destination, "a+") as destination_file:
            for item in output:    
                destination_file.write(f"{item}\n")
    

text=[]
output=[]
k=69

txt_folder=filedialog.askdirectory()
txt_files=listdir(txt_folder)
for file in txt_files:
    full_fname=f"{txt_folder}/{file}"
    open_file(full_fname)
    convert(file,txt_folder)
    



