import fitz  # PyMuPDF
import re

# Define the path to your PDF file
pdf_path = 'D:\\A\\_MISC10\\Star Scientist’s Claim of ‘Reverse Aging’ Draws Hail of Criticism - WSJ.pdf'
output_file_path = 'D:\\A\\_MISC10\\processed_text.txt'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Initialize a list to hold all rows of text
text_rows = []

# Iterate through each page
for page_num in range(pdf_document.page_count):
    # Get a page
    page = pdf_document.load_page(page_num)
    
    # Extract text from the page
    text = page.get_text()

    # Split the text into rows by new lines
    rows = text.split('\n')
    
    # Filter out non-printable characters using a regular expression
    printable_rows = [re.sub(r'[^\x20-\x7E]', '', row).strip() for row in rows]
    
    # Add the rows to the master list, excluding empty rows
    text_rows.extend(filter(None, printable_rows))

# Close the PDF after processing
pdf_document.close()

# Write the rows to a text file
with open(output_file_path, 'w', encoding='utf-8') as text_file:
    for row in text_rows:
        text_file.write(row + '\n')

# Output the number of rows written to the text file
number_of_rows = len(text_rows)
print(f'{number_of_rows} rows have been written to {output_file_path}')
