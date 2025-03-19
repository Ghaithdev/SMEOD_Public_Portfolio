import re
file_name=input("Please enter the name of the file including extension:")
if len(file_name)<1:
    file_name="Check.txt"
fhand=open(file_name)
for line in fhand:
    re.findall('([0-9])')
    readout=list()
    readout.append(line)
print (readout)
