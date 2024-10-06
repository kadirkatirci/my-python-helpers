# Slugify Files and Folders

This Python script recursively renames all files and directories in the current working directory by converting their names to a URL-friendly format (slugifying), while preserving file extensions and handling Turkish characters. It helps in renaming files and folders to be compatible with web standards or other systems where special characters and spaces are not allowed.

## Features
- **Recursive Renaming**: Slugifies all files and folders, including subdirectories.
- **Handles Turkish Characters**: Converts Turkish-specific characters (e.g., `ç`, `ş`, `ü`) to their closest Latin equivalents.
- **Preserves Hyphens**: Retains hyphens (`-`) in filenames and folder names.
- **Maintains File Extensions**: Does not modify file extensions (e.g., `.txt`, `.jpg`).
- **Removes Special Characters**: Removes any special characters except for alphanumeric characters, hyphens, and underscores.
- **Converts Spaces**: Replaces spaces and consecutive hyphens with a single hyphen (`-`).

## Usage

### Requirements
- Python 3.x

### Installation
1. Clone this repository:

2. Navigate to the project directory:
   ```bash
   cd slugify-files-folders
   ```

3. Install required dependencies (if any).

### Running the Script

1. Place the script in the root directory of the folder structure you want to slugify.

2. Run the script with Python:
   ```bash
   python slugify.py
   ```

The script will recursively go through all folders and files in the current directory, renaming them to a slugified format. File extensions will be preserved, but file names and directory names will be updated.

### Example

If you have the following directory structure:
```
./
└── my folder/
    ├── special file!.txt
    ├── Türkçe karakterli dosya.docx
    └── Sub Folder/
        └── Another file.jpeg
```

After running the script, it will be renamed as:
```
./
└── my-folder/
    ├── special-file.txt
    ├── turkce-karakterli-dosya.docx
    └── sub-folder/
        └── another-file.jpeg
```
