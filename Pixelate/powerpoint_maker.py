

yourpath=r"C:\Users\Jackb\OneDrive\Desktop\PFE\Projects (Jack)\Quiz stuff\Pixelate\Results"

for root, dirs, files in os.walk(yourpath, topdown=False):#Reads each of the files in the folder
    for name in files: #name refers to the specific file to be opened
        source_image_name=f"{name}"
        directory_name=r"C:\Users\Jackb\OneDrive\Desktop\PFE\Projects (Jack)\Quiz stuff\Pixelate\Source Images"
        f_name=f"{directory_name}\\{name}"
        