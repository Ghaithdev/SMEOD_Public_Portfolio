with open (r"C:\Users\Jackb\OneDrive\Documents\PFE\Projects (Jack)\SANS\Sec_401\Auto_notes.md","r") as fhand:
    word_count=0
    for line in fhand:
        words=len(line.split())
        word_count+=words

print(word_count)
print(f"Approximate number of messages: {word_count/(4096/4)}")