f_path=r"C:\Users\Jackb\OneDrive\Documents\PFE\Projects (Jack)\SANS\Sec_401\Auto_notes_book3"
current_card=""
card_list=[]
question=""
answer=""
tags=""
with open(f_path,"r") as fhand:
    for line in fhand:
        if line.capitalize().startswith(("Question:")):
            question=line.removeprefix("Question: ")
            question=question.strip()
            continue
        elif line.capitalize().startswith(("Answer:")):
            answer=line.removeprefix("Answer: ")
            answer=answer.strip()
            continue
        elif line.capitalize().startswith(("Tags:")):
            tags=line.removeprefix("Tags:")
            tags=tags.strip()
            current_card=f"{question}; {answer}; {tags}"
            card_list.append(current_card)
        else:
            if question and answer and not tags:
                current_card=f"{question}; {answer};"
                card_list.append(current_card)
            current_card=""
            question=""
            answer=""
            tags=""



separator = '\n'  # Specify your desired separator

# Join the list elements into a single string using the separator
list_as_string = separator.join(map(str, card_list))

file_path = "output.txt"  # Replace with your desired file path

with open(r"C:\Users\Jackb\OneDrive\Documents\PFE\Projects (Jack)\SANS\Anki_output.txt", 'w+') as file:
    file.write(list_as_string)
print(f"Done creating {len(card_list)} cards")