dir_mode=open('LookupTable.txt')
C2N=dict()
N2C={}
print(N2C)
position=0
for line in dir_mode:
    position=position+1
    coord=line.lstrip().rstrip()
    C2N[coord]=position
    N2C[position]=coord
print(N2C)
while True:
    terminus=int(input("Input number"))
    if terminus in N2C:
        X0=N2C[terminus]
        print("the number", terminus, "corresponds with the coordinate:", X0)
    elif terminus == "":
        quit()
    #seqlen=tray*96+pos
    #print("The sequence is",seqlen,"long.")
#for k,v in C2N.items():
    #print(k,"is position number", v)
#for k,v in N2C.items():
    #print("Position number",k,"corresponds to coordinate:", v)
