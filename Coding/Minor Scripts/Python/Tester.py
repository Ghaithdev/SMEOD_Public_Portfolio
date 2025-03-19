import tkinter as tk #Tkinter is the module that allows the GUI to exist
from tkinter import ttk #Tkinter is the module that allows the GUI to exist
from tkinter import messagebox #Tkinter is the module that allows the GUI to exist
from tkinter import filedialog #Tkinter is the module that allows the GUI to exist
from tkinter import *


class MainApplication(tk.Tk):
    current_font=("Times New Roman", 36)

    def __init__(self, win_title):
        super().__init__()
        self.title(win_title)
        self.host_menu=HostMenu(self)

class HostMenu(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(text="Choose how to play",labelanchor="n")
        Button(self,width=16, text="Act as Host", padx=(0), pady=(0), column=0, row=0, command=None)
        Button(self,width=16, text="Play as Guest", padx=(0), pady=(0), column=0, row=1, command=None)
        self.pack()


#Below are the generic components
class Frame(tk.Frame):
    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=4) -> None:
        super().__init__(parent)
        self.grid(row=row,column=column,rowspan=rowspan, columnspan=columnspan)

class LabelFrame(tk.LabelFrame):
    instance_list=[]

    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=1, text=None, labelanchor='n', padx=(10,0),pady=(10)) -> None:
        super().__init__(parent)
        self.configure(text=text)
        self.configure(labelanchor=labelanchor)
        self.configure(font=MainApplication.current_font)
        self.grid(row=row,column=column,rowspan=rowspan, padx=padx, pady=pady, columnspan=columnspan)
        LabelFrame.instance_list.append(self)

class Button(tk.Button):
    instance_list=[]

    def __init__(self, parent, text="Button", command=None, row=0, column=0, columnspan=1,rowspan=1, padx=(10,0), pady=(10,0),sticky="nesw", width=None, state=NORMAL):
        super().__init__(parent)
        self.configure(text=text, command=command, state=state,font=MainApplication.current_font)
        self.text=text
        self.grid(row=row, column=column,rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        Button.instance_list.append(self)

class Label(tk.Label):
    instance_list=[]

    def __init__(self,parent, text="text", column=0, row=0):
        super().__init__(parent)
        self.configure(text=text,font=MainApplication.current_font)
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

#This is a custom component that simply combines the checkbox and label and places them together
class Labelled_Checkbox():

    def __init__(self, parent, text="text", column=0, row=0):
        Label(parent,text=text, column=column,row=row)
        self.checkbox=Checkbox(parent, name=text, column=(column+1), row=row)      

if __name__ == '__main__':
    app = MainApplication("Boxing day bonanza")
    app.mainloop()