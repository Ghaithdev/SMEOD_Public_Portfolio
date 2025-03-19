import tkinter as tk
from tkinter import filedialog
from openpyxl import Workbook, load_workbook
from tkinter import messagebox

# Rest of your code...


class index():
    entries = []

    def __init__(self, keyword, pn, book):
        self.keyword = keyword
        self.page = pn
        self.book = book
        index.entries.append(self)

# Initialize the file path as None
excel_file_path = None
last_item_label = None

# Function to open a file dialog and set the excel_file_path
def open_excel_file():
    global excel_file_path
    excel_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    # Check if a file was selected
    if excel_file_path:
        commit_button.config(state=tk.NORMAL)  # Enable the "Commit" button if a file was selected
        enable_form_widgets()
        open_file_button.config(state=tk.DISABLED)  # Disable the open file button
    else:
        disable_form_widgets()

# Function to enable form widgets
def enable_form_widgets():
    entry1.config(state=tk.NORMAL)
    entry2.config(state=tk.NORMAL)
    entry3.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.NORMAL)

# Function to disable form widgets
def disable_form_widgets():
    entry1.config(state=tk.DISABLED)
    entry2.config(state=tk.DISABLED)
    entry3.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.DISABLED)

# Function to handle the "Submit" button click event
def submit():
    keyword = entry1.get()
    page_number = entry2.get()
    book = entry3.get()
    entry1.delete(0, tk.END)

    # Create an instance of the index class
    entry_instance = index(keyword, page_number, book)

    # Move the focus (selection) back to the "Keyword" entry widget
    entry1.focus_set()

    # Update the last item label
    update_last_item_label(keyword, book, page_number)

# Function to update the last item label
def update_last_item_label(keyword, book, page_number):
    global last_item_label

    if last_item_label:
        last_item_label.config(text=f"Last item submitted: Keyword='{keyword}', Book='{book}', Page='{page_number}'")
    else:
        last_item_label = tk.Label(root, text=f"Last item submitted: Keyword='{keyword}', Book='{book}', Page='{page_number}'")
        last_item_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

# Function to handle the "Reset Form" button click event
def reset_form():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

# Function to handle the "Commit" button click event
def commit():
    global excel_file_path
    if excel_file_path:
        try:
            wb = load_workbook(excel_file_path)
            ws = wb.active

            for item in index.entries:
                temp_list = [str(item.keyword), str(item.book), str(item.page)]
                ws.append(temp_list)

            wb.save(excel_file_path)
            show_message("Success: Data written to the Excel file.")
        except Exception as e:
            show_message(f"Error: {str(e)}")
    else:
        show_message("Error: Please select an Excel file first.")

# Function to show a message in a messagebox
def show_message(message):
    messagebox.showinfo("Message", message)

# Function to submit the form when the Enter key is pressed
def submit_on_enter(event):
    submit()

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter GUI")

# Create a button to open the Excel file
open_file_button = tk.Button(root, text="Open Excel File", command=open_excel_file)
open_file_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)


# Create labels
label1 = tk.Label(root, text="Keyword:")
label2 = tk.Label(root, text="Page number:")
label3 = tk.Label(root, text="Book:")

# Create entry widgets
entry1 = tk.Entry(root, state=tk.DISABLED)
entry2 = tk.Entry(root, state=tk.DISABLED)
entry3 = tk.Entry(root, state=tk.DISABLED)

# Arrange labels and entry widgets using the grid layout
label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry1.grid(row=1, column=1, padx=10, pady=5)
label2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry2.grid(row=2, column=1, padx=10, pady=5)
label3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry3.grid(row=3, column=1, padx=10, pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

# Create "Submit" button, "Reset Form" button, and "Commit" button inside the frame
submit_button = tk.Button(button_frame, text="Submit", command=submit, state=tk.DISABLED)
reset_button = tk.Button(button_frame, text="Reset Form", command=reset_form, state=tk.DISABLED)

# Grid placement for buttons
submit_button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
reset_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

# Create the "Commit" button outside the frame
commit_button = tk.Button(root, text="Commit", command=commit, state=tk.DISABLED)  # Disabled initially
commit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

# Automatically open the Excel file dialog on application start
#open_excel_file()

# Bind the Enter key to the "Submit" function
root.bind('<Return>', submit_on_enter)

# Start the Tkinter main loop
root.mainloop()