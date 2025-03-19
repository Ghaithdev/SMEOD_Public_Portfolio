from PIL import Image
from numpy import round as round
import os
import customtkinter as ctk 
from tkinter import messagebox


class App(ctk.CTk):
    current_font=("Roboto", 18)
    # List to keep track of percentages
    percentage_values = []

    def __init__(self):
        super().__init__()

        self.file_source=None
        self.file_destination=None
        self.title("Pixelate Creator")
        self.geometry("800x800")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "App Images")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Pixelate_logo.jpg")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.automatic_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Pixelate", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.source_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Source",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.source_button_event)
        self.source_button.grid(row=1, column=0, sticky="ew")

        self.automatic_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Create",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.automatic_image, anchor="w",state=ctk.NORMAL, command=self.automatic_button_event)
        self.automatic_button.grid(row=2, column=0, sticky="ew")

        self.manual_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Refine",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",state=ctk.NORMAL, command=self.manual_button_event)
        self.manual_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create refine frame
        self.refine_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.refine_frame.grid_columnconfigure(0, weight=1)

        self.refine_frame_large_image_label = ctk.CTkLabel(self.refine_frame, text="", image=self.large_test_image)
        self.refine_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.refine_frame_button_1 = ctk.CTkButton(self.refine_frame, text="")
        self.refine_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.refine_frame_button_2 = ctk.CTkButton(self.refine_frame, text="CTkButton", compound="right")
        self.refine_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.refine_frame_button_3 = ctk.CTkButton(self.refine_frame, text="CTkButton", compound="top")
        self.refine_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.refine_frame_button_4 = ctk.CTkButton(self.refine_frame, text="CTkButton", compound="bottom", anchor="w")
        self.refine_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create source frame
        self.source_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.source_frame.grid_columnconfigure(0, weight=1)
        self.source_frame.grid_columnconfigure(1, weight=1)
        self.source_frame.grid_columnconfigure(2, weight=1)

        Label(self.source_frame, text='File Source:', column=0, row=0, padx=(0,5), pady=(10,5), sticky="n", text_color=None, font=App.current_font)
        self.source_label=Label(self.source_frame, text="No Source selected", column=1, row=0, padx=(5), pady=(10,5), sticky="n", text_color=None, font=App.current_font)
        self.source_select_button=Button(self.source_frame, text="Browse", column=2,row=0, padx=(5,10),sticky="ew", width=None, height=None, state=ctk.NORMAL, 
                 fg_color=None, hover_color=None, text_color=None, corner_radius=None, border_width=None, border_color=None,command=self.get_filesource)
        Label(self.source_frame, text='Save Destination:', column=0, row=1, padx=(0,5), pady=(10,5), sticky="n", text_color=None, font=App.current_font)
        self.destination_label=Label(self.source_frame, text="No Destination selected", column=1, row=1, padx=(5), pady=(10,5), sticky="n", text_color=None, font=App.current_font)
        self.destination_select_button=Button(self.source_frame, text="Browse", column=2,row=1, padx=(5,10),sticky="ew", width=None, height=None, state=ctk.NORMAL, 
                 fg_color=None, hover_color=None, text_color=None, corner_radius=None, border_width=None, border_color=None,command=self.get_filedestination)

        # create create frame
        self.create_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.create_frame.grid_columnconfigure(0, weight=1)
        self.create_frame.grid_columnconfigure(1, weight=1)
        self.create_frame.grid_columnconfigure(2, weight=1)

        Label(self.create_frame, text='Pixelation amount:', column=0, row=0, padx=(0,5), pady=(10,5), sticky="n", text_color=None, font=App.current_font)
        self.auto_pixelation_entry=ValidatedEntry(self.create_frame, min=0.0, max=100.0, increment=10.0, column=1, row=0)

        # Scrollable frame to display the list
        self.scrollable_percentage_list = ctk.CTkScrollableFrame(self.create_frame, width=200, height=400)
        Label(self.create_frame, text="Entered Quantities:",row=1,column=0, sticky="e")
        self.scrollable_percentage_list.grid(row=1, column=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.scrollable_percentage_list.grid_columnconfigure(0, weight=1)


        # select default frame
        self.select_frame_by_name("create frame")

    def get_filesource(self):
        self.file_source=ctk.filedialog.askdirectory(initialdir=(os.path.realpath(__file__)),title="Choose directory containing source images")
        if not self.file_source or self.file_source=="":
            messagebox.showerror(title="No folder selected",message="A folder must be selected in order to import files from that folder")
            self.source_label.update("No Folder selected")
            return False
        if not self.ximage_check(self.file_source):
            messagebox.showerror(title="Invalid folder selected",message="Folder must only contain image files, non-image files shold be hidden, directories will be ignored by the check")
            self.file_source=None
            self.source_label.update("Invalid folder selected")
            return False
        self.source_label.update(str(self.file_source))
        if self.file_source and self.file_destination:
            self.manual_button.configure(state=ctk.NORMAL)
            self.automatic_button.configure(state=ctk.NORMAL)

    def get_filedestination(self):
        self.file_destination=ctk.filedialog.askdirectory(initialdir=(os.path.realpath(__file__)),title="Choose directory containing source images")
        if not self.file_destination or self.file_destination=="":
            messagebox.showerror(title="No folder selected",message="A folder must be selected in order to import files from that folder")
            self.destination_label("No destination selected")
            return False
        self.destination_label.update(str(self.file_destination))
        if self.file_source and self.file_destination:
            self.manual_button.configure(state=ctk.NORMAL)
            self.automatic_button.configure(state=ctk.NORMAL)

    
    def ximage_check(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Skip directories or hidden files
            if os.path.isdir(file_path) or filename.startswith('.'):
                continue
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify if it's a valid image
            except (IOError, SyntaxError):
                return False  # Return False if any file is not a valid image
        return True  # Return True if all files are valid images

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.automatic_button.configure(fg_color=("gray75", "gray25") if name == "create frame" else "transparent")
        self.source_button.configure(fg_color=("gray75", "gray25") if name == "source frame" else "transparent")
        self.manual_button.configure(fg_color=("gray75", "gray25") if name == "refine frame" else "transparent")

        # show selected frame
        if name == "create frame":
            self.create_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.create_frame.grid_forget()
        if name == "source frame":
            self.source_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.source_frame.grid_forget()
        if name == "refine frame":
            self.refine_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.refine_frame.grid_forget()

    def source_button_event(self):
        self.select_frame_by_name("source frame")

    def automatic_button_event(self):
        self.select_frame_by_name("create frame")

    def manual_button_event(self):
        self.select_frame_by_name("refine frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

class LabelFrame(ctk.CTkFrame):
    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=1, text=None, labelanchor='n', padx=(10,0), pady=(10),
                 fg_color="transparent", corner_radius=10, border_width=0, border_color="transparent") -> None:
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color)
        self.grid(row=row, column=column, rowspan=rowspan, padx=padx, pady=pady, columnspan=columnspan)
        if text:
            self.label = ctk.CTkLabel(self, text=text)
            self.label.grid(sticky=labelanchor)

class Frame(ctk.CTkFrame):
    def __init__(self, parent, column=0, row=0, columnspan=1, rowspan=4, fg_color="transparent", corner_radius=10, border_width=0, border_color="transparent") -> None:
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

class Button(ctk.CTkButton):
    instance_list=[]

    def __init__(self, parent, text="Button", command=None, row=0, column=0, columnspan=1, rowspan=1, padx=(10,0), pady=(10,0), sticky="nesw", width=None, height=None, state=ctk.NORMAL, 
                 fg_color=None, hover_color=None, text_color=None, corner_radius=None, border_width=None, border_color=None,font=App.current_font):
        super().__init__(parent, text=text, command=command, state=state, fg_color=fg_color, hover_color=hover_color, text_color=text_color, 
                         corner_radius=corner_radius, border_width=border_width, border_color=border_color)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        if width:
            self.configure(width=width)
        if height:
            self.configure(height=height)
        self.configure(font=font)
        Button.instance_list.append(self)

class Label(ctk.CTkLabel):
    instance_list=[]

    def __init__(self, parent, text="text", column=0, row=0, padx=(0,0), pady=(0,0), sticky="w", 
                 text_color=None, font=App.current_font):
        super().__init__(parent, text=text, text_color=text_color, font=font)
        self.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        self.text = text
        Label.instance_list.append(self)
    
    def update(self, new_text="text"):
        self.configure(text=new_text)
        self.text = new_text

class Checkbox(ctk.CTkCheckBox):
    instance_list=[]

    def __init__(self, parent, name, column=0, row=0, error_msg=None, padx=(0,0), pady=(0,0), sticky="w",
                 text_color=None, fg_color=None, border_color=None, checkmark_color=None):
        self.variable = ctk.BooleanVar(self)
        super().__init__(parent, text=name, variable=self.variable, text_color=text_color, fg_color=fg_color, border_color=border_color, checkmark_color=checkmark_color)
        self.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        self.name = name
        if not error_msg:  # default error message for checkbox
            self.error_msg = f"{name.capitalize()} checkbox was left unticked"
        else:  # custom error message
            self.error_msg = error_msg
        Checkbox.instance_list.append(self)

    def checked(self):
        return self.variable.get()
    
    def set(self, boolean):
        self.variable.set(boolean)

class Combobox(ctk.CTkComboBox):
    instance_list=[]

    def __init__(self, parent, values=None, row=0, column=0, columnspan=1, padx=(0), pady=(0), sticky="nesw", 
                 fg_color=None, button_color=None, button_hover_color=None):
        if values is None:
            values = ["Default Value"]
        super().__init__(parent, values=values, fg_color=fg_color, button_color=button_color, button_hover_color=button_hover_color)
        self.current(0)
        self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        Combobox.instance_list.append(self)

class Entry(ctk.CTkEntry):
    instance_list=[]

    def __init__(self, parent, column=0, row=0, state=ctk.NORMAL, placeholder_text=None, fg_color=None, text_color=None, 
                 border_color=None, border_width=None, corner_radius=None, padx=(0,0), pady=(0,0), sticky="nesw"):
        super().__init__(parent, state=state, placeholder_text=placeholder_text, fg_color=fg_color, text_color=text_color, 
                         border_color=border_color, border_width=border_width, corner_radius=corner_radius)
        self.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        Entry.instance_list.append(self)

class Labelled_Checkbox:
    def __init__(self, parent, text="text", column=0, row=0, label_padx=(0,0), label_pady=(0,0), checkbox_padx=(0,0), checkbox_pady=(0,0), 
                 label_sticky="w", checkbox_sticky="w", text_color=None, fg_color=None, border_color=None, checkmark_color=None):
        Label(parent, text=text, column=column, row=row, padx=label_padx, pady=label_pady, sticky=label_sticky, text_color=text_color)
        self.checkbox = Checkbox(parent, name=text, column=(column+1), row=row, padx=checkbox_padx, pady=checkbox_pady, 
                                 sticky=checkbox_sticky, text_color=text_color, fg_color=fg_color, border_color=border_color, checkmark_color=checkmark_color)

class ValidatedEntry(ctk.CTkFrame):
    def __init__(self, parent, min=0.0, max=10.0, increment=0.1, row=0, column=1, padx=5, pady=5):
        super().__init__(parent)
        self.value = ctk.DoubleVar(value=((min+max)/2))
        self.from_ = min
        self.to = max
        self.increment = increment

        self.entry = Entry(parent, column=column, row=row, state=ctk.NORMAL, placeholder_text=self.value, fg_color=None, text_color=None, 
                 border_color=None, border_width=None, corner_radius=None, padx=(0,0), pady=(0,0), sticky="nesw")
        self.entry.grid(row=row, column=column, padx=padx, pady=pady)

        self.add_button = Button(parent, text="+", command=self.add_value, width=30,row=row, column=column+1, padx=5)
        self.add_button.grid(row=row, column=column+1, padx=5,sticky="news")


    def add_value(self):
        value=self.entry.get()
        value=check_number(value)
        if not check_number(value):
            return
        App.percentage_values.append(value)

def check_number(number):
    try:
        if float(number)<=0 or float(number)>=100:
            raise ValueError
        return int(number)
    except(ValueError):
        messagebox.showerror(title="Bad input", message="NUmbers must be a percentage between 0 and 100 (exclusive)")
        return False


if __name__ == "__main__":
    app = App()
    app.mainloop()






