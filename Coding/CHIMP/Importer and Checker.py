import tkinter as tk #Tkinter is the module that allows the GUI to exist
from tkinter import ttk #Tkinter is the module that allows the GUI to exist
from tkinter import messagebox #Tkinter is the module that allows the GUI to exist
from tkinter import filedialog #Tkinter is the module that allows the GUI to exist
from tkinter import *
import re #Regex library
import os #Module that allows reading all files in folder, reading current user, and reads the modification date for files
from datetime import datetime
from hashlib import sha256

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class MainApplication(tk.Tk):

    current_font=("Times New Roman", 12)
    max_plates=12
    wells_per_plate=96
    coord_to_wellno={}
    wellno_to_coord={}
    coord_list=[]

    def __init__(self, win_title, icon):
        super().__init__()
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.title(win_title)
        self.iconbitmap(icon)
        self.notebook = ttk.Notebook(self)
        self.import_frame = ImportTab(self.notebook)
        self.checker_frame = CheckerTab(self.notebook)
        self.notebook.add(self.import_frame, text='Import')
        self.notebook.add(self.checker_frame, text='Check')
        self.notebook.pack()
        MainApplication.map_coordinates()
    
    def map_coordinates():
        MainApplication.coord_to_wellno={}
        MainApplication.wellno_to_coord={}
        MainApplication.coord_list=[]

        with open("Lookup_Vert_document.txt") as dir_mode:#Reads the direction file 
            position=0
            for line in dir_mode:
                position+=1
                coord=line.strip()
                MainApplication.coord_to_wellno[coord]=position
                MainApplication.wellno_to_coord[position]=coord
                MainApplication.coord_list.append(coord)

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
        ImportTab.change_font(font)
        CheckerTab.change_font(font)
    
    def open_single_file():
        messagebox.showwarning(title="User Info", message="This importer is to be used on the files on the H: drive\nDO NOT USE FILES FROM THE EXCEL TOPCOUNT MACRO")
        full_fname=filedialog.askopenfilename(title='Select a file', filetypes=(("All files","*.*"),("ASCII files","*min.*"),("Text files","*.txt")))
        if not full_fname:
            selection=messagebox.askretrycancel(title="No file selected", message="No file was selected, would you like to try again?")
            if selection:
                MainApplication.open_single_file()
            else:
                return False
        return full_fname
    
    def open_directory():
        messagebox.showwarning(title="Select a folder", message="Please select the folder for the function chosen")
        directory=filedialog.askdirectory(title='Select a file')
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
        
    def file_edit_check(filename):#Reads the 'created' and 'modified' times in the windows system for a given file
        try:
            epoch_stamp_creation = os.path.getctime(filename)
            epoch_stamp_modification = os.path.getmtime(filename)
            if abs(epoch_stamp_creation-epoch_stamp_modification)>30:
                return False
            else:
                return True
        except(FileNotFoundError):
            return "File not found"

class Font_window(tk.Toplevel):

    fonts=["Arial","Helvetica","Times","Times New Roman", "Courier", "Wingdings"]
    font_sizes=[8,9,10,12,14,16,18,20,24,30,36,48,72,100]

    def __init__(self,parent,top_level,):
        super().__init__(parent)
        self.parent=parent
        self.top_level = top_level
        self.populate()
        self.iconbitmap("Company_logo.ico")
        ImportTab.change_font(MainApplication.current_font)
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

class ImportTab(ttk.Frame):
    max_plates=12
    samples=[]
    psn_list=[]
    sample_data={}
    used_files=[]
    plate_listbox_labels=[]
    labelled_plates={}

    def __init__(self, parent):
        super().__init__(parent)
        ImportTab.plate_bin_frame=PlateBinFrame(self)
        ImportTab.assay_plate_frame=AssayPlatesFrame(self)
        ImportTab.sample_frame=SampleFrame(self)
        MigrateFrame(self)
        Button_Frame(self)
        ImportTab.change_font(MainApplication.current_font)

    def import_study(self):
        messagebox.showinfo(title="Select Study Folder", message="Select folder containing assays from data share (D:/ Drive)")
        directory=MainApplication.open_directory()
        if not directory or directory == '':
            return
        files=os.listdir(directory)
        for file in files:
            full_fname=f"{directory}/{file}"
            self.import_recounts(full_fname)
    
    def get_recount_file(self):
        full_fname=MainApplication.open_single_file()
        if not full_fname:
            return False
        self.import_recounts(full_fname)

    def import_recounts(self, file):
        self.full_fname=file
        if not self.valid_file_choice(self.full_fname):
            return
        if not self.confirm_file_choice(self.full_fname):
            return
        self.used_files.append(self.full_fname)
        short_fname=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', self.full_fname).group(1)
        self.plates=self.extract_plates(self.file_contents())
        self.short_fname=short_fname.replace(".","_Assay")
        self.assay_name=self.short_fname
        self.process(file)

    def valid_file_choice(self,filename):
        if not filename or filename=="":
            messagebox.showerror(parent=self,title="File Error", message="No file selected")
            return False
        elif filename in self.used_files:
            messagebox.showerror(parent=self,title="File Error", message="This File is Already in Use")
            return False
        else:
            return True
    
    def confirm_file_choice(self, filename):
        return messagebox.askyesno('Confirmation',parent=self, message=f'Continue using file:{filename}?')
    
    def file_contents(self):
        read_lines=[]
        with open(self.full_fname, "r") as file:
            for line in file:
                try:
                    read_lines.append(int(line.strip()))
                except(ValueError):
                    self.record_psn(line)
        return read_lines

    def record_psn(self, line):
        if not line.strip().startswith('Plate Sequence Number'):
            return
        temp=re.findall('Plate Sequence Number: ([0-9]+)', line)
        psn=temp[0]
        self.psn_list.append(psn)

    def extract_plates(self, temp_list):
       plates = [temp_list[MainApplication.wells_per_plate*i:MainApplication.wells_per_plate*(i+1)] for i in range((len(temp_list)//MainApplication.wells_per_plate)+(len(temp_list)%MainApplication.wells_per_plate!=0))]
       return plates
    
    def assign_psns_2_plates(self, filename =None):
        index=len(self.labelled_plates)
        for plate in self.plates:
            self.labelled_plates[self.psn_list[index]]={'Data':plate, 'Length':len(plate), 'Final Well':MainApplication.wellno_to_coord[len(plate)], 'Source':filename}
            index+=1

    def process(self, filename):
        self.assign_psns_2_plates(filename)
        self.plate_bin_frame.clear_plates()
        for psn in self.labelled_plates:
            data=self.labelled_plates[psn]
            label=f"PSN: {psn}, Final Well: {data['Final Well']}"
            ImportTab.plate_bin_frame.box.insert(END,label)

    def change_font(font):
        ImportTab.plate_bin_frame.configure(font=font)
        ImportTab.assay_plate_frame.configure(font=font)
        ImportTab.sample_frame.configure(font=font)
        ImportTab.plate_bin_frame.box.config(font=font)
        ImportTab.assay_plate_frame.box.config(font=font)
        ImportTab.sample_frame.box.config(font=font)

    def extract_psn(text):
        psn=re.search(r'PSN: ([0-9]+)', text).group(1)
        return psn

    def plate_lookup(psn, entry):
        if not psn:
            return "Del me"
        result=ImportTab.labelled_plates[psn][entry]
        return result
    
    def assay_lookup(name, entry):
        if not name:
            return False
        result=name[entry]
        return result
    
    def reset_window(self):
        self.quit()

    def check(self):
        for sample in ImportTab.sample_data:
            plates=ImportTab.sample_data[sample]['Plates']
            if not self.check_order(plates):
                return False
        return True

    def check_order(self, plates):
        error_message=f"Only the final well of a sample may be shorter than {MainApplication.wells_per_plate}"
        i=1
        end_plates=0
        previous=0
        for plate in plates:
            data=ImportTab.labelled_plates[plate]['Data']
            if len(data)<MainApplication.wells_per_plate:
                end_plates+=1
            if end_plates==2:
                messagebox.showerror(title="Plate order error", message=error_message)
                return False
            if i==len(plates):
                break
            if len(data)<previous:
                messagebox.showerror(title="Plate order error", message=error_message)
                return False
            previous=len(data)
            i+=1
        return True

    def submit(self):
        if not self.check():
            messagebox(title='Failed to submit',message='One or more of the required checks failed')
            return
        ticket_body=""
        for sample in ImportTab.sample_data:
            plates=ImportTab.sample_data[sample]['Plates']
            read_plates=self.read_plates(plates)
            file_destination=self.write_out(read_plates, sample)
            sample_ticket=self.add_to_ticket(sample, file_destination, plates)
            ticket_body+=sample_ticket
        user=os.getlogin()
        now=datetime.now()
        datetime_stamp=now.strftime("%Y-%m-%d, %H-%M-%S")
        ticket_head=f"Created by: {user}\nDate Created: {now}\nSamples:\n{ticket_body}\n"
        ticket_head=self.create_ticket_hash(ticket_head)
        ticket_title=f"Import_ticket {datetime_stamp}"
        ticket_dest=filedialog.asksaveasfilename(parent=self, title="Save Ticket", defaultextension=".txt", initialfile=ticket_title, filetypes = (("Text files","*.txt"),("All files","*.*")))
        with open(ticket_dest, "w+") as ticket:
            ticket.truncate()
        with open(ticket_dest, "a+") as ticket:   
            ticket.write(ticket_head)
            messagebox.showinfo(title="Success", message="File created without issue")
        self.quit()

    def create_ticket_hash(self, ticket_head):
        ticket_hash_object=sha256()
        ticket_hash_object.update(ticket_head.encode('utf-8'))
        ticket_hash=ticket_hash_object.hexdigest()
        ticket_head=f"{ticket_head}Ticket Hash: {ticket_hash}"
        return ticket_head

    def read_plates(self,plates):
        output=[]
        for plate in plates:
            data=ImportTab.plate_lookup(plate,'Data')
            output.extend(data)
        return output

    def write_out(self, input, name):
        filename_suggestion=self.generate_name(name)
        destination=filedialog.asksaveasfilename(title = "Save file",initialfile = filename_suggestion,filetypes = (("Text files","*.txt"),("All files","*.*")))
        if not self.valid_file_choice(destination):
            return        
        with open(destination, "w+") as destination_file:
            destination_file.truncate()
        with open(destination, "a+") as destination_file:
            for item in input:    
                destination_file.write(f"{item}\n")
            messagebox.showinfo(title="Success", message="File created without issue")
            ImportTab.assay_plate_frame.clear_plates()
        return destination
    
    def add_to_ticket(self, sample, filepath, plates):
        sample_tickets=""
        sample_hash=self.generate_filehash(filepath)
        plate_stub=""
        for plate in plates:
            plate_ticket=f"{plate}:\nSource: {ImportTab.labelled_plates[plate]['Source']}\nLength: {ImportTab.labelled_plates[plate]['Length']}\nF Well: {ImportTab.labelled_plates[plate]['Final Well']}\nData: {ImportTab.labelled_plates[plate]['Data']}\n"
            plate_stub+=plate_ticket
        sample_ticket=f"{sample}:\nRecount: {ImportTab.sample_data[sample]['Recount']}\nN Plates: {len(ImportTab.sample_data[sample]['Plates'])}\nSaved at: {filepath}\nPlates:\n{plate_stub}\nSample hash: {sample_hash}\n"
        sample_tickets+=f"{sample_ticket}\n"
        return sample_tickets

    def generate_filehash(self, filename):
        sample_hash=sha256()
        with open(filename, 'rb') as file:
            for line in file:
                sample_hash.update(line)
        return sample_hash.hexdigest()

    def generate_name(self,name):
        plates=ImportTab.sample_data[name]['Plates']
        plate_strings=[]
        for plate in plates:
            plate_strings.append(str(plate).zfill(3))
        plate_string=f"({'-'.join(plate_strings)})"
        filename_suggestion=f"{name}{(ImportTab.sample_data[name]['Recount'])*(plate_string)}.txt"
        return filename_suggestion

    def trim_plate(self):
        selection=ImportTab.plate_bin_frame.read_selection()
        if not selection:
            messagebox.showerror(title="Invalid selection", message="No plate selected")
            return
        if len(selection)>1:
            messagebox.showerror(title="Invalid selection", message="more than one plate selected")
            return
        psn=ImportTab.extract_psn(selection[0])
        plate_length=ImportTab.plate_lookup(psn, 'Length')
        self.plate_edit_window=Edit_window('Edit plate data', psn, plate_length, self)

class Import_window(tk.Toplevel):
    assay_files=[]
    sample_data={}
    labelled_plates={}
    psn_list=[]
    samples=[]
    plate_listbox_labels=[]

    def __init__(self, parent, top_level):
        super().__init__(parent)
        self.parent=parent
        self.top_level=top_level
        self.populate()
        self.iconbitmap("Company_logo.ico")
        ImportTab.change_font(MainApplication.current_font)
        Import_window.used_files=ImportTab.used_files.copy()
        self.transient(parent) # set to be on top of the main window
        self.grab_set() # hijack all commands from the master (clicks on the main window are ignored)
        parent.wait_window(self) # pause anything on the main window until this one closes

    def populate(self):
        frame=Frame(self)
        
        param_frame=LabelFrame(frame, padx=(10), text="Sample Parameters", column=0,row=1, columnspan=2)
        Label(param_frame, row=0, column=0, text="Plates per sample:")
        Label(param_frame, row=0, column=1, text="Final Well:")
        self.plates_per_sample=Spinbox(param_frame,row=1,padx=(10,5),column=0,command=self.update_screen)
        self.final_well_coord=Combobox(param_frame,padx=(5,10),values=(MainApplication.coord_list), row=1, column=1)
        Label(param_frame, row=2, column=0, text="Wells per sample:")
        Label(param_frame, row=2, column=1, text="Final Well Number:")
        self.total_wells_lab=Label(param_frame, row=3, column=0, text="No Source Chosen")
        self.final_well_no_lab=Label(param_frame, row=3, column=1, text="No Source Chosen")
        
        source_frame=LabelFrame(frame,pady=(0,10), padx=(10), text="Source Choice", column=0,row=2, columnspan=2)
        Label(source_frame, text="Source: ", column=0, row=0)
        self.source_label=Label(source_frame, text="No File Chosen", column=1, row=0)
        Button(source_frame,width=16, text="Choose File", padx=(0), pady=(0), column=0, row=1, command=self.import_single_file)
        Button(source_frame,width=16, text="Choose Directory", padx=(0), pady=(0), column=1, row=1, command=None, state=DISABLED)
        Label(source_frame, row=2, column=0, text="Total Number of Plates:")
        Label(source_frame, row=2, column=1, text="Number of Samples:")
        self.total_plates_lab=Label(source_frame, row=3, column=0, text="No Source Chosen")
        self.no_samples_lab=Label(source_frame, row=3, column=1, text="No Source Chosen")
        
        Button(frame,padx=(0),pady=(0), text="Validate", row=3, column=0, command=self.validate)
        Button(frame,padx=(0),pady=(0), text="Cancel", row=3, column=1, command=self.destroy)
        Button(frame,padx=(0),pady=(0), text="Submit", row=4, column=0,columnspan=2, command=self.submit)

    def validate_filename(self, filename):
        try:
            test=re.search(r'[A-Z]+-[0-9]+_', filename).group(0)
            return True
        except(AttributeError):
            return False
  
    def import_single_file(self, filename=None):
        if not filename:
            filename=MainApplication.open_single_file()
        if not filename or filename=="":
            messagebox.showerror(message="No file selected", title="No file selected")
            return
        Import_window.full_fname=filename
        if not self.validate_parameters():
            return
        Import_window.used_files.append(Import_window.full_fname)
        self.short_fname=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', Import_window.full_fname).group(1)
        content=Import_window.file_contents()
        n_plates=len(content)/MainApplication.wells_per_plate
        if n_plates%int(self.plates_per_sample.get())!=0:
            messagebox.showerror(title="Invalid parameters input",message="The provded number of plates per sample must be an factor of the total number of plates in the sample")
            return
        self.plates=Import_window.extract_plates(content)
        Import_window.assay_name=self.short_fname.replace(".","_Assay")
        Import_window.assay_name=re.search(r'([A-Z]+-[0-9]+_\S+)', Import_window.assay_name).group(1)
        self.calculate_parameters()
        self.update_screen()
        self.source_label.update(self.short_fname)

    def check_file_choice(self, file):
        if not self.valid_file_choice(file):
            return False
        if not self.confirm_file_choice(file):
            return False
        return True

    def validate_parameters(self):
        if not self.check_pps():
            messagebox.showerror(parent=self, title="Plate per sample issue", message=f"Plates per sample must be an integer between 1 and {MainApplication.max_plates}")
            return False
        if not self.check_fwell():
            messagebox.showerror(parent=self, title="Invalid final well", message="Please enter a valid well coordinatew")
            return False
        return True

    def calculate_parameters(self):
        self.len_final_plate=int(MainApplication.coord_to_wellno[self.final_well_coord.get()])
        try:
            self.n_plates=len(self.plates)
            self.no_samples=int(self.n_plates/int(self.plates_per_sample.get()))
            self.no_full_plates=self.n_plates-self.no_samples
        except(AttributeError):
            return
        self.len_final_plate=int(MainApplication.coord_to_wellno[self.final_well_coord.get()])
        try:
            self.n_plates=len(self.plates)
            self.no_samples=int(self.n_plates/int(self.plates_per_sample.get()))
            self.no_full_plates=self.n_plates-self.no_samples
        except(AttributeError):
            return

    def update_screen(self):
        self.calculate_parameters()
        self.final_well_no_lab.update(self.len_final_plate)
        self.total_wells_lab.update((MainApplication.wells_per_plate*(int(self.plates_per_sample.get())-1)+self.len_final_plate))
        try:
            self.total_plates_lab.update(str(self.n_plates))
            self.no_samples_lab.update(str(self.no_samples))
        except(AttributeError):
            return
       
    def valid_file_choice(self,filename):
        if not filename or filename=="":
            messagebox.showerror(parent=self,title="File Error", message="No file selected")
            return False
        elif filename in Import_window.used_files:
            messagebox.showerror(parent=self,title="File Error", message="This File is Already in Use")
            return False
        else:
            return True
    
    def confirm_file_choice(self, filename):
        return messagebox.askyesno('Confirmation',parent=self, message=f'Continue using file:{filename}?')
        
    def file_contents():
        read_lines=[]
        with open(Import_window.full_fname, "r") as file:
            for line in file:
                try:
                    read_lines.append(int(line.strip()))
                except(ValueError):
                    Import_window.record_psn(line)
        return read_lines

    def record_psn(line):
        if not line.strip().startswith('Plate Sequence Number'):
            return
        temp=re.findall('Plate Sequence Number: ([0-9]+)', line)
        psn=temp[0]
        Import_window.psn_list.append(psn)

    def extract_plates(temp_list):
       plates = [temp_list[MainApplication.wells_per_plate*i:MainApplication.wells_per_plate*(i+1)] for i in range((len(temp_list)//MainApplication.wells_per_plate)+(len(temp_list)%MainApplication.wells_per_plate!=0))]
       return plates

    def validate(self):
        if not self.check_source():
            messagebox.showerror(parent=self, title="No file source", message="No files to be imported")
            return False
        if not self.check_pps():
            messagebox.showerror(parent=self, title="Plate per sample issue", message=f"Plates per sample must be an integer between 1 and {ImportTab.max_plates}")
            return False
        if not self.check_factor():
            messagebox.showerror(title="Plate per sample issue", message="The total number of plates must be an integer multiple of the number of plates per sample\nYou may have to close this window without submitting and try again")
            return False
        if not self.check_fwell():
            messagebox.showerror(parent=self, title="Final Well issue", message="Final well must be a valid coordinate on a plate")
            return False
        return True

    def check_source(self):
        try:
            self.plates
        except(AttributeError):
            return False
        else:
            return True

    def check_pps(self):
        try:
            check=int(self.plates_per_sample.get())
            if check<1 or check>ImportTab.max_plates:
                raise ValueError
        except(ValueError):
            return False
        else:
            return True

    def check_factor(self):
        if self.n_plates%int(self.plates_per_sample.get())!=0:
            return False
        return True

    def check_fwell(self):
        try:
            MainApplication.coord_to_wellno[self.final_well_coord.get()]
        except(KeyError):
            return False
        else:
            return True

    def submit(self):
        if not self.validate():
            messagebox.showerror(parent=self, title="Invalid input",message="One or more checks failed")
            return
        self.subdivide_assays()
        self.assign_psns_2_plates()
        self.assign_plates_2_samples()
        self.generate_listbox_labels()
        self.pass_data()
        self.clear_data()
        self.destroy()

    def subdivide_assays(self):
        if self.no_samples==1:
            self.samples.append(self.assay_name)
            return
        counter=0
        while counter<self.no_samples:
            subassay_name=f"{self.assay_name}-{alphabet[counter]}"
            counter+=1
            self.samples.append(subassay_name)

    def assign_psns_2_plates(self):
        index=len(self.labelled_plates)
        for plate in self.plates:
            self.labelled_plates[self.psn_list[index]]={'Data':plate, 'Length':len(plate), 'Final Well':MainApplication.wellno_to_coord[len(plate)],'Source':self.full_fname}
            index+=1

    def assign_plates_2_samples(self):
        counter=0
        for sample in self.samples:
            counter=self.store_plates(counter, sample)
            
    def store_plates(self, counter, sample):
        if sample not in self.sample_data:
            self.sample_data[sample] = {'Source':self.full_fname,'Recount':False,'Plates':None}
        plate_list=[]
        while (counter+1)%int(self.plates_per_sample.get())!=0:#if counter plus one is not a multiple of the number of plates per sample
                plate_list.append(self.psn_list[counter])
                counter+=1
        plate_list.append(self.psn_list[counter])
        psn=self.psn_list[counter]
        self.trim_final_plate(psn)
        self.sample_data[sample]['Plates']=tuple(plate_list)
        counter+=1
        return counter
    
    def trim_final_plate(self, psn):
        self.labelled_plates[psn]['Data']=self.labelled_plates[psn]['Data'][:self.len_final_plate]
        self.labelled_plates[psn]['Length']=self.len_final_plate
        self.labelled_plates[psn]['Final Well']=MainApplication.wellno_to_coord[self.len_final_plate]

    def subdivide_counter(self,counter):
        sub_counter=(counter+1)%int(self.plates_per_sample.get())+(int(self.plates_per_sample.get())*((counter+1)%int(self.plates_per_sample.get())==0))#
        return sub_counter
    
    def generate_listbox_labels(self):
        for item in self.samples:
            ImportTab.sample_frame.box.insert(END,item)
        for psn in self.labelled_plates:
            data=self.labelled_plates[psn]
            label=f"PSN: {psn}, Final Well: {data['Final Well']}"
            ImportTab.plate_bin_frame.box.insert(END,label)

    def pass_data(self):
        ImportTab.sample_data.update(self.sample_data)
        ImportTab.labelled_plates.update(self.labelled_plates)
        self.join_lists(self.samples, ImportTab.samples)
        self.join_lists(self.used_files, ImportTab.used_files)
        self.join_lists(self.plate_listbox_labels,ImportTab.plate_listbox_labels)
        self.join_lists(self.psn_list,ImportTab.psn_list)

    def clear_data(self):
        self.sample_data.clear()
        self.samples.clear()
        self.used_files.clear()
        self.psn_list.clear()
        self.plate_listbox_labels.clear()
        self.labelled_plates.clear()

    def join_lists(self, list_1, list_2):
        for item in list_1:
            list_2.append(item)
        
class Edit_window(tk.Toplevel):
    error_message="Error message has not been set, an error has occcurred in the application"

    def __init__(self, top_level, plate_name, plate_length, parent):
        super().__init__()
        self.top_level = top_level
        self.iconbitmap("Company_logo.ico")
        self.plate_name=plate_name
        self.plate_length=plate_length
        self.populate()
        ImportTab.change_font(MainApplication.current_font)
        self.parent=parent
    
    def populate(self):
        frame=LabelFrame(self, text="Edit Plates")
        frame.configure(font=MainApplication.current_font)
        Label(frame,text="Plate Name:",row=0,column=0)       
        Label(frame,text=self.plate_name,row=0,column=1)
        Label(frame,text="Plate Length:",row=1,column=0)       
        Label(frame,text=self.plate_length,row=1,column=1)
        Label(frame,text="Final Well:",row=2,column=0)       
        Label(frame,text=MainApplication.wellno_to_coord[self.plate_length],row=2,column=1)
        self.radio_selected = tk.IntVar()
        self.radio_selected.set(0)
        self.nwells_radio = ttk.Radiobutton(frame, text='Use no. wells', value=0, variable=self.radio_selected)
        self.fwell_radio = ttk.Radiobutton(frame, text='Use fin. well', value=1, variable=self.radio_selected)
        self.nwells_radio.grid(row=3,column=0)
        self.fwell_radio.grid(row=3,column=1)
        self.radio_selected.trace_add('write', self.onRadioButtonChange)
        Label(frame,text="New plate length:",row=4,column=0)
        self.new_number_well_entry=Entry(frame,row=4, column=1, state=NORMAL)
        Label(frame,text="New plate final well:",row=5,column=0)
        self.new_final_well_entry=Entry(frame,row=5, column=1, state=DISABLED)
        Button(frame,text="Check Edit",row=6,column=0,padx=(0),pady=(0),command=self.check)
        Button(frame,text="Cancel Edit",row=6,column=1,padx=(0),pady=(0),command=self.destroy)
        Button(frame,text="Submit Edit",row=7,column=0,columnspan=2,padx=(0),pady=(0),command=self.submit)
    
    def check(self):
        if not self.radio_selected.get():
            if not self.validate_nwells(self.new_number_well_entry.get()):
                messagebox.showerror(title="Invalid request", message=self.error_message)
                return False
        if self.radio_selected.get():
            if not self.validate_fwell(self.new_final_well_entry.get()):
                messagebox.showerror(title="Invalid request", message=self.error_message)
                return False
        messagebox.showinfo(title="Success", message="Values given are valid")
        return True
            
    def validate_nwells(self, nwells):
        try:
            new_fwell=int(nwells)
        except(ValueError):
            self.error_message="New final well must be integer"
            return False
        if new_fwell<1 or new_fwell>MainApplication.wells_per_plate:
            self.error_message=f"New final well must be integer between 1 & {MainApplication.wells_per_plate}"
            return False
        if new_fwell>=self.plate_length:
            self.error_message="New final well must be smaller than previous value"
            return False
        return True
    
    def validate_fwell(self, fwell):
        try:
            new_fwell=(MainApplication.coord_to_wellno[fwell.capitalize()])
        except(KeyError):
            self.error_message="The value entered must be a valid coordinate on a plate"
            return False
        if new_fwell>=self.plate_length:
            self.error_message="New final well must be before than previous value"
            return False
        return True

    def submit(self):
        if not self.check():
            messagebox.showerror(parent=self, title="Checks failed", message="One or more checksums failed")
            return
        if not self.radio_selected.get():
            new_fwell=int(self.new_number_well_entry.get())
        if self.radio_selected.get():
            new_fwell=MainApplication.coord_to_wellno[self.new_final_well_entry.get().capitalize()]
        old_plate_data=ImportTab.plate_lookup(self.plate_name,'Data')

        new_plate_data=old_plate_data[:new_fwell]
        ImportTab.labelled_plates[self.plate_name]['Data']=new_plate_data
        ImportTab.labelled_plates[self.plate_name]['Length']=len(new_plate_data)
        ImportTab.labelled_plates[self.plate_name]['Final Well']=MainApplication.wellno_to_coord[len(new_plate_data)]
        messagebox.showinfo(title="Success", message=f"{self.plate_name} has been shortened, this action cannot be undone")
        messagebox.showinfo(title="Success", message=f"{self.plate_name} has been shortened, this action cannot be undone")
        listbox_message=f"PSN: {self.plate_name}, Final Well: {ImportTab.labelled_plates[self.plate_name]['Final Well']}"
        ImportTab.plate_bin_frame.delete_plates()
        ImportTab.plate_bin_frame.box.insert(END,listbox_message)


    def onRadioButtonChange(self, *args):
        if self.radio_selected.get()==0:
            self.new_number_well_entry.delete(0,END)
            self.new_final_well_entry.delete(0,END)
            self.new_number_well_entry.config(state=NORMAL)
            self.new_final_well_entry.config(state=DISABLED)
        if self.radio_selected.get()==1:
            self.new_number_well_entry.delete(0,END)
            self.new_final_well_entry.delete(0,END)
            self.new_number_well_entry.config(state=DISABLED)
            self.new_final_well_entry.config(state=NORMAL)

class PlateBinFrame(tk.LabelFrame):
    
    def __init__(self, parent):
        super().__init__(parent, text="All Available Plates", labelanchor="nw")
        self.parent=parent
        self.grid(row=0, column=3, sticky="news", padx=(0,10),pady=(10))
        self.populate()
        
    def populate(self):
        Button(self,padx=0, text="Select Study",column=1,rowspan=1, row=0, pady=0, command=self.parent.import_study)
        Button(self,padx=0, text="Add Recounted Plates",column=1, row=1, pady=0, command=self.parent.get_recount_file)
        Button(self,padx=0, text="Repopulate",column=1, row=2, pady=0, command= self.repopulate)
        Button(self,padx=0, text="Change Final Well",column=1, row=3, pady=0, command= self.parent.trim_plate)
        self.listbox_frame=Frame(self,column=0)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=25, selectmode='multiple',exportselection=False)
        self.box.configure
        self.box.pack(side='right', fill=Y)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)

    def display_to_listbox(self, content):
        for plate in content:
            self.box.insert(END, plate)

    def delete_plates(self):
        selection=self.box.curselection()
        for plate in reversed(selection):
            ImportTab.plate_bin_frame.box.delete(plate)

    def clear_plates(self):
        self.box.selection_set(0,"end")
        self.delete_plates()

    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for plate in (selection):
            selected_items.append(self.box.get(plate))
        return selected_items
    
    def repopulate(self):
        self.clear_plates()
        for item in self.parent.labelled_plates:
            label=f"PSN: {item}, Final Well: {self.parent.labelled_plates[item]['Final Well']}"
            self.box.insert(END, label)

class MigrateFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=2, sticky="ew", padx=10)
        self.populate()
    
    def populate(self):
        Button(self, text="←", row=0,column=0, pady=0, command=self.move_left)
        Button(self, text="→", row=1,column=0, pady=0, command=self.move_right)

    def move_left(self):
        movers=ImportTab.plate_bin_frame.read_selection()
        ImportTab.assay_plate_frame.display_to_listbox(movers)
        ImportTab.plate_bin_frame.delete_plates()

    def move_right(self):
        movers=ImportTab.assay_plate_frame.read_selection()
        ImportTab.plate_bin_frame.display_to_listbox(movers)
        ImportTab.assay_plate_frame.delete_plates()

class AssayPlatesFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.configure(text="Plates", labelanchor="ne")
        self.grid(row=0,column=1, sticky="news", padx=(0,10),pady=(10))
        self.text="Final Sequence"
        self.populate()

    def populate(self):
        Button(self, text="↑", row=0,column=0,padx=(0), pady=0, command=self.move_up)
        Button(self, text="↓", row=1,column=0,padx=(0), pady=0, command=self.move_down)
        Button(self, text="Delete", row=2,column=0,padx=(0), pady=0, command=self.delete_plates)
        self.commit_button=Button(self, text="Commit\nChanges", row=3,column=0,padx=(0), pady=0, command=self.commit)
        self.listbox_frame=Frame(self,column=1)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=25, selectmode='multiple')
        self.box.pack(side='left', fill=Y)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def move_up(self):
        selection=self.box.curselection()
        selected_text=self.read_selection()
        if not selection:
            return
        if len(selection)>1:
            messagebox.showerror(title="Invalid request", message="Only 1 item can be selected for this command")
            return
        if selection[0]==0:
            return
        self.box.delete(selection[0])
        self.box.insert(selection[0]-1,selected_text[0])
        self.box.selection_set(selection[0]-1)

    def move_down(self):
        selection=self.box.curselection()
        selected_text=self.read_selection()
        if not selection:
            return
        if len(selection)>1:
            messagebox.showerror(title="Invalid request", message="Only 1 item can be selected for this command")
            return
        if selection[0]==ImportTab.assay_plate_frame.box.index("end"):
            return
        self.box.delete(selection[0])
        self.box.insert(selection[0]+1,selected_text[0])
        self.box.selection_set(selection[0]+1)

    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for plate in (selection):
            selected_items.append(self.box.get(plate))
        return selected_items
    
    def delete_plates(self):
        selection=self.box.curselection()
        for plate in reversed(selection):
            self.box.delete(plate)

    def clear_plates(self):
        self.box.selection_set(0,"end")
        self.delete_plates()

    def display_to_listbox(self, content):
        for plate in content:
            self.box.insert(END, plate)

    def validate_entries(self):
        self.box.selection_set(0,END)
        if self.selection_empty():
            return False
        selection=self.selection_get()
        if not self.valid_positions(selection):
            return False
        if not self.validate_lengths():
            return False
        self.box.selection_clear(0,END)
        return True

    def selection_empty(self):
        try:
            self.box.selection_get()
        except(TclError):
            messagebox.showerror(title="No Final Sequence", message="No final sequence plates found")
            return True
        return False

    def valid_positions(self, selection):
        if len(selection)==1:
            return True
        if not self.validate_nonfinal_lengths():
            return False
        return True
    
    def validate_lengths(self):
        self.box.selection_set(0,END)
        selection=self.read_selection()
        for item in selection:
            psn=ImportTab.extract_psn(item)
            length=ImportTab.plate_lookup(psn, 'length')
            if not (length>=1 and length<=MainApplication.wells_per_plate):
                messagebox.showerror(title="Plate length issue", message=f"Plates must be between 1 and {MainApplication.wells_per_plate} wells long")
                return False
        return True

    def validate_nonfinal_lengths(self):
        self.box.selection_clear("end", 'end')
        selection=self.read_selection()
        for item in selection:
            psn=ImportTab.extract_psn(item)
            length=ImportTab.plate_lookup(psn, 'length')
            if length<MainApplication.wells_per_plate:
                messagebox.showerror(title="Plate order issue", message=f"Only the final plate in a sequence may be fewer than {MainApplication.wells_per_plate} wells long")
                return False
        return True
    
    def commit(self):     
        temp_storage={}
        self.box.selection_set(0,END)
        selection=self.read_selection()
        assay=self.parent.sample_frame.get_selected_assay()
        temp_storage=[]
        for plate in selection:
            psn=re.search('PSN: ([0-9]+)', plate).group(1)
            temp_storage.append(psn)
        ImportTab.sample_data[assay]['Plates']=tuple(temp_storage)
        self.box.select_clear
        self.parent.sample_frame.box.selection_clear(0,END)
        self.box.selection_clear(0,END)
        self.box.delete(0,END)
        messagebox.showinfo(title="Sample data updated",message="Changes successfully committed sample data have been changed")

    def populate_plates_box(self, assay):
        plate_list=assay['Plates']
        self.clear_plates()
        for plate in plate_list:
            f_well=ImportTab.plate_lookup(plate, 'Final Well')
            label=f"PSN: {plate}, Final Well: {f_well}"
            self.box.insert(END,label)

class ManualSample(tk.Toplevel):

    def __init__(self, parent, top_level):
        super().__init__(parent)
        self.parent=parent
        self.top_level=top_level
        self.index=0
        self.populate()
        self.iconbitmap("Company_logo.ico")
        ImportTab.change_font(MainApplication.current_font)

    def populate(self):
        self.frame=Frame(self)
        self.static_source= Label(self.frame, text="Source:",row=0, column=0)
        self.source_label=Label(self.frame, text="No source chosen", row=0, column=1)
        self.button_choose_file=Button(self.frame, text="Choose File", command=self.choose_file,row=0, column=2, padx=(10))
        self.label_num_samples=Label(self.frame, text="Number of samples:",row=1, column=0)
        self.spinbox_num_samples=Spinbox(self.frame,row=1, column=1, from_=1, to=12, increment=1, pady=(10))
        self.submit_button=Button(self.frame,text="Submit", command=self.submit,row=2, column=0,columnspan=3, padx=(10))

    def choose_file(self):
        file=MainApplication.open_single_file()
        if not file:
            return False
        s_filename=MainApplication.get_short_fname(file)
        if not s_filename:
            return False
        self.filename=s_filename
        self.assay_name=re.search(r'([A-Z]+-[0-9]+_\S+)', self.filename).group(1)
        self.assay_name=self.assay_name.replace(".","_Assay")
        self.source_label.update(self.filename)

    def submit(self):
        try:
            for i in range(int(self.spinbox_num_samples.get())):
                label=(f"{self.assay_name}-{alphabet[i]}")
                ImportTab.sample_data[label]={}
                ImportTab.sample_data[label]['Recount']=True
                ImportTab.sample_data[label]['Plates']=[None]
                ImportTab.sample_frame.box.insert(END,label)
                self.destroy()
        except():
            pass
        
class SampleFrame(tk.LabelFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.configure(text="Samples", labelanchor="ne")
        self.grid(row=0,column=0, sticky="news", padx=(10),pady=(10))
        self.text="Samples"
        self.populate()

    def populate(self):
        Button(self, text="Add Assay", row=0,column=0, pady=0, padx=(0), command=self.add_but_press)
        Button(self, text="Add Recount", row=1,column=0, pady=0, padx=(0), command=self.add_recount)
        Button(self, text="Add Empty\nSample", row=2,column=0, pady=0, padx=(0), command=self.add_man_sample)
        Button(self, text="Delete Sample", row=3,column=0, pady=0, padx=(0), command=self.delete_sample)
        self.listbox_frame=Frame(self,column=1)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=32, selectmode='single',exportselection=False)
        self.box.pack(side='left', fill=Y)
        self.box.bind("<<ListboxSelect>>",self.on_assay_select)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def add_man_sample(self):
        self.parent.manual_sample_window=ManualSample(self.parent, "Add Manual Sample")

    def add_but_press(self):
        self.parent.font_window=Import_window(self,'Choose Font')

    def add_recount(self):
        if not self.get_selected_assay():
            messagebox.showerror(title="Operation Failed", message="A base assay must be selected to create a recount")
            return
        name=self.get_selected_assay()
        recount_label=f"{name}_R"
        self.parent.sample_data[recount_label]={'Recount':True,'Plates':[None]}
        self.box.insert(END,recount_label)        

    def on_assay_select(self,*args):
        selection=(self.get_selected_assay())
        if not selection:
            return
        assay=ImportTab.sample_data[selection]
        self.parent.assay_plate_frame.populate_plates_box(assay)

    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for plate in (selection):
            selected_items.append(self.box.get(plate))
        return selected_items

    def get_selected_assay(self):
        selection=self.box.get(ANCHOR)
        return selection
    
    def delete_sample(self):
        sample=self.get_selected_assay()
        self.box.delete(ANCHOR)
        del ImportTab.sample_data[sample]
        self.parent.assay_plate_frame.clear_plates()

class Button_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.grid(row=2, column=0, sticky="news", padx=10, pady=10, columnspan=4)
        self.populate()
    
    def populate(self):
        Button(self, text="Check", row=0,column=0, pady=0, padx=(0), width=65, command=self.parent.check)
        Button(self, text="Reset", row=0,column=1, pady=0, padx=(0), width=65, command=self.parent.reset_window)
        Button(self, text="Submit", row=1,column=0, pady=0, padx=(0), columnspan=2, command=self.parent.submit)

    def run_checks():
        if not ImportTab.assay_plate_frame.validate_entries():
            return False
        return True
        
class CheckerTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.populate()

    def populate(self):
        self.ticket_frame=Ticket_frame(self)
        self.ticket_info_frame=Ticket_Info_Frame(self)
        self.sample_check_frame=Sample_Check_Frame(self)
        self.sample_info_frame=Sample_Info_Frame(self)
        self.plate_display_frame=Plate_Display_Frame(self)
        self.plate_display_info=Plate_Info_Frame(self)
        self.report_button_frame=Report_Button_Frame(self)

class Ticket_frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Tickets", labelanchor="ne")
        self.configure(font=MainApplication.current_font)
        self.grid(row=0, column=0, sticky="news", padx=(10,0))
        self.populate()
        self.parent=parent
        self.text="Tickets"
        self.samples={}
        self.plates={}
        self.tickets={}
    
    def populate(self):
        Button(self, text="Open Folder", row=0, pady=0, command=self.open_ticket_dir)
        Button(self, text="Open single Ticket", row=1, pady=0, command=self.open_ticket_file)
        Button(self, text="Delete Ticket", row=2, pady=0, command= self.delete_ticket)
        self.listbox_frame=Frame(self,column=1)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='single')
        self.box.pack(side='left', fill=Y)
        self.box.bind("<<ListboxSelect>>",self.on_ticket_select)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)

    def open_ticket_dir(self):
        messagebox.showinfo(title="Please select",message="Choose a folder containing ticket files")
        dir=MainApplication.open_directory()
        if not dir:
            return False
        files=os.listdir(dir)
        for file in files:
            self.open_ticket_file(f"{dir}/{file}")

    def open_ticket_file(self, filename=None):
        if not filename:#This will activte if the user used the Open ticket file button
            filename=MainApplication.open_single_file()
        if not filename:#This will activate if the user fails to select a file
            messagebox.showerror(title='Invalid file choice', message='Please select a valid file')
            return False
        ticket_content=self.read_ticket(filename)
        if not self.validate_ticket(ticket_content, filename):
            return False
        self.process_ticket(filename)

    def process_ticket(self, filename):
        ticket_name=self.display_ticket(filename)
        self.tickets[ticket_name]={}
        self.digest_ticket(filename, ticket_name)

    def digest_ticket(self, filename, ticket_name):
        reading_plate=False
        reading_sample=False
        self.current_sample={}
        self.current_plate={}
        sample_title=None
        sample_plates=[]
        ticket_samples=[]
        with open(filename, "r") as file:
            for line in file:
                s_line=line.strip()
                if not s_line:
                    continue
                if s_line.startswith("Created by:"):
                    author=s_line.removeprefix("Created by: ")
                    continue
                if s_line.startswith("Date Created: "):
                    ticket_date=s_line.removeprefix("Date Created: ")
                    continue
                if s_line.startswith("Samples:"):
                    reading_sample=True
                    continue
                if s_line.startswith("Ticket Hash:"):
                    temp_dict={"Ticket Date":ticket_date,"Author":author,"Samples":ticket_samples}
                    self.tickets[ticket_name]=temp_dict.copy()
                    break
                if reading_plate:
                    if s_line.startswith("Sample hash:"):
                        sample_hash=s_line.removeprefix("Sample hash:")
                        self.current_sample['Sample Hash']=sample_hash
                        reading_plate=False
                        self.current_sample['Plates']=sample_plates
                        self.current_sample['Integrity Check']=self.file_integrity_check(self.current_sample)
                        self.current_sample['Sample Edit Flag']=MainApplication.file_edit_check(self.current_sample['Save Location'])
                        self.samples[sample_title]=self.current_sample.copy()
                        self.current_sample={}
                        self.current_plate={}
                        sample_plates=[]
                        continue
                    data=self.read_plate_data(s_line)
                    if data[0]=="PSN":
                        current_psn=data[1]
                        sample_plates.append(data[1])
                        continue
                    self.current_plate[data[0]]=data[1]
                    if data[0]=="Data":
                        self.plates[current_psn]=self.current_plate.copy()
                        self.current_plate={}
                        continue
                elif reading_sample:
                    datum=self.read_sample_details(s_line)
                    if not datum:
                        reading_plate=True
                        continue
                    elif datum[0]=="Sample name":
                        sample_title=datum[1]
                        ticket_samples.append(datum[1])
                    elif datum:
                        self.current_sample[str(datum[0])]=datum[1]

    def read_sample_details(self, s_line):#Returns some information about the sample as a tuple describing what the info is and giving the information
        if s_line.startswith("Recount: "):
            try:
                recount=eval(s_line.removeprefix("Recount: "))
            except(NameError):
                recount="Indeterminate, error in processing"
            output=("Recount",recount)
            return output
        elif s_line.startswith("N Plates: "):
            n_plates=s_line.removeprefix("N Plates: ")
            output=("N Plates",n_plates)
            return output
        elif s_line.startswith("Saved at: "):
            file_location=s_line.removeprefix("Saved at: ")
            output=("Save Location",file_location)
            return output
        elif s_line.startswith("Plates:"):
            return False
        else:
            sample_name=s_line.removesuffix(":")
            output=("Sample name",sample_name)
            return output

    def read_plate_data(self, s_line):
        if s_line.startswith("Source: "):
            source=s_line.removeprefix("Source: ")
            output=("Source",source)
            return output
        elif s_line.startswith("Length: "):
            length=s_line.removeprefix("Length: ")
            output=("Length",length)
            return output
        elif s_line.startswith("F Well: "):
            f_well=s_line.removeprefix("F Well: ")
            output=("F Well",f_well)
            return output
        elif s_line.startswith("Data: "):
            data=s_line.removeprefix("Data: ")
            output=("Data",data)
            return output        
        else:
            psn=s_line.removesuffix(":")
            output=("PSN",psn)
            return output

    def display_ticket(self, filename):
        short_filename=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', filename).group(1)
        self.box.insert(END, short_filename)
        return short_filename
        
    def read_ticket(self, ticket):
        sample_hashes=[]
        ticket_text=""
        ticket_hash=False
        filename=False
        path=False
        hash=False
        with open(ticket, "r") as file:
            for line in file:
                s_line=line.strip()#strips whitespace characters from the ends of the line
                if not line:#Skips empty lines
                    continue
                if not ticket_hash:
                    ticket_hash=Ticket_frame.check_for_ticket_hash(s_line)
                if not filename:
                    filename=Ticket_frame.get_filename(s_line)
                #The following blocks search each line for a filepath and a hash
                if s_line.startswith("Saved at: "):
                    path=s_line.removeprefix("Saved at: ")
                if s_line.startswith("Sample hash: "):
                    hash=line.removeprefix("Sample hash: ")
                #The next block checks if a matching hash and path have been found, records them and resets them
                if path and hash and filename:
                    sample_hashes.append((filename, path, hash))
                    filename=None
                    path=None
                    hash=None
                #Records the ticket hash and breaks out of the loop
                if line.startswith("Ticket Hash:"):
                    ticket_hash=line.removeprefix("Ticket Hash:").strip()
                    break
                ticket_text+=line
        if not ticket_hash:
            messagebox.showerror(title="Ivalid ticket", message="No ticket hash was found, ticket may not be formatted to the current standard")
        output={'text':ticket_text, 'orig hash':ticket_hash, 'output files':sample_hashes}
        return output

    def get_filename(s_line):
        try:#Try block searches each line for a file name in the format ABC-123_Example
            filename=re.search(r'(^[A-Z]+-[0-9]+_\S+):', s_line).group(1)
            return filename
        except(AttributeError):#Except block tells program that failing to find the file name means it should just move on
            pass

    def check_for_ticket_hash(line):
            try:
                ticket_hash = re.search(r'Ticket Hash:\s*([a-fA-F0-9]+)', line).group(1)
                return ticket_hash
            except(AttributeError):
                pass

#The below functions are for the integrity checks of the ticket itself            
    def validate_ticket(self, ticket,filename):
        gen_hash=self.create_ticket_hash(ticket['text'])
        orig_hash=ticket['orig hash']
        if gen_hash!=orig_hash:
            short_fname=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', filename).group(1)
            messagebox.showerror(title='Hash mismatch',message=f'The hash read from ticket {short_fname} does not match the one that should have been generated, suggesting it was somehow altered')
            return False
        edit_check=MainApplication.file_edit_check(filename)
        if not edit_check:
            short_fname=re.search(r'([^\\\/]+)(?=[^\\\/]*$)', filename).group(1)
            messagebox.showerror(title='Edit check failure',message=f'The file {short_fname}\n was created at {creation_time}\n but was edited at {modification_time}')
            return False
        return True
    
    def create_ticket_hash(self, ticket):
            ticket_hash_object=sha256()
            ticket_hash_object.update(ticket.encode('utf-8'))
            ticket_hash=ticket_hash_object.hexdigest()
            return ticket_hash
    

#The below functions are for the integrity checks on the individual sample files
    def generate_filehash(self, filename):
        sample_hash=sha256()
        try:
            with open(filename, 'rb') as file:
                for line in file:
                    sample_hash.update(line)
            return sample_hash.hexdigest()
        except(FileNotFoundError):
            messagebox.showerror(parent=self, title="File not found", message=f"The file {filename} could not be found")
            return False

    def file_integrity_check(self, sample):
        file=sample['Save Location']
        read_hash=sample['Sample Hash']
        test_hash=self.generate_filehash(file)
        if not test_hash:
            error_message=f"The file '{file}' could not be read"
            return False
        if test_hash.strip()!=read_hash.strip():
            error_message=f"The generated hash for the file at {file}\n is {test_hash}\nbut the hash in the ticket is:\n{read_hash}\nThis may indicate that the file has been altered"
            messagebox.showerror(parent=self, title="File integrity issue", message=error_message)
            return False
        else:
            return True

#The below functions serve to allow the listbox displaying
#tickets to work as intended

    def on_ticket_select(self,*args):
        selection=(self.get_selected_ticket())
        if not selection:
            return
        ticket=self.tickets[selection]
        samples=ticket["Samples"]
        sample_int_flag=self.samples_integrity_check(samples)
        ticket["Sample Integrity Flag"]=sample_int_flag
        sample_edit_flag=self.samples_integrity_check(samples)
        ticket["Sample Edit Flag"]=sample_edit_flag
        self.parent.sample_check_frame.update_listbox(samples)
        self.parent.ticket_info_frame.update_text(selection,ticket)

    def samples_integrity_check(self, samples):#Checks the ticket for samples that failed the integrity check
        output=True
        for sample in samples:
            if not self.parent.ticket_frame.samples[sample]["Integrity Check"]:
                output="False"
        return output
    
    def samples_edit_check(self, samples):#Checks the ticket for samples that failed the integrity check
        output=True
        for sample in samples:
            if not MainApplication.file_edit_check(self.parent.ticket_frame.samples[sample]['Save Location']):
                output=False
        return output     
           
    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for plate in (selection):
            selected_items.append(self.box.get(plate))
        return selected_items

    def get_selected_ticket(self):
        selection=self.box.get(ANCHOR)
        return selection
    
    def delete_ticket(self):
        ticket=self.get_selected_ticket()
        self.box.delete(ANCHOR)
        self.parent.sample_check_frame.clear_listbox()
        self.parent.plate_display_frame.clear_listbox()
        del(self.tickets[ticket])

class Ticket_Info_Frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Ticket Info", labelanchor="n",font=MainApplication.current_font)
        self.grid(row=1,column=0, sticky="news", padx=(10,0))
        self.populate()
        self.parent=parent

    def populate(self):
        Label(self, text="Ticket Name:",row=0, column=0)
        Label(self, text="Created By:",row=1, column=0)
        Label(self, text="Date Created:",row=2, column=0)
        Label(self, text="Ticket Integrity:",row=3, column=0)
        Label(self, text="Ticket Edit check:",row=4, column=0)
        Label(self, text="Ticket Samples Integrity:",row=5, column=0)
        Label(self, text="Ticket Samples Edit Check:",row=6, column=0)
        self.changing_tname= Label(self, text="Select sample",row=0, column=1)
        self.changing_author= Label(self, text="None:",row=1, column=1)
        self.changing_date= Label(self, text="None",row=2, column=1)
        self.changing_ticheck= Label(self, text="None",row=3, column=1)
        self.changing_techeck= Label(self, text="None",row=4, column=1)
        self.changing_t_samples_ichecks= Label(self, text="None",row=5, column=1)
        self.changing_t_samples_echecks= Label(self, text="None",row=6, column=1)

    def update_text(self, tname, ticket_info):
        self.changing_tname.update(tname)
        date=ticket_info["Ticket Date"]
        author=ticket_info["Author"]
        integrity=str(ticket_info["Sample Integrity Flag"])
        edit_check=str(ticket_info["Sample Edit Flag"])
        self.changing_author.update(author)
        self.changing_date.update(date)
        self.changing_ticheck.update("True")
        self.changing_techeck.update("True")
        self.changing_t_samples_ichecks.update(integrity)
        self.changing_t_samples_echecks.update(edit_check)

class Sample_Check_Frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Sample files", labelanchor="n",font=MainApplication.current_font)
        self.grid(row=0,column=1, sticky="news", padx=(10))
        self.populate()
        self.parent=parent

    def populate(self):
        self.listbox_frame=Frame(self,column=0)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='single')
        self.box.pack(side='left', fill=Y)
        self.box.bind("<<ListboxSelect>>",self.on_sample_select)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)

    def update_listbox(self, samples):
        self.clear_listbox()
        self.display_to_listbox(samples)
    
    def get_selected_sample(self):
        selection=self.box.get(ANCHOR)
        return selection
    
    def on_sample_select(self,*args):
        selection=(self.get_selected_sample())
        if not selection:
            return
        sample=self.parent.ticket_frame.samples[selection]
        sample['Edit Check']=MainApplication.file_edit_check(sample['Save Location'])
        samples=sample["Plates"]
        self.parent.plate_display_frame.update_listbox(samples)
        sample_info=self.parent.ticket_frame.samples[selection]
        self.parent.sample_info_frame.update_text(selection,sample_info)

    def delete_item(self):
        selection=self.box.curselection()
        for plate in reversed(selection):
            self.box.delete(plate)

    def clear_listbox(self):
        self.box.selection_set(0,"end")
        self.delete_item()

    def display_to_listbox(self, content):
        for plate in content:
            self.box.insert(END, plate)

class Sample_Info_Frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Sample Info", labelanchor="n",font=MainApplication.current_font)
        self.grid(row=1,column=1, sticky="news", padx=(10))
        self.populate()
        self.parent=parent

    def populate(self):
        Label(self, text="Sample Name:",row=0, column=0)
        Label(self, text="No Plates:",row=1, column=0)
        Label(self, text="Recount status:",row=2, column=0)
        Label(self, text="Saved at:",row=3, column=0)
        Label(self, text="Sample\nIntegrity Check", row=4, column=0)
        Label(self, text="Sample\nEdit Check", row=5, column=0)
        self.changing_sname= Label(self, text="Select sample",row=0, column=1)
        self.changing_nplates= Label(self, text="None:",row=1, column=1)
        self.changing_recount= Label(self, text="None",row=2, column=1)
        self.changing_destination= Label(self, text="None",row=3, column=1)
        self.changing_icheck=Label(self, text="None",row=4, column=1)
        self.changing_echeck=Label(self, text="None",row=5, column=1)

    def update_text(self, sname, sample_info):
        self.changing_sname.update(sname)
        recount=str(bool(sample_info["Recount"]))
        nplates=sample_info["N Plates"]
        destination=sample_info["Save Location"]
        integrity=str(sample_info["Integrity Check"])
        edit_check=str(sample_info["Sample Edit Flag"])
        self.changing_nplates.update(nplates)
        self.changing_recount.update(recount)
        self.changing_destination.update(destination)
        self.changing_icheck.update(integrity)
        self.changing_echeck.update(edit_check)

class Plate_Display_Frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Plates", labelanchor="nw",font=MainApplication.current_font)
        self.grid(row=0,column=2, sticky="news", padx=(0,10))
        self.populate()
        self.parent=parent

    def populate(self):
        self.listbox_frame=Frame(self,column=0)
        self.box=tk.Listbox(self.listbox_frame, height=12, width=50, selectmode='single')
        self.box.pack(side='left', fill=Y)
        self.box.bind("<<ListboxSelect>>",self.update_text)
        self.scrollbar=tk.Scrollbar(self.listbox_frame, orient=VERTICAL)
        self.scrollbar.config(command=self.box.yview)

    def update_text(self, *args):
        psn=self.read_selection()
        if psn:
            plate_info=self.parent.ticket_frame.plates[(psn[0])]
            self.parent.plate_display_info.update_text(psn,plate_info)

    def update_listbox(self, samples):
        self.clear_listbox()
        self.display_to_listbox(samples)
    
    def read_selection(self):
        selected_items=[]
        selection=self.box.curselection()
        for plate in (selection):
            selected_items.append(self.box.get(plate))
        return selected_items
    
    def delete_item(self):
        selection=self.box.curselection()
        for plate in reversed(selection):
            self.box.delete(plate)

    def clear_listbox(self):
        self.box.selection_set(0,"end")
        self.delete_item()

    def display_to_listbox(self, content):
        for plate in content:
            self.box.insert(END, plate)

class Plate_Info_Frame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Plate Info", labelanchor="n",font=MainApplication.current_font)
        self.grid(row=1,column=2, sticky="news", padx=(0,10))
        self.populate()
        self.parent=parent

    def populate(self):
        Label(self, text="Sample:",row=0, column=0)
        Label(self, text="Final Well:",row=1, column=0)
        Label(self, text="Final Well no:",row=2, column=0)
        Label(self, text="Source:",row=3, column=0)
        self.changing_psn= Label(self, text="Select plate",row=0, column=1)
        self.changing_fwell= Label(self, text="None:",row=1, column=1)
        self.changing_fwellno= Label(self, text="None",row=2, column=1)
        self.changing_source= Label(self, text="None",row=3, column=1)

    def update_text(self, psn, plate_info):
        self.changing_psn.update(psn)
        fwell=plate_info["F Well"]
        fwellno=plate_info["Length"]
        source=plate_info["Source"]
        self.changing_fwell.update(fwell)
        self.changing_fwellno.update(fwellno)
        self.changing_source.update(source)

class Report_Button_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.grid(row=2, column=0, sticky="news", padx=10, pady=10, columnspan=4)
        self.populate()
    
    def populate(self):
        Button(self, text="Check", row=0,column=0, pady=0, padx=(0), width=65, command=self.check)
        Button(self, text="Export", row=0,column=1, pady=0, padx=(0), width=65, command=self.export)

    def check(self):
        for sample in self.parent.ticket_frame.samples:
            data=self.parent.ticket_frame.samples[sample]
            if not data['Integrity Check'] or not data['Sample Edit Flag']:
                messagebox.showwarning(title="Checks Failed", message="One or more samples has failed its checks")
                return
        messagebox.showinfo(title="Checks Passed", message="All checks passed")

    def export(self):
        messagebox.showinfo(title="Information needed", message="While the ability to create some sort of report has been suggested I am afraid that I do not know what should go in it, please feel free to look at the information that appears on this screen or at the ticket files themselves and judge whether you think they have")

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
    app = MainApplication("Importer and Checker Working Copy","Company_logo.ico")
    app.mainloop()
