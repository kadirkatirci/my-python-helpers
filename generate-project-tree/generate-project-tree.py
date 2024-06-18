import os

IGNORE_LIST = {'.git'}

def should_ignore(path):
    for ignore in IGNORE_LIST:
        if ignore in path:
            return True
    return False

def generate_file_tree(start_path='.'):
    file_tree = []
    for root, dirs, files in os.walk(start_path):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]
        
        level = root.replace(start_path, '').count(os.sep)
        indent = '│  ' * level + '├─ '
        file_tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = '│  ' * (level + 1) + '├─ '
        for f in files:
            if not should_ignore(os.path.join(root, f)):
                file_tree.append(f"{subindent}{f}")
    return file_tree

def read_files(start_path='.'):
    file_contents = {}
    for root, _, files in os.walk(start_path):
        # Skip ignored directories
        dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and not should_ignore(os.path.join(root, d))]
        
        for file in files:
            file_path = os.path.join(root, file)
            if not should_ignore(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    relative_path = os.path.relpath(file_path, start_path)
                    file_contents[relative_path] = content
    return file_contents

def merge_to_markdown(file_tree, file_contents, output_file='project_tree.md'):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("## Project File Tree\n")
        f.write("```\n")
        for line in file_tree:
            f.write(line + "\n")
        f.write("```\n\n")
        
        for path, content in file_contents.items():
            f.write(f"### `{path}` :\n")
            f.write("```\n")
            f.write(content)
            f.write("\n```\n\n")

if __name__ == "__main__":
    start_path = '.'  # Specify your start path here
    file_tree = generate_file_tree(start_path)
    file_contents = read_files(start_path)
    merge_to_markdown(file_tree, file_contents)
