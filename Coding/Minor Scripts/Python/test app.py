import hashlib
from tkinter import filedialog

print(len("0ec43321299d3908bf8d53433460f7a111e8690437cb0801fd602cb6d093805b"))

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

filename=filedialog.askopenfilename(title='Choose file')
print(sha256sum(filename))