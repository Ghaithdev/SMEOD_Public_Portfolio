import tkinter as tk #Tkinter is the module that allows the GUI to exist
from tkinter import ttk #Tkinter is the module that allows the GUI to exist
from tkinter import messagebox #Tkinter is the module that allows the GUI to exist
from tkinter import filedialog #Tkinter is the module that allows the GUI to exist
from tkinter import *
import re #Regex library
from os import listdir, getlogin
from datetime import datetime
from hashlib import sha256

class MainApplication(tk.Tk):
    def __init__(self, win_title, icon):
        super().__init__()
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.title(win_title)
        self.iconbitmap(icon)
        self.notebook = ttk.Notebook(self)
        self.checker_frame = CheckerFrame(self.notebook)
        self.notebook.add(self.checker_frame, text='Check')
        self.notebook.pack()

class CheckerFrame(ttk.Frame):
    csv_files={}
    txt_files={}
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.populate()

    def populate(self):
        self.parent.txt_frame=Txt_frame(self)
        self.parent.csv_frame=Csv_frame(self)

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Reset", underline=1, command=None)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        viewMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="View",underline=0, menu=viewMenu)
        viewMenu.add_command(label="Change Font", underline=1, command=None)
        viewMenu.add_command(label="Hide Menu", underline=1, command=self.hide_menu)

        settingMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Settings",underline=0, menu=settingMenu)
        settingMenu.add_command(label="Open Settings", underline=1, command=None)
        settingMenu.add_command(label="Open Advanced Settings", underline=1, command=lambda: messagebox.showerror(title="No", message="Hahaha, no"))

    def hide_menu(self):
        self.destroy()

class Txt_frame(tk.LabelFrame):
    
    def __init__(self, parent):
        super().__init__(parent, text="Txt Files", labelanchor="nw")
        self.grid(row=0, column=0, sticky="news", padx=(10,0))
        self.populate()
        self.text="Txt Files"
    
    def populate(self):
        Button(self, text="Open Folder", row=0, pady=0, command=self.open_ticket_dir)
        Button(self, text="Open single Ticket", row=1, pady=0, command=None)
        Button(self, text="↑", row=2, pady=0, command= None)
        Button(self, text="↓", row=3, pady=0, command= None)
        self.listbox_frame=Frame(self,column=1)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='multiple')
        self.box.pack(side='left', fill=Y)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)

    def open_ticket_dir(self):
        dir=filedialog.askdirectory(title="Choose ticket folder")
        files=listdir(dir)
        for file in files:
            self.open_ticket_file(f"{dir}/{file}")

    def open_ticket_file(self, filename=None):
        if not filename:
            filename=filedialog.askopenfilename(title="Choose ticket file", filetypes=(('Text files','*.txt'),('All files','*')))
        if not filename:
            messagebox.showerror(title='Invalid file choice', message='Please select a valid file')
            return False
        ticket_content=self.read_ticket(filename)
        if not self.validate_ticket(ticket_content):
            messagebox(title="Invalid ticket", message="One or more tickets are no longer valid")
            return False
        
    def read_ticket(self, ticket):
            sample_hashes=[]
            ticket_text=""
            with open(ticket, "r") as file:
                for line in file:
                    try:
                        filename=re.search(r'(^[A-Z]+-[0-9]+_\S+):', line).group(1)
                    except(AttributeError):
                        continue
                    if line.strip().startswith("Saved at: "):
                        path=line.strip().removeprefix("Saved at: ")
                    if line.strip().startswith("Sample hash: "):
                        hash=line.strip().removeprefix("Sample hash: ")
                    if path and hash:
                        sample_hashes.append((filename, path, hash))
                        path=None
                        hash=None
                    if line.strip().startswith("Ticket Hash: "):
                        ticket_hash=line.removeprefix("Ticket Hash: ")
                        break
                    ticket_text+=line
            output={'text':ticket_text, 'orig hash':ticket_hash, 'output files':sample_hashes}
            return output

    def validate_ticket(self, ticket):
        if not self.validate_files(ticket['output files']):
            return False

        gen_hash=self.create_ticket_hash(ticket['text'])
        orig_hash=ticket['orig hash']
        if gen_hash!=orig_hash:
            messagebox.showerror(title='Hash mismatch',message='The hash read from the ticket does not match the one that should have been generated for that ticket, suggesting it was somehow altered')
            return False

    def generate_filehash(self, filename):
        sample_hash=sha256()
        with open(filename, 'rb') as file:
            for line in file:
                sample_hash.update(line)
        return sample_hash.hexdigest()

    def create_ticket_hash(self, ticket):
            ticket_hash_object=sha256()
            ticket_hash_object.update(ticket.encode('utf-8'))
            ticket_hash=ticket_hash_object.hexdigest()
            return ticket_hash

    def validate_files(self, pairs):
        for item in pairs:
            file=item[0]
            read_hash=item[1]
            test_hash=self.generate_filehash(file)
            if test_hash!=read_hash:
                message=f"The generated hash for the file at {file}\n is {test_hash}\nbut the hash in the ticket is:\n{read_hash}\nThis may indicate that the file has been altered"
                return False
        return True

class Csv_frame(tk.LabelFrame):
    def __init__(self, parent ):
        super().__init__(parent)
        self.configure(text="CSV files", labelanchor="ne")
        self.grid(row=0,column=2, sticky="news", padx=(0,10))
        self.text="Final Sequence"
        self.populate()

    def populate(self):
        Button(self, text="Add Folder", row=0,column=1, pady=0, command=None)
        Button(self, text="Add CSV File", row=1,column=1, pady=0, command=None)
        Button(self, text="↑", row=2,column=1, pady=0, command=None)
        Button(self, text="↓", row=3,column=1, pady=0, command=None)
        self.listbox_frame=Frame(self,column=0)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='multiple')
        self.box.pack(side='left', fill=Y)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)

    def get_ticket():
        ticket=filedialog.askopenfilename(title="Choose ticket file", filetypes=(('Text files','*.txt'),('All files','*')))
        if not ticket:
            messagebox.showerror(title='Invalid file choice', message='Please select a valid file')
            return False
        return ticket

    def validate_ticket(ticket):
        ticket=read_ticket(ticket)
        
        if not validate_files(ticket['output files']):
            return False

        gen_hash=create_ticket_hash(ticket['text'])
        orig_hash=ticket['orig hash']
        if gen_hash!=orig_hash:
            messagebox.showerror(title='Hash mismatch',message='The hash read from the ticket does not match the one that should have been generated for that ticket, suggesting it was somehow altered')

    def generate_filehash(filename):
        sample_hash=sha256()
        with open(filename, 'rb') as file:
            for line in file:
                sample_hash.update(line)
        return sample_hash.hexdigest()

    def create_ticket_hash(ticket):
            ticket_hash_object=sha256()
            ticket_hash_object.update(ticket.encode('utf-8'))
            ticket_hash=ticket_hash_object.hexdigest()
            return ticket_hash

    def validate_files(pairs):
        for item in pairs:
            file=item[0]
            read_hash=item[1]
            test_hash=generate_filehash(file)
            if test_hash!=read_hash:
                message=f"The generated hash for the file at {file}\n is {test_hash}\nbut the hash in the ticket is:\n{read_hash}\nThis may indicate that the file has been altered"
                return False
        return True

    def read_ticket(ticket):
        sample_hashes=[]
        ticket_text=""
        with open(ticket, "r") as file:
            for line in file:
                if line.strip().startswith("Saved at: "):
                    path=line.strip().removeprefix("Saved at: ")
                if line.strip().startswith("Sample hash: "):
                    hash=line.strip().removeprefix("Sample hash: ")
                if path and hash:
                    sample_hashes.append((path, hash))
                    path=None
                    hash=None
                if line.strip().startswith("Ticket Hash: "):
                    ticket_hash=line.removeprefix("Ticket Hash: ")
                    break
                ticket_text+=line
            output={'text':ticket_text, 'orig hash':ticket_hash, 'output files':sample_hashes}

class Frame(tk.Frame):
    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=4) -> None:
        super().__init__(parent)
        self.grid(row=row,column=column,rowspan=rowspan, columnspan=columnspan)

class LabelFrame(tk.LabelFrame):
    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=1, text=None, labelanchor='n', padx=(10,0),pady=(10)) -> None:
        super().__init__(parent)
        self.configure(text=text)
        self.configure(labelanchor=labelanchor)
        self.grid(row=row,column=column,rowspan=rowspan, padx=padx, pady=pady, columnspan=columnspan)

class Button(tk.Button):
    instance_list=[]

    def __init__(self, parent, text="Button", command=None, row=0, column=0, columnspan=1,rowspan=1, padx=(10,0), pady=(10,0),sticky="nesw", width=None, state=NORMAL):
        super().__init__(parent)
        self.configure(text=text, command=command, state=state)
        self.text=text
        self.grid(row=row, column=column,rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        Button.instance_list.append(self)

class Label(tk.Label):
    instance_list=[]

    def __init__(self,parent, text="text", column=0, row=0):
        super().__init__(parent)
        self.configure(text=text)
        self.grid(row=row,column=column)
        self.text=text
        Label.instance_list.append(self)
    
    def update(self,new_text="text"):
        self.configure(text=new_text)
        self.text=new_text

class Checkbox(ttk.Checkbutton):
    instance_list=[]

    def __init__(self,parent, name, column=0, row=0, error_msg=None):
        super().__init__(parent)
        self.variable=tk.BooleanVar(self)
        self.config(variable=self.variable)
        self.grid(row=row,column=column)
        self.name=name
        if not error_msg:#default error message for checkbox
            self.error_msg=f"{name.capitalize()} checkbox was left unticked"
        else:#custom error message
            self.error_msg=error_msg
        Checkbox.instance_list.append(self)

    def checked(self):
        return self.variable.get()
    
    def set(self, boolean):
        self.variable.set(boolean)

class Combobox(ttk.Combobox):
    instance_list=[]

    def __init__(self, parent, values=None, row=0, column=0, columnspan=1, padx=(0), pady=(0),sticky="nesw"):
        super().__init__(parent)
        if values==None:
            self.values=["Default Value"]
        else:
            self.values=values
        self.configure(values=values)
        self.current(95)
        self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        Combobox.instance_list.append(self)

class Spinbox(ttk.Spinbox):
    instance_list=[]

    def __init__(self, parent, from_=1,to=12,increment=1, row=0, column=0, columnspan=1, padx=(0), pady=(0),sticky="nesw",command=None):
        super().__init__(parent)
        self.var = StringVar(self)
        self.var.set(int((from_+to)/2))
        self.configure(from_=from_, to=to, increment=increment, textvariable=self.var, command=command)
        self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        Spinbox.instance_list.append(self)

class Entry(tk.Entry):
    instance_list=[]

    def __init__(self,parent, column=0, row=0, state=NORMAL):
        super().__init__(parent)
        self.grid(row=row,column=column)
        self.configure(state=state)
        Entry.instance_list.append(self)

if __name__ == '__main__':
    app = MainApplication("Importer and Checker Ver00.01","Pharmaron_logo.ico")
    app.mainloop()
