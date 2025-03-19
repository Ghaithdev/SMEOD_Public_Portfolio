from PIL import Image
from numpy import round as round
import os
from tkinter import filedialog as filedialog
#define our sick pixelation function
def pixelate(image_path, pixelation_amount):
    
    #open image
    im = Image.open(image_path)
    #new dimensions via list comprehension
    new_dims = [int(round(a*pixelation_amount)+1) for a in im.size]
    #downsample, upsample, and return
    return im.resize(new_dims).resize(im.size, resample = 4)



yourpath=filedialog.askdirectory(title='Select a source folder')
storage_location=filedialog.askdirectory(title='Select a destination folder')

pixelation_amounts=["0.250","0.150","0.100","0.075","0.050","0.030","0.020","0.010"]
while True:
    pixelation=input("Please enter a pixelation factor, it should be  number between 0 & 1 (non-inclusive)\nWhen done type 'done'\n>")
    if pixelation.lower() =='done' or pixelation == "":
        break
    else:
        try:
            float(pixelation)
        except(ValueError):
            print("Non numeric input ignored")
            continue
        pixelation_amounts.append(pixelation)
                     
print("")
for root, dirs, files in os.walk(yourpath, topdown=False):#Reads each of the files in the folder
    for name in files: #name refers to the specific file to be opened
        for new_size in pixelation_amounts:
            size=new_size
            source_image_name=f"{name}"
            directory_name=yourpath
            f_name=f"{directory_name}/{name}"
            image=pixelate(f_name,float(new_size))
            new_f_name=f"{source_image_name.split('.')[0]}({size.zfill(0)}).{source_image_name.split('.')[1]}"
            filelocation=f"{storage_location}/{new_f_name}"
            image.save(filelocation)
