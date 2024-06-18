import os
import subprocess

# Set the directory containing the DOCX files
docx_dir = "/path/"

# Loop through all the DOCX files in the directory and convert each one to PDF
for filename in os.listdir(docx_dir):
    if filename.endswith(".docx"):
        basename = os.path.splitext(filename)[0] # get the filename without extension
        docx_path = os.path.join(docx_dir, filename) # full path to input file
        pdf_path = os.path.join(docx_dir, basename + ".pdf") # full path to output file
        subprocess.run(["pandoc", docx_path, "-o", pdf_path])

