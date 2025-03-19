f_path=r"C:\Users\Jackb\OneDrive\Documents\Courses\Computing\SANS\Foundations\SANS_Foundations_Anki.txt"
current_card=""
section=None
subsection=None
i=0
card_list=[]
with open(f_path,"r") as fhand:
    for line in fhand:
        if line.capitalize().startswith(("Section")):
            section=line.split(":")[1]
            print(section)
            section=section.strip()
            print(section)
            i=0
            continue
        elif line.capitalize().startswith(("Subsection")):
            subsection=line.split(":")[1]
            print(subsection)
            subsection=subsection.strip()
            i=0
            continue
        tags=f"{section}, {subsection}"
        if line.strip():
            i+=1
            current_card+=f"{line.strip()};"
            if i==2:
                current_card+=tags
                card_list.append(current_card)
        else:
            i=0
            current_card=""

separator = '\n'  # Specify your desired separator

# Join the list elements into a single string using the separator
list_as_string = separator.join(map(str, card_list))

file_path = "output.txt"  # Replace with your desired file path

with open(r"C:\Users\Jackb\OneDrive\Documents\Courses\Computing\SANS\Foundations\Anki_output.txt", 'w') as file:
    file.write(list_as_string)
