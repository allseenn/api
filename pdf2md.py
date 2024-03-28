import sys
import PyPDF2
from pdf2md import pdf2md

# Open the PDF file
with open(sys.argv[1], 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    num_pages = reader.numPages
    text = ''

    # Extract text from each page
    for page_num in range(num_pages):
        page = reader.getPage(page_num)
        text += page.extractText()

# Convert text to Markdown
markdown = pdf2md(text)

# Save the Markdown to a file
output_file_name = sys.argv[1][:-4] + '.md'
with open(output_file_name, 'w') as file:
    file.write(markdown)
