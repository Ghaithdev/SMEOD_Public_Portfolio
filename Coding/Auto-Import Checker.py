import tkinter as tk#Tkinter is the module that allows the GUI to exist
from tkinter import ttk#Tkinter is the module that allows the GUI to exist
from tkinter import messagebox#Tkinter is the module that allows the GUI to exist
from tkinter import filedialog#Tkinter is the module that allows the GUI to exist
import tkinter.font as font#Tkinter is the module that allows the GUI to exist
from tkinter import *#Tkinter is the module that allows the GUI to exist
import re #Imports Regex expression compatibility

#this is where the boxes that contain the form's fields can be found
mainroot=tk.Tk()#creates a window
mainroot.iconbitmap("Pharmaron_logo.ico")#Put pharmaron logo as icon for app
mainroot.title("Splicing Tool Version 02.00")#Titlebar title set
tk.messagebox.showinfo(title="User Info", message="Please report any issues in an email to:\nJack.Johnston@pharmaron-uk.com")#gives message to user

frame=tk.Frame(mainroot)
frame.pack(pady=(10,0))


"""The below frame contains the information about the splices and their position.
It is subdivided with the second section showing all the buttons in the frame"""
splice_frame=tk.LabelFrame(frame,text="Available Plates",labelanchor="n")
splice_frame.grid(row=0,column=0, padx=(10), pady=(10),sticky="nesw")
available_listbox_frame=Frame(splice_frame)
available_listbox_frame.grid(row=0,column=1,rowspan=4)
listbox_scrollbar=Scrollbar(available_listbox_frame, orient=VERTICAL)#scrollbr for associated listbox and the command that allows it control of the yview
available_listbox=tk.Listbox(available_listbox_frame,height=12, width=50, selectmode='multiple', yscrollcommand=listbox_scrollbar.set)#this is the listbox
listbox_scrollbar.config(command=available_listbox.yview)#scrollbr for associated listbox and the command that allows it control of the yview
listbox_scrollbar.pack(side=RIGHT, fill=Y)#scrollbr for associated listbox and the command that allows it control of the yview
available_listbox.pack(fill=Y)

base_browse_but=Button(splice_frame, text="Add Base Sequence", command=None)#add base button
base_browse_but.grid(row=0,column=0, padx=(5),sticky="news")
splice_add_but=Button(splice_frame, text="Add Splice Plate(s)",  command=None)#add splice button
splice_add_but.grid(row=1, column=0,padx=(5), sticky="news")
edit_plate_but=Button(splice_frame, text="Edit plate", width = 5, command=None)#available edit button
edit_plate_but.grid(row=2, column=0,padx=(5), sticky="news")
del_plate_but=Button(splice_frame, text="Delete plate", width = 5, command=None)#delete plate button
del_plate_but.grid(row=3, column=0,padx=(5), sticky="news")

"""The folowing frame contains the buttons to move an assay from the available
listbox to the used listbox"""
migrate_frame=tk.Frame(frame)
migrate_frame.grid(row=0,column=1, pady=(10),sticky="nesw")#move left/right buttons
final_browse_but=Button(migrate_frame, text="→", command=None)#move left/right buttons
final_browse_but.grid(row=0,column=0,pady=(75,0), padx=(5),sticky="news")#move left/right buttons
final_browse_but=Button(migrate_frame, text="←", command=None)#move left/right buttons
final_browse_but.grid(row=1,column=0,pady=(5), padx=(5),sticky="news")


"""The below frame contains the information about the splices and their position.
It is subdivided with the second section showing all the buttons in the frame"""
final_frame=tk.LabelFrame(frame,text="Final",labelanchor="n")
final_frame.grid(row=0,column=2, padx=(10), pady=(10),sticky="nesw")
final_listbox_frame=Frame(final_frame)
final_listbox_frame.grid(row=0,column=0,rowspan=4)
final_listbox_scrollbar=Scrollbar(final_listbox_frame, orient=VERTICAL)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox=tk.Listbox(final_listbox_frame,height=12, width=50, selectmode='multiple', yscrollcommand=listbox_scrollbar.set)#this is the listbox
final_listbox_scrollbar.config(command=final_listbox.yview)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox_scrollbar.pack(side=RIGHT, fill=Y)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox.pack(fill=Y)

final_browse_but=Button(final_frame, text="↑", command=None)#move up/down button
final_browse_but.grid(row=0,column=1, padx=(5),sticky="news")
final_add_but=Button(final_frame, text="↓",  command=None)#move up/down button
final_add_but.grid(row=1, column=1,padx=(5), sticky="news")
final_edit_but=Button(final_frame, text="Edit plate", width = 12, command=None)#final edit button
final_edit_but.grid(row=2, column=1,padx=(5), sticky="news")
final_del_but=Button(final_frame, text="Delete plate", width = 12, command=None)#final delete button
final_del_but.grid(row=3, column=1,padx=(5), sticky="news")

"""The below frame is the one that contains all the onscreen checksums"""
checks_frame=tk.LabelFrame(frame,text="Checklist",labelanchor="n")
checks_frame.grid(row=1,column=0, columnspan=2, padx=(10), pady=(10),sticky="nesw")

filename_frame=tk.LabelFrame(checks_frame,text="File names",labelanchor="n")
filename_frame.grid(row=0,column=0,padx=(10), pady=(0,10),sticky="nesw")
base_check_var = tk.IntVar()#these allow the app to read if the tickbox is checked
base_filename_check_lab=tk.Label(filename_frame, text="Base file match:")
base_filename_check_lab.grid(row=0,column=0)
splice_check_var= tk.IntVar()#these allow the app to read if the tickbox is checked
spliced_filename_lab=tk.Label(filename_frame, text="Splice files match:")
spliced_filename_lab.grid(row=1,column=0)
base_filename_checkbox=tk.Checkbutton(filename_frame, variable=base_check_var)#checkbutton (tickbox) it controls the associated IntVar
base_filename_checkbox.grid(row=0,column=1)
splice_filename_check=tk.Checkbutton(filename_frame, variable=splice_check_var)#checkbutton (tickbox) it controls the associated IntVar
splice_filename_check.grid(row=1,column=1)

filelen_frame=tk.LabelFrame(checks_frame,text="Sequence lengths",labelanchor="n")
filelen_frame.grid(row=0,column=1, padx=(0,10), pady=(0,10),sticky="nesw")
orig_len_lab_fixed=tk.Label(filelen_frame, text="Original:")
orig_len_lab_fixed.grid(row=0,column=0)
orig_len_lab=tk.Label(filelen_frame, text="No file selected")#displays the length of the base/spliced sequence
orig_len_lab.grid(row=0,column=1)
spliced_len_lab_fixed=tk.Label(filelen_frame, text="Spliced:")
spliced_len_lab_fixed.grid(row=1,column=0)
spliced_len_lab=tk.Label(filelen_frame, text="No file selected")#displays the length of the base/spliced sequence
spliced_len_lab.grid(row=1,column=1)
update_button=Button(filelen_frame, text="Update", command=None)#updates the length of the spliced sequence. in theory this button won't do anything as the value updates automatically
update_button.grid(row=2,column=0,columnspan=2, sticky='news')

order_frame=tk.LabelFrame(checks_frame,text="Order & Length",labelanchor="n")
order_frame.grid(row=0,column=2,padx=(0,10), pady=(0,10),sticky="nesw")
order_check_var = tk.IntVar()#these allow the app to read if the tickbox is checked
file_order_check_lab=tk.Label(order_frame, text="File order checked:")
file_order_check_lab.grid(row=0,column=0)
len_check_var= tk.IntVar()#these allow the app to read if the tickbox is checked
length_check_lab=tk.Label(order_frame, text="Sequence lengths checked:")
length_check_lab.grid(row=1,column=0)
file_order_checkbox=tk.Checkbutton(order_frame, variable=order_check_var)#checkbutton (tickbox) it controls the associated IntVar
file_order_checkbox.grid(row=0,column=1)
length_checkbox=tk.Checkbutton(order_frame, variable=len_check_var)#checkbutton (tickbox) it controls the associated IntVar
length_checkbox.grid(row=1,column=1)

#Button frame on bottom of screen
Button_frame=tk.Frame(frame)
Button_frame.grid(row=3,column=0, columnspan=3, sticky="nesw")

checkbut=Button(Button_frame, text="Check Values", command=None)#check button
checkbut.pack(side=LEFT,fill="both",expand=1)
#This is the code for the button that clears all fields in Sequence_info_frame
clear_a_but=Button(Button_frame, text="Clear Values", command=None)#clear button
clear_a_but.pack(side=RIGHT,fill="both",expand=1)

#This is the button that allows the user to submit all entries
submit_but=Button(mainroot, text="Submit", command=None)#submit button
submit_but.pack(side=BOTTOM,fill="both",expand=1)

splice_add_but.grid(row=1, column=0,padx=(5), sticky="news")
edit_plate_but=Button(splice_frame, text="Edit plate", width = 5, command=None)#available edit button
edit_plate_but.grid(row=2, column=0,padx=(5), sticky="news")
del_plate_but=Button(splice_frame, text="Delete plate", width = 5, command=None)#delete plate button
del_plate_but.grid(row=3, column=0,padx=(5), sticky="news")

"""The folowing frame contains the buttons to move an assay from the available
listbox to the used listbox"""
migrate_frame=tk.Frame(frame)
migrate_frame.grid(row=0,column=1, pady=(10),sticky="nesw")#move left/right buttons
final_browse_but=Button(migrate_frame, text="→", command=None)#move left/right buttons
final_browse_but.grid(row=0,column=0,pady=(75,0), padx=(5),sticky="news")#move left/right buttons
final_browse_but=Button(migrate_frame, text="←", command=None)#move left/right buttons
final_browse_but.grid(row=1,column=0,pady=(5), padx=(5),sticky="news")


"""The below frame contains the information about the splices and their position.
It is subdivided with the second section showing all the buttons in the frame"""
final_frame=tk.LabelFrame(frame,text="Final",labelanchor="n")
final_frame.grid(row=0,column=2, padx=(10), pady=(10),sticky="nesw")
final_listbox_frame=Frame(final_frame)
final_listbox_frame.grid(row=0,column=0,rowspan=4)
final_listbox_scrollbar=Scrollbar(final_listbox_frame, orient=VERTICAL)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox=tk.Listbox(final_listbox_frame,height=12, width=50, selectmode='multiple', yscrollcommand=listbox_scrollbar.set)#this is the listbox
final_listbox_scrollbar.config(command=final_listbox.yview)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox_scrollbar.pack(side=RIGHT, fill=Y)#scrollbr for associated listbox and the command that allows it control of the yview
final_listbox.pack(fill=Y)

final_browse_but=Button(final_frame, text="↑", command=None)#move up/down button
final_browse_but.grid(row=0,column=1, padx=(5),sticky="news")
final_add_but=Button(final_frame, text="↓",  command=None)#move up/down button
final_add_but.grid(row=1, column=1,padx=(5), sticky="news")
final_edit_but=Button(final_frame, text="Edit plate", width = 12, command=None)#final edit button
final_edit_but.grid(row=2, column=1,padx=(5), sticky="news")
final_del_but=Button(final_frame, text="Delete plate", width = 12, command=None)#final delete button
final_del_but.grid(row=3, column=1,padx=(5), sticky="news")

#Button frame on bottom of screen
Button_frame=tk.Frame(frame)
Button_frame.grid(row=3,column=0, columnspan=3, sticky="nesw")

checkbut=Button(Button_frame, text="Check Values", command=None)#check button
checkbut.pack(side=LEFT,fill="both",expand=1)
#This is the code for the button that clears all fields in Sequence_info_frame
clear_a_but=Button(Button_frame, text="Clear Values", command=None)#clear button
clear_a_but.pack(side=RIGHT,fill="both",expand=1)

#This is the button that allows the user to submit all entries
submit_but=Button(mainroot, text="Submit", command=None)#submit button
submit_but.pack(side=BOTTOM,fill="both",expand=1)

mainroot.mainloop()#this makes window persistent