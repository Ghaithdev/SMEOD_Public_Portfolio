from PIL import Image
from tkinter import filedialog
image=filedialog.askopenfilename(title="Select webp")
if not image:
    quit()
im=Image.open(image).convert("RGB")
im.save("Pixelate Logo.jpg","jpeg")
