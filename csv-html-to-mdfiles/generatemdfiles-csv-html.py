import os
import pandas as pd
import html2text
from unidecode import unidecode

# Read the CSV file into a DataFrame
file_path = 'your_file.csv'
df = pd.read_csv(file_path)

# Set the output directory
output_dir = 'output_md_files'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize the HTML to Markdown converter
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.body_width = 0  # Disable line wrapping

# Iterate over the DataFrame rows
for index, row in df.iterrows():
    # Format the file name with a leading zero-filled counter
    file_name = f'{index:03}.md'
    html_content = row[1]

    # Convert HTML content to Markdown
    md_content = converter.handle(html_content)

    # Write the Markdown content to a file
    with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

print("Markdown files created successfully!")