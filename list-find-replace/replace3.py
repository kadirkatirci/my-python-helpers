import os
import re

# Set the folder path and file names
folder_path = "dosyalar"
text_file_path = "degisim_liste.txt"

# Read the replacement texts from the file
with open(text_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Extract the first line as the replacement text
replacement_text = lines[0].strip()

# Initialize counters for matches and replacements
total_matches = 0
total_replacements = 0

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip subdirectories
    if os.path.isdir(file_path):
        continue

    # Read the content of each file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()

    # Initialize counters for matches and replacements in the current file
    file_matches = 0
    file_replacements = 0

    # Replace each line in the content
    for line in lines[1:]:
        line = line.strip()
        pattern = re.compile(re.escape(line), re.IGNORECASE)
        matches = len(re.findall(pattern, content))
        replacements = len(re.findall(pattern, content))        

        file_matches += matches
        file_replacements += replacements

        content = re.sub(pattern, replacement_text, content)

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    total_matches += file_matches
    total_replacements += file_replacements

    print(f"Replaced {file_replacements} occurrences in {filename} ({file_matches} matches).")

print(f"\nTotal matches: {total_matches}")
print(f"Total replacements: {total_replacements}")
