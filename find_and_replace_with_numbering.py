import re

def find_and_replace_with_numbering(file_path, search_str):
    with open(file_path, 'r') as file:
        content = file.read()

    regex_pattern = re.compile(re.escape(search_str))

    i = 1
    def replace(match):
        nonlocal i
        replacement = f"{match.group()} - {i:02}"
        i += 1
        return replacement

    content = re.sub(regex_pattern, replace, content)

    with open(file_path, 'w') as file:
        file.write(content)

# example usage:
find_and_replace_with_numbering('Habbe.md', '-aziz!')