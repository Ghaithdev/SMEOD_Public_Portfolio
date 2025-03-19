import datetime
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
fhand=open(input("Please input filename including file extension\n>"),"a")
fhand.write(input("What would you like to append to the chosen text file?\n>")+"\nTheses additions were made on:"+ str(now)+"\n")
