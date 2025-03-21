
def connection(file=None):
    output=""
    global coordinates
    coordinates={}
    if not file:
        file=input("Please provide the path to your file:\n>")
    read_input(file)
    result=connection_path()
    for item in result:
        output+=item
    return output
    
    
def create_grid(xmax,ymax):
    for x in range(xmax+1):
        for y in range(ymax+1):
            coordinates[(x,y)]={"content":" ", "directions":[],"connections":[]}
    
def get_directions(content):

    norths=['║', '╚', '╝', '╠', '╣', '╩',"*",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    easts=['═', '╔', '╚', '╠', '╦', '╩',"*",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    souths=['║', '╔', '╗','╠', '╣', '╦',"*",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wests=['═', '╗', '╣', '╦', '╩','╝',"*",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    directions=[]
    if content in norths:
        directions.append("n")
    if content in easts:
        directions.append("e")
    if content in souths:
        directions.append("s")
    if content in wests:
        directions.append("w")
    
    return directions

def read_input(file, xmax=0, ymax=0):
    with open(file, "r") as fhand:
        content=[]
        for line in fhand:
            text=line.strip().split()
            character,x,y=read_line(text)
            if x>xmax:
                xmax=x
            if y>ymax:
                ymax=y
            content.append(((x,y),character))  
        create_grid(xmax,ymax)
        for item in content:
            coord=item[0]
            character=item[1]
            coordinates[coord]['content']=character
            coordinates[coord]['directions']=get_directions(character)
    return xmax, ymax


def read_line(text):
    character=text[0]
    x=int(text[1])
    y=int(text[2])
    return character, x, y




def print_grid(xmax,ymax):
    output=""
    current_row=ymax
    while current_row>=0:
        for coord in coordinates:
            xcoord=coord[0]
            ycoord=coord[1]
            if ycoord!=current_row:
                continue
            cell=coordinates[coord]['content']
            output+=f"{cell} "
            if xcoord==xmax:
                output+="\n"
        current_row-=1
    print(output)
        
def determine_partners(cell):
    connections=[]
    xcell=cell[0]
    ycell=cell[1]

    if coordinates[cell]["connections"]:
        return False
    if "n" in coordinates[cell]['directions']:
        xpartner=xcell
        ypartner=ycell+1
        reciprocal='s'
        if check_reciprocity((xpartner,ypartner),reciprocal):
            connections.append((xpartner,ypartner))
    if "e" in coordinates[cell]['directions']:
        xpartner=xcell+1
        ypartner=ycell
        reciprocal='w'
        if check_reciprocity((xpartner,ypartner),reciprocal):
            connections.append((xpartner,ypartner))
    if "s" in coordinates[cell]['directions']:
        xpartner=xcell
        ypartner=ycell-1
        reciprocal='n'
        if check_reciprocity((xpartner,ypartner),reciprocal):
            connections.append((xpartner,ypartner))
    if "w" in coordinates[cell]['directions']:
        xpartner=xcell-1
        ypartner=ycell
        reciprocal='e'
        if check_reciprocity((xpartner,ypartner),reciprocal):
            connections.append((xpartner,ypartner))
    return connections

def connection_path():
    connected=[]
    output=[]
    for coord in coordinates:
        if "*" != coordinates[coord]["content"]:
            continue
        connected.append(coord)
        if determine_partners(coord):
            coordinates[coord]["connections"]=determine_partners(coord)
            for item in coordinates[coord]["connections"]:
                connected.append(item)
    for cell in connected:
        if determine_partners(cell):
            coordinates[cell]["connections"]=determine_partners(cell)
            for item in coordinates[cell]["connections"]:
                if item not in connected:
                    connected.append(item)
    for coordinate in connected:
        letter=(coordinates[coordinate]['content'])
        letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if letter in letters:
            output.append(letter)
    return output

def check_reciprocity(cell, direction):
    try:
        if direction in coordinates[cell]['directions']:
            return True
        else:
            return False
    except(KeyError):
        return False

print(connection())
xmax,ymax=read_input("/home/smeod/Documents/Coding portfolio/Coding/Python/Testing and demos/pipe data test long")
