print("Test that the directory has been found")
suffixes=list()
prefixes=list()
word_list=list()
user_file=input("Please enter the name of the file to be searched including the file extendsion: ")
if len(user_file)<1:
    user_file="test.txt"
fhand=open(user_file)
for line in fhand:
    print(line)
