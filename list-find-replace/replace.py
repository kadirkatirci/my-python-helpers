import os

folder_path = "dosyalar"  # Replace with the path to your folder containing the files
replacement_lists_file = "degisim_liste.txt"  # Replace with the path to your replacement lists file

def replace_lines(file_path, replacement_list):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    replaced_lines = []
    for line in lines:
        if line.strip():
            replaced_lines.append(replacement_list[0] + '\n')
        else:
            replaced_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(replaced_lines)


# Read the replacement lists from the text file
replacement_lists = []
with open(replacement_lists_file, 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()
    replacement_list = []
    for line in lines:
        if line.strip():
            replacement_list.append(line.strip())
        else:
            replacement_lists.append(replacement_list)
            replacement_list = []

    # Append the last replacement list if it exists
    if replacement_list:
        replacement_lists.append(replacement_list)

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        for replacement_list in replacement_lists:
            replace_lines(file_path, replacement_list)
