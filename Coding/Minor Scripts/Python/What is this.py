import tkinter as tk
from tkinter import *
import sqlite3 as sql
from tkinter import filedialog, messagebox, simpledialog, ttk
import os
import re #Regex library
import os #Module that allows reading all files in folder, reading current user, and reads the modification date for files
import weakref
from pathlib import Path

class Database():

    def __init__(self, path=None):
        if not path:
            path=self.get_filepath()
        if not path:
            quit()
        self.path=path
        self.connection=sql.connect(path)
        self.cursor=self.connection.cursor()

    def get_filepath(self):
        path=filedialog.askopenfilename(title="Choose database")
        if not path or not os.path.isfile(path):
            retry=messagebox.askretrycancel(title="No file selected", message="User did not select valid")
            if retry:
                self.get_filepath
            else:
                return False
        return path
    



global image_tk


class MainApplication(tk.Tk):
    confirmed_images={"Pixelate Logo.jpg":{"Path":f"{Path(__file__).parent.resolve()}/Pixelate Logo.jpg","Percentages":[100,50,25]}}
    source=None
    destination=None
    current_font=("Times New Roman", 12)
    percentages=[100]
    files=["Pixelate Logo.jpg"]

    def __init__(self, win_title):
        super().__init__()
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.title(win_title)
        self.notebook = ttk.Notebook(self)
        self.notebook.parent=self
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_selected)   
        self.source_frame = SourceTab(self.notebook)
        self.create_frame = CreateTab(self.notebook)
        self.manual_frame = ManualTab(self.notebook)
        self.auto_frame = AutoTab(self.notebook)
        self.play_frame = PlayTab(self.notebook)
        self.notebook.add(self.source_frame, text='Source')
        self.notebook.add(self.create_frame, text='Create')
        self.notebook.add(self.manual_frame, text='Manual')
        self.notebook.add(self.auto_frame, text='Auto')
        self.notebook.add(self.play_frame, text='Play')
        self.notebook.pack()

    def toggle_frame(self, frame, state):
        frames=["Source","Create","Manual","Auto"]
        for i in range(len(frames)):
            if frames[i]==frame:
                index=i
        self.notebook.tab(index, state=state)

    def on_tab_selected(self, event):
        selected_tab=event.widget.select()
        tab_text=event.widget.tab(selected_tab, "text")
        if tab_text=="Manual":
            self.manual_frame.update()
        elif tab_text=="Auto":
            self.auto_frame.update()
        self.percentages.sort()

    def font_window(self):
        self.font_window=Font_window(self,'Choose Font')

    def change_font(font):
        for instance in LabelFrame.instance_list:
            try:
                instance.configure(font=font)
            except(TclError):
                continue
        for instance in Button.instance_list:
            try:
                instance.configure(font=font)
            except(TclError):
                continue
        for instance in Label.instance_list:
            try:
                instance.configure(font=font)
            except(TclError):
                continue
        for instance in Entry.instance_list:
            try:
                instance.configure(font=font)
            except(TclError):
                continue
        SourceTab.change_font(font)
        CreateTab.change_font(font)
    
    def open_single_file():
        full_fname=filedialog.askopenfilename(title='Select a file',initialdir=(os.path.dirname(__file__)), filetypes=(("All files","*.*"),("ASCII files","*min.*"),("Text files","*.txt")))
        if not full_fname:
            selection=messagebox.askretrycancel(title="No file selected", message="No file was selected, would you like to try again?")
            if selection:
                MainApplication.open_single_file()
            else:
                return False
        return full_fname
    
    def open_directory():
        messagebox.showwarning(title="Select a folder", message="Please select the folder for the function chosen")
        directory=filedialog.askdirectory(title='Select a file',initialdir=(os.path.dirname(__file__)))
        if not directory:
            selection=messagebox.askretrycancel(title="No file selected", message="No file was selected, would you like to try again?")
            if selection:
                MainApplication.open_directory()
            else:
                return False
        return directory
    
    def get_short_fname(full_fname):
        try:
            short_fname=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', full_fname).group(1)
            return short_fname
        except(AttributeError):
            return False

    
class Font_window(tk.Toplevel):

    fonts=["Arial","Helvetica","Times","Times New Roman", "Courier", "Wingdings"]
    font_sizes=[8,9,10,12,14,16,18,20,24,30,36,48,72,100]

    def __init__(self,parent,top_level,):
        super().__init__(parent)
        self.parent=parent
        self.top_level = top_level
        self.populate()
        SourceTab.change_font(MainApplication.current_font)
        self.transient(parent) # set to be on top of the main window
        self.grab_set() # hijack all commands from the master (clicks on the main window are ignored)
        parent.wait_window(self) # pause anything on the main window until this one closes
    
    def populate(self):
        self.font_listbox_frame=LabelFrame(self, rowspan=1, text="Font")
        self.font_box=tk.Listbox(self.font_listbox_frame, height=12, width=15, selectmode='single', exportselection=False)
        self.font_box.pack(side='left', fill=Y)
        self.font_box_scrollbar=tk.Scrollbar(self.font_listbox_frame, orient=VERTICAL)
        self.font_box_scrollbar.config(command=self.font_box.yview)
        self.font_box_scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox_fill(self.font_box,sorted(self.fonts))
        

        self.size_listbox_frame=LabelFrame(self, column=1, rowspan=1, text="Size")
        self.size_box=tk.Listbox(self.size_listbox_frame, height=12, width=15, selectmode='single', exportselection=False)
        self.size_box.pack(side='left', fill=Y)
        self.size_box_scrollbar=tk.Scrollbar(self.size_listbox_frame, orient=VERTICAL)
        self.size_box_scrollbar.config(command=self.size_box.yview)
        self.size_box_scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox_fill(self.size_box,self.font_sizes)

        font_button_frame=Frame(self,row=1,columnspan=2)
        self.preview_button=Button(font_button_frame,row=0, width=40,padx=(0),text="Preview",pady=(0), command=self.preview)
        self.submit_button=Button(font_button_frame,row=1, width=40,padx=(0),text="Submit",pady=(0), command=self.submit)
        self.cancel_button=Button(font_button_frame,row=2, width=40,padx=(0),text="Cancel",pady=(0), command=self.destroy)

    def listbox_fill(self,listbox, list):
        for item in list:
            listbox.insert(END,item)

    def preview(self):
        try:
            new_font_type=self.read_listbox(self.font_box)
            new_font_size=self.read_listbox(self.size_box)
            new_font=(new_font_type,new_font_size)
            self.preview_button.configure(font=new_font)
            self.submit_button.configure(font=new_font)
            self.cancel_button.configure(font=new_font)
            return new_font
        except(TclError):
            return MainApplication.current_font
    
    def read_listbox(self, listbox):
        selection=listbox.get(ANCHOR)
        return selection
    
    def submit(self):
        new_font=self.preview()
        MainApplication.current_font=(new_font)
        MainApplication.change_font(MainApplication.current_font)

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Reset", underline=1, command=self.quit)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        viewMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="View",underline=0, menu=viewMenu)
        viewMenu.add_command(label="Change Font", underline=1, command=self.parent.font_window)
        viewMenu.add_command(label="Hide Menu", underline=1, command=self.hide_menu)


    def hide_menu(self):
        self.destroy()

class SourceTab(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.populate()
        self.parent=parent
        
    def populate(self):
        self.source_entry=CustomEntry(self,column=1,row=0,sticky="news", padx=10,pady=10, placeholder="Choose Source Folder")
        self.destination_entry=CustomEntry(self,column=1,row=1,sticky="news", padx=10,pady=10, placeholder="Choose Destination Folder")
        self.source_but=Button(self, text="Browse", row=0,column=2, pady=0, padx=(0), command=self.get_source)
        self.dest_but=Button(self, text="Browse", row=1,column=2, pady=0, padx=(0), command=self.get_dest)
        self.source_sub_but=Button(self, text="Submit", row=0,column=3, pady=0, padx=(0), command=self.confirm_source)
        self.dest_sub_but=Button(self, text="Submit", row=1,column=3, pady=0, padx=(0), command=self.confirm_dest)

    def get_source(self):
        messagebox.showwarning(title="Selcting source folder", message="The selected folder must only contain images")
        source=MainApplication.open_directory()
        if not source:
            return False
        self.source_entry.set_text(source)

    def get_dest(self):
        destination=MainApplication.open_directory()
        if not destination:
            return False
        self.destination_entry.set_text(destination)

    def confirm_source(self):
        try:
            text=self.source_entry.get_text()
            if not text or text == "":
                raise FileNotFoundError
            if not os.path.isdir(text):
                raise FileNotFoundError
        except(FileNotFoundError):
            messagebox.showerror(title="No folder selected",message="A valid folder must be selected")
            return False
        else:
            self.source_entry.disable()
            self.source_but.disable()
            self.source_sub_but.disable()
            MainApplication.source=text
            if MainApplication.destination:
                self.parent.parent.toggle_frame("Create","normal")
            MainApplication.open_image_folder(MainApplication.source)

    def confirm_dest(self):
        try:
            text=self.destination_entry.get_text()
            if not text or text == "":
                raise FileNotFoundError
            if not os.path.isdir(text):
                raise FileNotFoundError
        except(FileNotFoundError):
            messagebox.showerror(Title="No folder selected",message="A valid folder must be selected")
            return False
        else:
            self.destination_entry.disable()
            self.dest_but.disable()
            self.dest_sub_but.disable()
            MainApplication.destination=text
            if MainApplication.source:
                self.parent.parent.toggle_frame("Create","normal")
          
class CreateTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.populate()

    def populate(self):
        Label(self,text="Percentage of\noriginal pixels:", column=0, row=0, sticky='n',pady=0)
        self.percent_entry=Spinbox(self,from_=0.0, to=100.0, increment=5,pady=0,padx=(0,5),sticky="news",row=0,column=1)
        self.add_but=Button(self, text="Add", column=2,row=0, pady=0, command=self.add_percentage)
        self.del_but=Button(self, text="Delete", column=2,row=1, pady=0, command=self.delete_item)
        self.reset_but=Button(self, text="Reset", column=2,row=2, pady=0, command=self.clear_listbox)
        self.confirm_but=Button(self, text="Confirm", column=2,row=3, pady=0, command=self.confirm_percentages)
        self.listbox_frame=Frame(self,row=1,column=1, rowspan=3, pady=0)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='multiple')
        self.box.pack(side='left', fill=Y)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)
        self.percent_entry.bind("<Return>", self.on_enter)

    def on_enter(self, *args):
        self.add_percentage()

    def validate_percentage(self):
        text=self.percent_entry.get()
        try:
            percent=float(text)
            if percent>=100 or percent<=0:
                messagebox.showerror(title="Bad input",message="Values must be between 0 and 100 exclusive")
                raise ValueError
            return True
        except(ValueError):
            messagebox.showerror(title="Bad input",message="Input must be a number between 0 and 100 exclusive")
            return False

    def add_percentage(self):
        if not self.validate_percentage():
            return False
        value=float(self.percent_entry.get())
        self.display_to_listbox(value)
        self.percent_entry.set_value("")

    def display_to_listbox(self, data):
        self.box.insert(END, data)
    
    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for item in (selection):
            selected_items.append(self.box.get(item))
        return selected_items
    
    def delete_item(self):
        selection=self.box.curselection()
        for plate in reversed(selection):
            self.box.delete(plate)

    def clear_listbox(self):
        self.box.selection_set(0,"end")
        self.delete_item()
    
    def confirm_percentages(self):
        self.box.selection_set(0,"end")
        selection=self.read_selection()
        if not selection:
            messagebox.showerror(title="No Values entered",message="Please enter at least one valid percentage")
            return False
        for item in selection:
            if item not in MainApplication.percentages:
                MainApplication.percentages.append(float(item))
        print(*MainApplication.percentages)
        self.parent.parent.toggle_frame("Manual","normal")
        self.percent_entry.disable()
        self.add_but.disable()
        self.del_but.disable()
        self.reset_but.disable()
        self.confirm_but.disable()

class ManualTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.populate()

    def populate(self):
        Label(self,text="Image:", column=0, row=0)
        self.picture_select=Combobox(self,pady=5,padx=(0),sticky="news",row=0,column=1)
        self.left_button=Button(self, text="←", column=0,row=1, padx=0, pady=0, command=self.prev_image)
        self.image_canvas=Canvas(self,row=1,column=1)
        self.right_button=Button(self, width=5, text="→", column=2,row=1, padx=0, pady=0, command=self.next_image)
        self.percent_label=Label(self, column=1, row=2, text="Image name")
        Button(self, text="Load", column=0,row=3,columnspan=3, pady=0, command=self.activate_thumbnails)
        self.confirm_button=Button(self, text="Confirm", column=0,row=4,columnspan=3, pady=0, command=self.confirm_image)
        self.left_button.disable()
        self.right_button.disable()
        self.confirm_button.disable()

    def activate_thumbnails(self):
        self.index=0
        self.load_image()
        self.toggle_buttons()

    def toggle_buttons(self):
        image=self.picture_select.get_value()
        confirmed_percentages=MainApplication.confirmed_images[image]["Percentages"]
        if self.index==0:
            self.left_button.disable()
        else:
            self.left_button.enable()
        if self.index==len(MainApplication.percentages)-1:
            self.right_button.disable()
        else:
            self.right_button.enable()  
        if self.convert_index() in confirmed_percentages:
            self.confirm_button.disable()
        else:
            self.confirm_button.enable()
        
    def get_image_name(self):
        image=self.picture_select.get_value()
        percentage=self.convert_index()
        image_name=MainApplication.generate_image_name(image, percentage)[0]
        return image_name

    def convert_index(self):
        return float(MainApplication.percentages[self.index])

    def update(self):
        self.picture_select.configure(values=MainApplication.files)

    def load_image(self):
        global image_tk
        image=self.picture_select.get_value()
        image_path=MainApplication.confirmed_images[image]["Path"]
        new_name=self.get_image_name()
        percentage=self.convert_index()
        self.percent_label.set_text(new_name)
        self.toggle_buttons()
        image=MainApplication.generate_image(image_path,percentage).resize((400,300))
        image_tk=ImageTk.PhotoImage(image)
        self.image_canvas.create_image(0,0,image=image_tk, anchor="nw")

    def next_image(self):
        self.index+=1
        self.load_image()

    def prev_image(self):
        self.index-=1
        self.load_image()

    def confirm_image(self):
        image=self.picture_select.get_value()
        percentage=self.convert_index()        
        MainApplication.confirmed_images[image]["Percentages"].append(percentage)
        self.toggle_buttons()

class AutoTab(ttk.Frame):
    
    samples=[]
    psn_list=[]
    sample_data={}
    used_files=[]
    plate_listbox_labels=[]
    labelled_plates={}

    def __init__(self, parent):
        super().__init__(parent)
        self.all_percents_frame=LabelFrame(self, text="All Percentages", labelanchor="nw", row=0, column=3, sticky="news", padx=(0,10),pady=(10))
        self.confirmed_percents_frame=LabelFrame(self,row=0,column=1, sticky="news", padx=(0,10),pady=(10),text="Confirmed Percentages")
        self.images_frame=LabelFrame(self,row=0,column=0, text="Images")
        self.migrate_frame=Frame(self,row=0, column=2, sticky="ew", padx=10)
        self.button_frame=Frame(self,row=2, column=0, sticky="news", padx=10, pady=10, columnspan=4)
        self.populate_all_percents_frame()
        self.populate_confirmed_percentages_frame()
        self.populate_images_frame()
        self.populate_migrate_frame()
        self.populate_button_frame()

    #The below functions fill the various frames of the Auto Tab    
    def populate_images_frame(self):
        Button(self.images_frame, text="Add Image Folder", row=0,column=0, pady=0, padx=(0), command=MainApplication.open_image_folder)
        Button(self.images_frame, text="Add Image File", row=1,column=0, pady=0, padx=(0), command=MainApplication.open_image_file)
        Button(self.images_frame, text="Delete Image", row=2,column=0, pady=0, padx=(0), command=self.delete_image)
        self.images_frame.listbox_frame=Frame(self.images_frame,column=1,row=0,rowspan=3)
        self.images_frame.box=tk.Listbox(self.images_frame.listbox_frame, height=12, width=32, selectmode='single',exportselection=False)
        self.images_frame.box.pack(side='left', fill=Y)
        self.images_frame.box.bind("<<ListboxSelect>>",self.on_image_select)
        self.images_frame.scrollbar=tk.Scrollbar(self.images_frame.listbox_frame, orient=VERTICAL)
        self.images_frame.scrollbar.config(command=self.images_frame.box.yview)
        self.images_frame.scrollbar.pack(side=RIGHT, fill=Y)

    def populate_migrate_frame(self):
        Button(self.migrate_frame, text="←", row=0,column=0, pady=0, command=self.move_left)

    def populate_confirmed_percentages_frame(self):
        self.confirmed_percents_frame.commit_button=Button(self.confirmed_percents_frame, text="Preview", row=0,column=0,padx=(0), pady=0, command=self.generate_preview)
        Button(self.confirmed_percents_frame, text="Delete", row=1,column=0,padx=(0), pady=0, command=self.delete_confirmed_percentage)
        self.confirmed_percents_frame.listbox_frame=Frame(self.confirmed_percents_frame,column=1,row=0,rowspan=3)
        self.confirmed_percents_frame.box=tk.Listbox(self.confirmed_percents_frame.listbox_frame, height=12, width=25, selectmode='multiple')
        self.confirmed_percents_frame.box.pack(side='left', fill=Y)
        self.confirmed_percents_frame.scrollbar=tk.Scrollbar(self.confirmed_percents_frame.listbox_frame, orient=VERTICAL)
        self.confirmed_percents_frame.scrollbar.config(command=self.confirmed_percents_frame.box.yview)
        self.confirmed_percents_frame.scrollbar.pack(side=RIGHT, fill=Y)

    def populate_all_percents_frame(self):
        Button(self.all_percents_frame,padx=0, text="Use All",column=1,rowspan=1, row=0, pady=0, command=self.use_all)
        Button(self.all_percents_frame,padx=0, text="Add Percentage",column=1, row=1, pady=0, command=self.add_percentage)
        Button(self.all_percents_frame,padx=0, text="Delete Percentage",column=1, row=2, pady=0, command=self.delete_percentage)
        self.all_percents_frame.listbox_frame=Frame(self.all_percents_frame,column=0,row=0,rowspan=4)
        self.all_percents_frame.box=tk.Listbox(self.all_percents_frame.listbox_frame, height=12, width=25, selectmode='multiple',exportselection=False)
        self.all_percents_frame.box.pack(side='right', fill=Y)
        self.all_percents_frame.scrollbar=tk.Scrollbar(self.all_percents_frame.listbox_frame, orient=VERTICAL)
        self.all_percents_frame.scrollbar.config(command=self.all_percents_frame.box.yview)
        self.all_percents_frame.scrollbar.pack(side=LEFT, fill=Y)

    def populate_button_frame(self):
        Button(self.button_frame, text="Update", row=0,column=0, pady=0, padx=(0), width=140, command=self.update)

    #Updates the listbox content
    def update(self):
        self.clear_box(self.images_frame.box)
        self.clear_box(self.all_percents_frame.box)
        self.display_to_listbox(content=MainApplication.files,box=self.images_frame.box)
        self.display_to_listbox(content=MainApplication.percentages,box=self.all_percents_frame.box)

    def on_image_select(self,*args):
        selection=(self.read_selection(self.images_frame.box))
        if not selection:
            return
        confirmed_percents=MainApplication.confirmed_images[selection[0]]["Percentages"]
        self.clear_box(self.confirmed_percents_frame.box)
        self.display_to_listbox(confirmed_percents,self.confirmed_percents_frame.box)

    #Listbox logic
    def display_to_listbox(self, content, box):
        for item in content:
            box.insert(END, item)

    def read_selection(self, box):
        selected_items=[]
        selection=box.curselection()
        for plate in (selection):
            selected_items.append(box.get(plate))
        return selected_items
    
    def delete_items(self, box):
        selection=box.curselection()
        for plate in reversed(selection):
            box.delete(plate)

    def clear_box(self, box):
        box.selection_set(0,"end")
        self.delete_items(box)

    def move_left(self):
        try:
            image=self.read_selection(self.images_frame.box)[0]
            if not image:
                messagebox.showwarning(title="Invalid selection",message="An image must be selected")
                return
            selection=self.read_selection(self.all_percents_frame.box)
            if not selection:
                messagebox.showwarning(title="Invalid selection",message="At least one percentage must be selected")
                return
            percent_list=MainApplication.confirmed_images[image]["Percentages"]
            unique_list=[]
            for percentage in selection:
                if float(percentage) not in percent_list:
                    percent_list.append(float(percentage))
                    unique_list.append(percentage)
            self.display_to_listbox(unique_list, self.confirmed_percents_frame.box)
        except(IndexError):
            messagebox.showerror(title="No Image selected", message="No image is selected, this sometimes happens when using the 'add percentages button'. Select an image and try again")

    #Image logic
    def generate_preview(self):
        pass

    #Data and dictionary logic
    def delete_image(self):
        selection=self.read_selection(self.images_frame.box)
        if not selection:
            return
        image=selection[0]
        MainApplication.files.remove(image)
        del MainApplication.confirmed_images[image]
        self.update()
    
    def delete_confirmed_percentage(self):
        selection=self.read_selection(self.images_frame.box)
        if not selection:
            return
        image=selection[0]
        selection=self.read_selection(self.confirmed_percents_frame.box)
        if not selection:
            return
        for item in reversed(selection):
            MainApplication.confirmed_images[image]["Percentages"].remove(item)
        self.delete_items(self.confirmed_percents_frame.box)
    
    def delete_percentage(self):
        selection=self.read_selection(self.all_percents_frame.box)
        if not selection:
            return
        for item in (selection):
            MainApplication.percentages.remove(item)
        self.delete_items(self.confirmed_percents_frame.box)
        self.update()

    def add_percentage(self):
        percentage=simpledialog.askfloat(title="Enter percentage", prompt="Please enter a percentage between 0 and 100 (non inclusive):")
        if not percentage:
            messagebox.showerror(title="No value entered", message="No value was given")
            return
        if percentage not in MainApplication.percentages:
            MainApplication.percentages.append(percentage)
        self.update()
    
    def use_all(self):
        for image_file in MainApplication.files:
            existing_percentages = MainApplication.confirmed_images[image_file]["Percentages"]
            
            for new_percentage in MainApplication.percentages:
                if new_percentage not in existing_percentages:
                    existing_percentages.append(new_percentage)
    
class PlayTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.populate()
        self.parent=parent
        
    def populate(self):
        self.source_sub_but=Button(self, text="Export to PPTX", row=0,column=0, pady=0, padx=(0), command=self.export_to_pptx)
        self.dest_sub_but=Button(self, text="Export To File System", row=1,column=0, pady=0, padx=(0), command=self.export)

    def export_to_pptx(self):
        self.export()
        # Prompt user to save the PowerPoint file
        ppt_location = filedialog.asksaveasfilename(
            title="Save PPT file",
            defaultextension=".pptx",
            initialdir=MainApplication.destination,
            initialfile="Pixelate Powerpoint"
        )

        # Create a PowerPoint presentation
        prs = Presentation()

        # Define slide dimensions (default 10x7.5 inches for a standard slide)
        slide_width = prs.slide_width
        slide_height = prs.slide_height

        other_dirs = []

        # Walk through the directories to find "Pixelate Logo" and other folders
        for root, dirs, files in os.walk(MainApplication.destination, topdown=False):
            # Check for the "Pixelate Logo" directory first
            if "Pixelate Logo" in dirs:
                logo_dir = os.path.join(root, "Pixelate Logo")
                # Process logo images
                for logo_file in sorted(os.listdir(logo_dir)):  # Sort the logo files
                    logo_path = os.path.join(logo_dir, logo_file)

                    # Create a slide for the logo
                    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank slide layout
                    slide.shapes.add_picture(logo_path, 0, 0, width=slide_width, height=slide_height)

                # Remove "Pixelate Logo" from dirs
                dirs.remove("Pixelate Logo")

            # Collect remaining directories for random processing
            for dir in dirs:
                other_dirs.append(os.path.join(root, dir))

        # Shuffle remaining directories
        random.shuffle(other_dirs)

        # Process images from remaining directories
        for dir in other_dirs:
            for file in sorted(os.listdir(dir)):  # Sort the files for consistent order
                image_path = os.path.join(dir, file)

                # Create a slide
                slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank slide layout
                slide.shapes.add_picture(image_path, 0, 0, width=slide_width, height=slide_height)

                notes_slide = slide.notes_slide
                notes_slide.notes_text_frame.text = f"Image: {file}"

        # Save the PowerPoint presentation
        prs.save(ppt_location)
        

    def export(self):
        if not MainApplication.destination:
            MainApplication.destination=MainApplication.open_directory()
        if not MainApplication.destination:
            return False
        folders=self.generate_folders()
        for i in range(len((MainApplication.files))-1):
            file=MainApplication.files[i]
            folder=folders[i]
            self.gen_output(file, folder)
        messagebox.showinfo(title='Files Saved', message='Files successfully saved')
            
        
    def generate_folders(self):
        folders=[]
        for image in MainApplication.files:
            subject_name=re.search(r'([^\/]+)\.([a-zA-Z0-9]+)$',image).group(1)
            subject_folder=f"{MainApplication.destination}/{subject_name}"
            folders.append(subject_folder)
            try:
                os.mkdir(subject_folder)
            except(FileExistsError):
                continue
        return folders

    def gen_output(self, file, folder):
        percentages=MainApplication.confirmed_images[file]["Percentages"]
        file_path=MainApplication.confirmed_images[file]["Path"]
        for percentage in percentages:
            name=MainApplication.generate_image_name(file,percentage)[0]
            image=MainApplication.generate_image(file_path,percentage)
            self.save_image(name,image,folder)          

    def save_image(self,filename,image,folder):
        full_fname=f"{folder}/{filename}"
        image.save(full_fname)


#Below are the generic components
class CustomEntry(tk.Entry):
    instance_list = []

    def __init__(self, parent, row=0, column=0, columnspan=1, rowspan=1,
                 padx=(10, 0), pady=(10, 0), sticky="nesw", width=None,
                 state=tk.NORMAL,  placeholder=None, placeholder_color='grey', **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(state=state, font=MainApplication.current_font)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.default_fg_color = self['fg']
        if placeholder:
            self._add_placeholder()
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        Entry.instance_list.append(weakref.ref(self))

    def _add_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def _on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _on_focus_out(self, event):
        if not self.get():
            self._add_placeholder()

    def get_text(self):
        return self.get()

    def set_text(self, text):
        self.delete(0, tk.END)
        self.insert(0, text)
        
    def clear(self):
        self.delete(0, tk.END)
    
    def enable(self):
        self.configure(state=tk.NORMAL)

    def disable(self):
        self.configure(state=tk.DISABLED)

class Frame(tk.Frame):
    instance_list = []

    def __init__(self, parent, row=0, column=0, columnspan=1, rowspan=1,
                 padx=(0, 0), pady=(0, 0), sticky="nesw", width=None, height=None,
                 bg=None, relief=None, borderwidth=None, **kwargs):
        super().__init__(parent, width=width, height=height, bg=bg, relief=relief,
                         borderwidth=borderwidth, **kwargs)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        Frame.instance_list.append(weakref.ref(self))

    def show(self):
        self.grid()

    def hide(self):
        self.grid_remove()

class LabelFrame(tk.LabelFrame):
    instance_list = []

    def __init__(self, parent, text="", row=0, column=0, columnspan=1, rowspan=1,
                 padx=(10, 0), pady=(10, 0), sticky="nesw", width=None, height=None,
                 labelanchor='n', font=None, bg=None, relief=None, borderwidth=None,
                 **kwargs):
        super().__init__(parent, text=text, labelanchor=labelanchor, font=font, bg=bg,
                         relief=relief, borderwidth=borderwidth, **kwargs)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        if height:
            self.configure(height=height)
        LabelFrame.instance_list.append(weakref.ref(self))

    def show(self):
        """Show the label frame."""
        self.grid()

    def hide(self):
        """Hide the label frame."""
        self.grid_remove()

class Button(tk.Button):
    instance_list = []

    def __init__(self, parent, text="Button", command=None, row=0, column=0,
                 columnspan=1, rowspan=1, padx=(10, 0), pady=(10, 0),
                 sticky="nesw", width=None, state=tk.NORMAL, **kwargs):
        super().__init__(parent, text=text, command=command, state=state,
                         font=MainApplication.current_font, **kwargs)
        self.text = text
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        Button.instance_list.append(weakref.ref(self))

    def set_text(self, text):
        """Set the button's text."""
        self.configure(text=text)
        self.text = text

    def get_text(self):
        """Get the button's current text."""
        return self.cget("text")

    def enable(self):
        """Enable the button."""
        self.configure(state=tk.NORMAL)

    def disable(self):
        """Disable the button."""
        self.configure(state=tk.DISABLED)

class Label(tk.Label):
    instance_list = []

    def __init__(self, parent, text="Label", row=0, column=0, columnspan=1,
                 rowspan=1, padx=(10, 0), pady=(10, 0), sticky="nesw",
                 width=None, font=None, **kwargs):
        super().__init__(parent, text=text, font=font or MainApplication.current_font, **kwargs)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        Label.instance_list.append(weakref.ref(self))

    def set_text(self, new_text):
        """Set the label's text."""
        self.configure(text=new_text)

    def get_text(self):
        """Get the label's current text."""
        return self.cget("text")

class Checkbox(ttk.Checkbutton):
    instance_list = []

    def __init__(self, parent, name, row=0, column=0, columnspan=1, rowspan=1,
                 padx=(10, 0), pady=(10, 0), sticky="w", error_msg=None,
                 variable=None, command=None, **kwargs):
        super().__init__(parent, text=name, command=command, **kwargs)
        self.name = name
        self.variable = variable or tk.BooleanVar(self)
        self.configure(variable=self.variable)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if error_msg is None:
            self.error_msg = f"{name.capitalize()} checkbox was left unticked"
        else:
            self.error_msg = error_msg
        Checkbox.instance_list.append(weakref.ref(self))

    def is_checked(self):
        """Return the current state of the checkbox."""
        return self.variable.get()

    def set_checked(self, value):
        """Set the state of the checkbox."""
        self.variable.set(value)

    def toggle(self):
        """Toggle the state of the checkbox."""
        self.variable.set(not self.variable.get())

class Combobox(ttk.Combobox):
    instance_list = []

    def __init__(self, parent, values=None, default=None, row=0, column=0,
                 columnspan=1, rowspan=1, padx=(0, 0), pady=(0, 0), sticky="nesw",
                 width=None, state='readonly', variable=None, **kwargs):
        # Initialize variable
        self.variable = variable or tk.StringVar()
        super().__init__(parent, textvariable=self.variable, state=state, **kwargs)
        
        # Set values
        if values is None:
            self['values'] = ["Default Value"]
        else:
            self['values'] = values

        # Set default selection
        if default is not None:
            self.set_value(default)
        elif values:
            self.set_value(values[0])  # Set to the first value if default is not specified

        # Grid configuration
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)

        # Add to instance list
        Combobox.instance_list.append(weakref.ref(self))

    def get_value(self):
        """Return the current value of the combobox."""
        return self.variable.get()

    def set_value(self, value):
        """Set the value of the combobox."""
        if value in self['values']:
            self.variable.set(value)
        else:
            raise ValueError(f"'{value}' is not in the list of combobox values.")

    def add_value(self, value):
        """Add a new value to the combobox."""
        current_values = list(self['values'])
        current_values.append(value)
        self['values'] = current_values

    def remove_value(self, value):
        """Remove a value from the combobox."""
        current_values = list(self['values'])
        if value in current_values:
            current_values.remove(value)
            self['values'] = current_values
        else:
            raise ValueError(f"'{value}' is not in the list of combobox values.")

class Spinbox(ttk.Spinbox):
    instance_list = []

    def __init__(self, parent, from_=1, to=12, increment=1, default=None,
                 row=0, column=0, columnspan=1, rowspan=1, padx=(0, 0), pady=(0, 0),
                 sticky="nesw", width=None, state='normal', command=None,
                 variable=None, **kwargs):
        # Initialize variable
        self.variable = variable or tk.StringVar()
        super().__init__(parent, from_=from_, to=to, increment=increment,
                         textvariable=self.variable, command=command, state=state, **kwargs)

        # Set default value
        if default is not None:
            self.set_value(default)
        else:
            # Set to the midpoint between from_ and to
            midpoint = (from_ + to) / 2
            self.set_value(midpoint)

        # Grid configuration
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                  padx=padx, pady=pady, sticky=sticky)

        if width:
            self.configure(width=width)

        # Add to instance list
        Spinbox.instance_list.append(weakref.ref(self))

    def get_value(self):
        """Return the current value of the spinbox as a float or int."""
        value = self.variable.get()
        try:
            # Try to return as int if possible
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value  # Return as is if not a number

    def set_value(self, value):
        """Set the value of the spinbox."""
        self.variable.set(value)

    def enable(self):
        """Enable the spinbox."""
        self.configure(state='normal')

    def disable(self):
        """Disable the spinbox."""
        self.configure(state='disabled')

    def increment(self):
        """Increment the spinbox value by the specified increment."""
        current_value = self.get_value()
        self.set_value(current_value + self.cget('increment'))

    def decrement(self):
        """Decrement the spinbox value by the specified increment."""
        current_value = self.get_value()
        self.set_value(current_value - self.cget('increment'))

class Entry(tk.Entry):
    instance_list=[]

    def __init__(self,parent, column=0, row=0, state=NORMAL):
        super().__init__(parent)
        self.grid(row=row,column=column)
        self.configure(state=state)
        Entry.instance_list.append(self)

    def read(self):
        return self.get()
    
    def set_text(self, text):
        self.delete(0,'END')
        self.insert(0,text)
        return
    
    def enable(self):
        self.configure(state=tk.NORMAL)

    def disable(self):
        self.configure(state=tk.DISABLED)

class Canvas(tk.Canvas):
    
    def __init__(self, parent, bg= 'black', bd=0, highlight=0, relief='ridge', column=0, row=0, rowspan=1,columnspan=1):
        super().__init__(parent, background= bg, bd=bd, highlightthickness=highlight, relief=relief)
        self.parent=parent
        self.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

#This is a custom component that simply combines the checkbox and label and places them together
class Labelled_Checkbox():

    def __init__(self, parent, text="text", column=0, row=0):
        Label(parent,text=text, column=column,row=row)
        self.checkbox=Checkbox(parent, name=text, column=(column+1), row=row)      

if __name__ == '__main__':
    app = MainApplication("Pixelator Builder and Client Launcher")
    app.mainloop()