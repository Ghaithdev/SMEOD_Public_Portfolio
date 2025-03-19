import PyPDF2

def read_pdf_text(file_path):
    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store the text from the PDF
        text = ""

        # Iterate through all pages of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_num]

            # Extract text from the current page
            page_text = page.extract_text()

            # Append the extracted text to the overall text string
            text += page_text

    return text

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_text = read_pdf_text(r"C:\Users\Jackb\OneDrive\Documents\Courses\Gaeilge\Gaeilge Gan Stro\Gaeilge_gan_stró_beginners(with_text).pdf")
with open(r"C:\Users\Jackb\OneDrive\Documents\Courses\Gaeilge\Gaeilge Gan Stro\Gaeilge_gan_stró_beginners.txt",'w+', encoding="utf-8") as file:
    file.write(pdf_text)
print("done")
