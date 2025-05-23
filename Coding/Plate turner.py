from tkinter import filedialog

class grid():
    coordinates=[]

    def __init__(self, x, y, value):
        self.x=x
        self.y=y
        self.value=value
        grid.coordinates.append(self)

startx=-6
starty=4
ydir=-1

file=filedialog.askopenfilename(title="Choose file")

with open(file,"r") as fhand:
    x=startx
    y=starty
    first_pass=True
    for line in fhand:
        content=line.strip()
        current_coord=grid(x,y,content)
        if abs(y)==4:
            if not first_pass:
                ydir*=-1
                x+=1
                y-=ydir
                first_pass=True
                if x==0:
                    x+=1
            else:
                first_pass=False
        y+=ydir
        if y==0:
            y+=ydir


n=1
for coordinate in grid.coordinates:
    coordinate.x*=-1
    coordinate.y*=-1


temp_list=[]
output=[]

while startx<7:
    for coordinate in grid.coordinates:
        if coordinate.x==startx:
            temp_list.append((coordinate.y,coordinate))
    for item in temp_list:
        output.append(item[1])
    temp_list.clear()
    startx+=1

for item in output:
    print(item.value)