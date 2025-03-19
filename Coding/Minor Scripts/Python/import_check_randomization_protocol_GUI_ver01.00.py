#Lines starting with a '#' are comments and thus not read 
#Text placed in triple speech marks like so '"""text"""' are also comments

"""
You can ignore the first comment if you're familiar with python, I put that
not knowing if this code would have to be read by people not literate in it
"""

"""
This text contains the python code that runs the program to randomize which wells
are checked for the QC import checking process. Literally saving this text document as a
.py file would allow it to run in python. It should be noted that the layout of
the document, including new lines and other white space characters
is actually an important part of how it functions and thus should be left as is
when auditing. The program is hopefully to be converted to a .exe file and hosted
in a read only drive in the network
"""

"""The below imports are the various modules required to run the code,
they will be included in the compoiled version of the program with no issue"""
import tkinter as tk    #these modules are to do with the graphic user interface
from tkinter import ttk     #these modules are to do with the graphic user interface
from tkinter import filedialog  #these modules are to do with the graphic user interface
from tkinter import *   #these modules are to do with the graphic user interface
from datetime import datetime,timezone  #these modules allow python to read the date and time, they are important to the randomization
import random as rnd    #THis is the library containing the pseudo random algorithm
#This are  predefined lists items and dictionaries required to run this script
now_out = datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')
now_inp = datetime.now(timezone.utc).timestamp()#This gives the time of opening the app as a single number
C2N={}#Conversion chart for plate corrd to well number ie A12 => 96
N2C={}#Conversion table in opposite direction filled in later
plate_table=[]
sequence=[]
sorted_plates=[]
output=[]
seedconv=()
seedout=(0x1)#This is how the seed will be displayed to the user
check_token_A=False#These check tokens allow the app to readily check that certain things have been done, check token b no longer exists
check_token_C=False#These check tokens allow the app to readily check that certain things have been done, check token b no longer exists
platesamples=3#this is the default value for samples per plate
textbox_w=60#The width (in characters) of the textbox in the output window
wells_per_plate=96#The default value of number of wells on a plate

#Below are all the functions defined for this script

"""
The below functions are thase that are called within the randomization
settings frame
"""

#This function inputs a new seed into the program and feeds it to the interface
def seedin(seed):#Seed is a variable pulled from the seedin bar
    global seedout #this makes sure that the seedout is rewritten
    global check_token_C#the check tokens are hidden variables that the program uses to check that a variable has been set
    if radio_selected.get() == 0:#This branch generates a randomized seed
        seedconv=None
        now_inp = datetime.now(timezone.utc).timestamp()
        rnd.seed(now_inp)#this step is to prevent seeds feeding into the selection of the next randomly generated seed
        RNG=rnd.randint(0, 4294967295)
        rnd.seed(RNG)
        seedout=str(hex(RNG))
        check_token_C=True
        seed_lab.config(text=seedout)
    elif radio_selected.get() == 1:#This branch inputs a given seed into the program
        seedconv=None
        try:
            seedconv=int(seed, base=16)
            rnd.seed(seedconv)
            seedout=str(seed)
            check_token_C=True
            seed_lab.config(text=seedout)
        except:
            tk.messagebox.showerror(title="Seed Error", message=("Invalid Seed"))
    else:
        tk.messagebox.showwarning(title="Catastrophic Error", message="I know what this error is but you need to record what you did to show me how you got it\nRadio group issue")

"""
This function reads the radio group in the the random settings frame and
enables and disables entry widgets accordingly
"""
def onRadioButtonChange(*args):#this allows the changes that occur on switching the staurs of the radio group within the window
    if radio_selected.get() == 0:               #This is the setting for a randomized seed
        seed_in.configure(state = tk.DISABLED)
        seed_bar.configure(state = tk.DISABLED)
        use_seed_but.configure(state = tk.NORMAL)
    else:                                        #This is the setting for a selected seed
        seed_in.configure(state = tk.NORMAL)
        seed_bar.configure(state = tk.NORMAL)
        use_seed_but.configure(state = tk.DISABLED)

#The below functions are those that are used by the "Other settings" frame

"""The two functions below define lists used for coordinates on a plate,
it is called on startup and whenever the user manually changes the direction,
the variable direction is determined by the button the user clicks"""

"""This is the non-standard custom direction change the likely use case is if the
plates used did not have 96 wells but it can also be used if the program cannot find
the plate map files to direct them to them"""
def customdirchange():
    mainroot.filename =filedialog.askopenfilename(initialdir="/", title='Select a file', filetypes=(("Text files","*.txt"),("All files","*.*")))
    direction_change(mainroot.filename)
#This is the version used by the more standard vertical and horizontal buttons
def direction_change(direction):
    try:
        C2N.clear()
        N2C.clear()
        plate_table.clear()
        sorted_plates.clear()
        position=0
        with open(direction) as dir_mode:#Reads the direction file 
            for line in dir_mode:
                position+=1
                coord=line.strip()
                C2N[coord]=position
                N2C[position]=coord
                plate_table.append(coord)
        for item in sorted(plate_table):
            sorted_plates.append(item)
        terminus_combobox.configure(values=plate_table)
        tk.messagebox.showinfo(title="Direction Change", message=(f"Snake Direction altered using: {direction}"))
    except(FileNotFoundError):
        tk.messagebox.showerror(title="File not recognized",message="Invalid file name entered")

#This function allows the user to access the advanced settings window
def advset():
    global adv_set_win
    adv_set_win=Toplevel()
    adv_set_win.iconbitmap("Pharmaron_logo.ico")
    adv_set_win.title("Advanced settings")
    randoframe=tk.LabelFrame(adv_set_win,text="Randomization Settings")
    randoframe.pack(side='top',fill="both",expand=1)
    spp_lab=tk.Label(randoframe, text="Samples per plate")
    spp_lab.grid(row=0,column=0)
    spp_bar=tk.Entry(randoframe)
    spp_bar.grid(row=0,column=1)
    cur_spp_lab=tk.Label(randoframe, text="Current SPP:")
    cur_spp_lab.grid(row=1,column=0)
    cur_spp=tk.Label(randoframe, text=platesamples)
    cur_spp.grid(row=1,column=1)
    def change_spp():
        global platesamples
        try:
            spp=spp_bar.get()
            spp=int(spp)
            if spp<1:
                raise ValueError
        except(ValueError):
            errormsg=("Invalid input")
            tk.messagebox.showerror(title="Invalid input", message=errormsg)
            return
        else:
            platesamples=int(spp_bar.get())
            cur_spp.config(text=platesamples)
            disp_cur_spp.config(text=platesamples)
    spp_but=Button(randoframe, text="Submit", command=change_spp)
    spp_but.grid(row=0,column=2)

    plate_frame=tk.LabelFrame(adv_set_win,text="Plate Settings")
    plate_frame.pack(side='bottom',fill="both",expand=1)
    wpp_lab=tk.Label(plate_frame, text="Wells per plate")
    wpp_lab.grid(row=0,column=0)
    wpp_bar=tk.Entry(plate_frame)
    wpp_bar.grid(row=0,column=1)
    cur_wpp_lab=tk.Label(plate_frame, text="Current WPP:")
    cur_wpp_lab.grid(row=1,column=0)
    cur_wpp=tk.Label(plate_frame, text=wells_per_plate)
    cur_wpp.grid(row=1,column=1)
    cust_but=Button(plate_frame, text="Custom directon", command=customdirchange)
    cust_but.grid(row=2, column=0, columnspan=3, sticky='news')
    def change_wpp():
        global wells_per_plate
        try:
            wpp=wpp_bar.get()
            wpp=int(wpp)
            if wpp<1:
                int("HAL9000")
            wells_per_plate=int(wpp_bar.get())
            cur_wpp.config(text=wells_per_plate)
            tk.messagebox.showwarning(title="Custom direction required", message="You must use a custom direction for plates of <96 wells")
        except:
            errormsg=(f"I'm sorry, {user}. I'm afraid I can't do that")
            tk.messagebox.showerror(title="HAL", message=errormsg)
            return
    wpp_but=Button(plate_frame, text="Submit", command=change_wpp)
    wpp_but.grid(row=0,column=2,sticky='news')

def font_window():
    font_win=Toplevel()
    font_win.iconbitmap("Pharmaron_logo.ico")
    font_win.title("Font adjust")

def calculator():
    global calc_win
    """This section is all for the the window that uses the number of wells and the run time to calculate the fraction time,
    final well position and the number of plates in the sample"""
    calc_win=Toplevel()
    calc_win.iconbitmap("Pharmaron_logo.ico")
    calc_win.title("Calculator")
    calc_notebook=ttk.Notebook(calc_win)
    calc_notebook.pack()

    nwell_RT_to_FT=Frame(calc_win)
    nwell_RT_to_FT.pack(fill="both",expand=1)
    calc_notebook.add(nwell_RT_to_FT, text="Nwells & RT => FT & FPos")
    input_frame1=LabelFrame(nwell_RT_to_FT, text="Inputs")
    input_frame1.pack(side=TOP,fill="both",expand=1)

    n_well_calc_in_lab=tk.Label(input_frame1, text="Number\nof Wells:")
    n_well_calc_in_lab.grid(row=0,column=0)
    n_well_calc_in_bar=tk.Spinbox(input_frame1, from_=0,to=1000,increment=24)
    n_well_calc_in_bar.grid(row=0,column=1)
    #this is the Final well spinbox and the label for it, the first two lines set the default
    run_time_inp_lab=tk.Label(input_frame1, text="Run Time")
    run_time_inp_bar=tk.Spinbox(input_frame1, from_=20,to=200,increment=5)
    run_time_inp_lab.grid(row=1,column=0)
    run_time_inp_bar.grid(row=1,column=1)
    #This is the number of plates textvariable
    calc_reset_but1=Button(input_frame1, text="Reset", command=None)
    calc_reset_but1.grid(row=1,column=2, columnspan=2, sticky="news")
    def calc_nwell_RT_to_FT():
        try:
            int(n_well_calc_in_bar.get())
        except:
            tk.messagebox.showerror(title="Invalid number of wells", message="Please enter a valid value")
        try:
            float(run_time_inp_bar.get())
        except:
            tk.messagebox.showerror(title="Invalid run time", message="Please enter a valid value")
        nw_calc_inp=int(n_well_calc_in_bar.get())
        if nw_calc_inp <= 0:
            tk.messagebox.showerror(title="Zero divide error", message="Cannot have zero wells on a plate")
            return()
        RT_calc_inp=int(run_time_inp_bar.get())*60
        terminus_calc_out=int(n_well_calc_in_bar.get())%wells_per_plate+(int(n_well_calc_in_bar.get())%wells_per_plate==0)*wells_per_plate
        FT_calc_out=(((RT_calc_inp)/nw_calc_inp)/60)*60
        PPS_calc_out=round((nw_calc_inp/96)+0.5)
        plateno_calc_out_entry.delete(0,END)
        plateno_calc_out_entry.insert(0,PPS_calc_out)
        terminus_calc_out_entry.delete(0,END)
        terminus_calc_out_entry.insert(0,N2C[terminus_calc_out])
        ft_entry_clac_out.delete(0,END)
        ft_entry_clac_out.insert(0,FT_calc_out)
    calc_sub_but1=Button(input_frame1, text="Submit", command=calc_nwell_RT_to_FT)
    calc_sub_but1.grid(row=0,column=2, columnspan=2,sticky="news")

    output_frame1=LabelFrame(nwell_RT_to_FT, text="Output")
    output_frame1.pack(side=BOTTOM,fill="both",expand=1)

    plateno_calc_out_lab=tk.Label(output_frame1, text="Plates/\nsample:")
    plateno_calc_out_lab.grid(row=0,column=0)
    plateno_calc_out_entry=tk.Entry(output_frame1)
    plateno_calc_out_entry.grid(row=0,column=1)
    
    terminus_lab_out=tk.Label(output_frame1, text="Final well")
    terminus_calc_out_entry=tk.Entry(output_frame1)
    terminus_lab_out.grid(row=0,column=2)
    terminus_calc_out_entry.grid(row=0,column=3)

    ft_lab=tk.Label(output_frame1, text="Fraction Time")
    ft_entry_clac_out=tk.Entry(output_frame1)
    ft_lab.grid(row=1,column=0)
    ft_entry_clac_out.grid(row=1,column=1)
    

"""
The below functions are the ones that are placed toward the bottom of the
main frame, they are the Check and clear functions and are called by their
respective buttons. The former is also called by the submit button. They
don't call other functions but they do call variables from within the program
including the check tokens
"""
def check():
    global check_token_A
    global check_token_C
    try:
        FT=ft_spinbox.get()
        FT=float(FT)
        if FT <0:
            #This if statement is literally designed to cause the 'try' to fail
            #if the number is outside the proper range so that the except
            #condition returns instead
            float("Crash")
    except:
        check_token_A=False
        tk.messagebox.showerror(title="Invalid fraction time", message="Fraction time must be a number")
        return
    try:
        PN=plateno_spinbox.get()
        PN=int(PN)
        if PN <1 or PN>20:
            #This if statement is literally designed to cause the 'try' to fail
            #if the number is outside the proper range so that the except
            #condition returns instead
            int("Crash")
    except:
        check_token_A=False
        tk.messagebox.showerror(title="Invalid Number of plates", message="Number of Plates must be an integer between 1 and 15")
        return
    terminus=terminus_combobox.get().capitalize()
    if terminus in sorted_plates:
        check_token_A=True
    else:
        tk.messagebox.showerror(title="Invalid Final Well Position",message="Final well position not recognized")
        check_token_A=False
        return
    tk.messagebox.showinfo(title="Validation Complete", message="Sequence info values are all valid")
    if check_token_C == False:
        tk.messagebox.showerror(title="Error: Validation Required", message="You must generate or enter a new seed")
        return
    else:
        tk.messagebox.showinfo(title="Validation Complete", message="Seed input valid")

def clear_a():#Function clears all the input fields
    global check_token_C
    terminus_combobox.delete(0,END)
    nsample_bar.delete(0,END)
    nsample_bar.insert(0,1)
    ft_spinbox.delete(0,END)
    ft_spinbox.insert(0,10.00)
    plateno_spinbox.delete(0,END)
    plateno_spinbox.insert(0,5)
    seed_lab.config(text="New seed required")
    check_token_C=False

"""
The functions below are all those that are activated after the user clicks
the submit button, some of the fucntions are those that are required for the
results window to work
"""

"""
This function allows a user to submit the form, it calls the check, gen_results
and give_user functions. It is called by the submit button
"""
def subform():
    global check_token_A
    global check_token_C
    check()
    if check_token_A is True and check_token_C is True:
        global output
        output=[]
        genresults()
        give_user()
        seed_lab.config(text="New seed required")
        check_token_C=False
    else:
        tk.messagebox.showwarning(title="Error: Validation Required", message="Required information is missing")
"""
This function generates the results that are to be fed to the end user.
It is called by the sub form function, the output variable it creates is called
by the populate function
"""
def genresults():
    global output #This output is called by the populate function
    global textbox_w
    allplate=int(plateno_spinbox.get())
    plate=allplate-1
    terminus=terminus_combobox.get().capitalize()
    pos=C2N[terminus]
    seqlen=plate*wells_per_plate+pos
    FT=float(ft_spinbox.get())
    opening=(f"Check that the result at each FT matches the one at the matching coordinate of the correct plate.\nThe number of plates in all samples was:  {allplate}\nThe final well position for all samples was:  {terminus}")#for some reason rather than cause the seed to be at the top of the output this causes it to sandwich the document and appear at the bottom, this was thought to be a somewhat desirable outcome so no effort was made to change this
    output.append(opening)
    output.append("The output format is as follows:\n")
    sep=(("~"*textbox_w)+"\n")
    output.append(sep)
    output.append("Sample #:\n")
    output.append("FT:#         P:#          X#\n")
    output.append(sep)
    output.append("Where any '#' represents some digit, FT is the fraction time, P is the plate & X# is the coordinate in the plate\n")
    output.append(sep)
    for i in range(int(nsample_bar.get())):
        seqintro=(f"The seed used for sample {str(i+1)} was:  {seedout}")
        output.append(seqintro)
        slist=list()
        n=0
        while True:
            if pos+1<platesamples:
                tk.messagebox.showerror(title="Sampling Error", message=("""The number of samples requested is higher than the number of wells in one of the sample's
                plates, results not generated""")) 
                break
            if n < plate:
                temp=(rnd.sample(range(n*wells_per_plate+1,(n+1)*wells_per_plate+1),platesamples))#This means that the program takes a number of random samples equal to the plate samples variable from the range (the range is the first position on a given plate to the last)
                for i in temp:
                    slist.append(i)
                n+=1
                continue
            if n == plate:
                temp=(rnd.sample(range(n*wells_per_plate+1,n*wells_per_plate+pos+1),platesamples))#This means that the program takes a number of random samples equal to the plate samples variable from the range (the range is the first position on the final plate to the final)
                for i in temp:
                    slist.append(i)
                n+=1
            if n>plate:#this stops the program from trying to sample plates from positions after the end of the sequence
                n=0
                break
        slist.sort()
        for item in slist:
            FTSample=round((FT)*(float(item)-1)/60,2)
            plateno=int(item/wells_per_plate+(item%wells_per_plate>0))
            platepo=item%wells_per_plate+(item%wells_per_plate==0)*wells_per_plate
            X0=N2C[platepo]
            readout_slist=str(f"FT: {str(FTSample).zfill(6)}        P:{str(plateno)}        {str(X0)}\n")
            output.append(readout_slist)
    sequence_time=(seqlen*FT)/60
    sequence_time_output=(f"Your sequences should be approximately {str(sequence_time)} minutes long and  exactly {seqlen} wells long\n")

    output.append(sequence_time_output)
"""
This function creates and displays the second window to the screen, it then
calls the populate function. It is called by the subform
"""
def give_user():
    global win2
    win2=Toplevel()#These create a second window
    win2.iconbitmap("Pharmaron_logo.ico")#This gives the second window the Pharmaron logo as an icon the app will fail if the .ico is not in the same directory
    win2.title("Randomization procedure for QC")#These create a second window
    r_click_menu=Menu(win2, tearoff=False)#these commands allow the second window to have a right click window
    r_click_menu.add_command(label= "Copy (Ctrl + C)", command=copy_all)#these commands allow the second window to have a right click window
    r_click_menu.add_separator()#these commands allow the second window to have a right click window
    r_click_menu.add_command(label= "Exit Window",command=exit_window)#these commands allow the second window to have a right click window
    def popup_menu(e):
        r_click_menu.tk_popup(e.x_root,e.y_root)
    win2.bind("<Button-3>", popup_menu)
    global read_me
    global textbox_w
    read_me=Text(win2, width=textbox_w, height=15, font=("Calibri",16))
    read_me.pack(pady=(20,0))
    bframe=Frame(win2)
    bframe.pack()
    populate()
    copy_all_but=Button(bframe, text="Copy to clipboard",command=copy_all,width=15)
    copy_all_but.grid(row=0,column=0)
    reset_but=Button(bframe, text="Reset", command=populate, width=15)
    reset_but.grid(row=0,column=1)
    exit_but=Button(bframe, text="Exit window", command=exit_window, width=15)
    exit_but.grid(row=0,column=2)
"""
The below fucntion is the one that allows the output of the textbox "read_me"
to be copied using the copy all button, it does not currently work, it is called
by the copy all to clipboard button
"""
def copy_all():
    global read_me
    txt_out=read_me.get(1.0,END)
    mainroot.clipboard_clear()
    mainroot.clipboard_append(txt_out)
"""
This function populates the textbox that with the results generated by the
genresults function, it is called by the submit button and the reset button
"""
def populate():
    global output
    global read_me
    read_me.delete(1.0,END)
    n=1.0
    for item in output:
        read_me.insert(n,item)
        n=n+1
"""
This function exits the second window of the program it is called by the exit
window button
"""
def exit_window():
    global win2
    win2.destroy()


"""
This is the main window in which other parts appear, the code configures the
title, size and colour
"""
mainroot=tk.Tk()
mainroot.iconbitmap("Pharmaron_logo.ico")
mainroot.title("Randomization tool for import check")

#this is where the boxes that contain the form's fields can be found
frame=tk.Frame(mainroot)
frame.pack(pady=(10,0))

tk.messagebox.showinfo(title="User Info", message="Please report any issues in an email to:\nJack.Johnston@pharmaron-uk.com")
"""
Objects in Sequence_info_frame are those that are expected to be entered only
once about the sequence
"""
Sequence_info_frame=tk.LabelFrame(frame,text="Sequence info",labelanchor="n")
Sequence_info_frame.grid(row=0,column=0, columnspan=3, sticky="nesw")
#this is the username field and the label for it
nsample_lab=tk.Label(Sequence_info_frame, text="Number\nof samples:")
nsample_lab.grid(row=0,column=0)
nsample_bar=tk.Spinbox(Sequence_info_frame, from_=1,to=6,increment=1,state="disabled")
nsample_bar.grid(row=0,column=1)
#this is the Final well dropdown and the label for it
terminus_lab=tk.Label(Sequence_info_frame, text="Final well")
terminus_combobox=ttk.Combobox(Sequence_info_frame,values=sorted_plates)
terminus_lab.grid(row=1,column=3)
terminus_combobox.grid(row=1,column=4)
#this is the Final well spinbox and the label for it, the first two lines set the default
FTvar = StringVar(Sequence_info_frame)
FTvar.set(str(10.00))
ft_lab=tk.Label(Sequence_info_frame, text="Fraction Time")
ft_spinbox=tk.Spinbox(Sequence_info_frame, from_=6.00,to=15.00,increment=0.01, textvariable=FTvar)
ft_lab.grid(row=1,column=0)
ft_spinbox.grid(row=1,column=1)
#This is the number of plates textvariable
plateno_lab=tk.Label(Sequence_info_frame, text="Plates/\nsample")
plateno_spinbox=tk.Spinbox(Sequence_info_frame, from_=1,to=20)
plateno_lab.grid(row=0,column=3)
plateno_spinbox.grid(row=0,column=4)

# this section pads all the widgets in the frame a window
for widget in Sequence_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady=5)

#This frame contains some important settings for how the program generates results
Randomization_settings_frame=tk.LabelFrame(frame,text="Randomization settings",labelanchor="n")
Randomization_settings_frame.grid(row=1,column=0, pady=(10,10),sticky="nesw")
"""
The below section is for a radio group that a user must assign to determine if
they wish to use a randomized seed or not
"""
rlab=tk.Label(Randomization_settings_frame, text="Use random seed?")
rlab.grid(row=0,column=0,columnspan=2)
radio_selected = tk.IntVar()
radio_selected.set(0)
r1 = ttk.Radiobutton(Randomization_settings_frame, text='Random', value=0, variable=radio_selected)
r2 = ttk.Radiobutton(Randomization_settings_frame, text='Set Seed', value=1, variable=radio_selected)
r1.grid(row=1,column=0)
r2.grid(row=1,column=1)
#This line means that a command is called when the radio grouup is changed
radio_selected.trace_add('write', onRadioButtonChange)
#This is the input field where the user enters their fixed seed if using one
en_seed_lab=tk.Label(Randomization_settings_frame, text="Enter seed:")
en_seed_lab.grid(row=2,column=0)
seed_bar=tk.Entry(Randomization_settings_frame,state="disabled")
seed_bar.grid(row=2,column=1)
#This is the button that allows the user to enter a manual seed
"""
Button commands cannot normally parse an object thus to make a button parse
an object a lambda function is necessary
"""
seed_in=Button(Randomization_settings_frame, text="Enter seed",state='disabled',width=12, command=lambda: seedin(seed_bar.get()))
seed_in.grid(row=2, column=2)

#This is the button that allows the user to enter a manual seed
seed_lab_static=tk.Label(Randomization_settings_frame, text="Current seed:")
seed_lab_static.grid(row=3,column=0)
#Button commands cannot normally parse an object thus to make a button parse an object a lambda function is necessary
use_seed_but=Button(Randomization_settings_frame, text="Generate Seed", state='normal', width=12, command=lambda: seedin(seed_bar.get()))
use_seed_but.grid(row=3, column=2, pady=(5,0))
seed_lab=tk.Label(Randomization_settings_frame, text="No seed assigned")
seed_lab.grid(row=3,column=1)
#These widgets display the number of samples per plate taken
disp_cur_spp_lab=tk.Label(Randomization_settings_frame, text="Current\nSamples/Plate:")
disp_cur_spp_lab.grid(row=4,column=0)
disp_cur_spp=tk.Label(Randomization_settings_frame, text=platesamples)
disp_cur_spp.grid(row=4,column=1)

#This frame contains some important settings for how the program generates results
Other_settings_frame=tk.LabelFrame(frame,text="Other settings",labelanchor="n")
Other_settings_frame.grid(row=1,column=1, padx=(10), pady=(10,10),sticky="news")
#This is the label frame that contians the direction control buttons
direction_labframe=tk.LabelFrame(Other_settings_frame,text="Snake Direction",labelanchor="n",)
direction_labframe.grid(row=0,column=0,columnspan=2,pady=(0,10),padx=10,sticky="news")
"""
Button commands cannot normally parse an object thus to make a button parse
an object a lambda function is necessary
"""
horizbut=Button(direction_labframe, text="Horizontal", width=8, command=lambda: direction_change("Lookup_Horiz_document.txt"))
horizbut.grid(row=0, column=0)
"""
Button commands cannot normally parse an object thus to make a button parse
an object a lambda function is necessary
"""
vertbut=Button(direction_labframe, text="Vertical", width=8, command=lambda: direction_change("Lookup_Vert_document.txt"))
vertbut.grid(row=0, column=1)
#This is the label frame that contians the direction control buttons
view_labframe=tk.LabelFrame(Other_settings_frame,text="View Settings",labelanchor="n")
view_labframe.grid(row=1,column=0,columnspan=2,pady=(0,10),padx=10,sticky="news")
font_but=Button(view_labframe, text="Change Font",state='disabled', command=font_window)
font_but.pack(side=TOP,fill="both",expand=1)
tog_but=Button(view_labframe, text="Toggle Night Mode", state='disabled')
tog_but.pack(side=BOTTOM,fill="both",expand=1)

#This is the advanced settings button
advset=Button(Other_settings_frame, text="Adv. Settings", command=advset)
advset.grid(row=2, column=0, sticky="sewn")
#This is the advanced settings button
calc_but=Button(Other_settings_frame, text="Calculator", command=calculator, state='normal')
calc_but.grid(row=2, column=1,sticky="sewn")

#Button frame on bottom of screen
Button_frame=tk.Frame(frame)
Button_frame.grid(row=3,column=0, columnspan=3, sticky="nesw")

checkbut=Button(Button_frame, text="Check Values", command=check)
checkbut.pack(side=LEFT,fill="both",expand=1)
#This is the code for the button that clears all fields in Sequence_info_frame
clear_a_but=Button(Button_frame, text="Clear Values", command=clear_a)
clear_a_but.pack(side=RIGHT,fill="both",expand=1)

#This is the button that allows the user to submit all entries
submit_but=Button(mainroot, text="Submit", command=subform)
submit_but.pack(side=BOTTOM,fill="both",expand=1)

#This mainloop is what allows the GUI to persist if this is deleted the window will only flash on screen
mainroot.mainloop()
