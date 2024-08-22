import PyPDF2
import markdown
import re

def pdf_to_markdown(pdf_path, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract text from each page
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n\n"
        
        # Basic formatting
        # Convert headers (assuming headers are in all caps)
        text = re.sub(r'^([A-Z\s]+)$', r'# \1', text, flags=re.MULTILINE)
        
        # Convert bullet points
        text = re.sub(r'^\s*•\s*', '* ', text, flags=re.MULTILINE)
        
        # Convert numbered lists
        text = re.sub(r'^\s*(\d+)\.\s*', r'\1. ', text, flags=re.MULTILINE)
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(text)

# Usage
pdf_path = 'AB.pdf'
output_path = 'AB.md'
pdf_to_markdown(pdf_path, output_path)
print(f"Conversion complete. Markdown file saved as {output_path}")