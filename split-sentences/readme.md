# Sentence Splitter Script

This Python script recursively processes all text files in the current directory and its subdirectories, splitting sentences based on specific rules extracted from the provided code. It replaces the original file content with the newly split sentences.

## Features

- **Recursive Processing**: Automatically processes all files in the current directory and subdirectories.
- **Custom Sentence Splitting Rules**: Implements specific rules for splitting sentences, handling punctuation, quotes, and special characters.
- **In-place Modification**: Overwrites the original files with the processed content.
- **Text Cleanup**: Removes text within square brackets `[]` or curly braces `{}`, including the brackets/braces themselves.


## Usage

1. **Backup Your Files**

   Before running the script, it's highly recommended to back up your files to prevent data loss, as the script overwrites the original files.

2. **Run the Script**

   ```bash
   python split_sentences.py
   ```

   If `python` points to Python 2 on your system, use:

   ```bash
   python3 split_sentences.py
   ```

3. **Processing Output**

   The script will print the paths of the files it processes. If any errors occur (e.g., unreadable files), they will be displayed in the console.

## Example

**Original File Content (`example.txt`):**

```
This is a paragraph. It contains sentences! And some "quoted text." [This should be removed]{And this too} End of paragraph.

Another paragraph? Yes it is! With some special@characters#inside.
```

**Command:**

```bash
python split_sentences.py
```

**Processed File Content (`example.txt` after running the script):**

```
This is a paragraph.
It contains sentences!
And some "quoted text."
End of paragraph.
Another paragraph?
Yes it is!
With some special
characters
inside.
```

## Notes

- **Sentence Splitting Rules:**

  - **Visible End-of-Sentence Characters:** `.`, `?`, `!`, `:`
  - **Invisible End-of-Sentence Characters:** `@`, `#`
  - Sentences are split based on these characters when not within quotes (`"`).
  - Handles quotation marks by toggling an `in_quotes` flag.
  - Skips spaces following end-of-sentence characters.

- **Text Removal:**

  - Removes any text within square brackets `[]` or curly braces `{}`, including the brackets/braces themselves.

- **File Encoding:**

  - The script assumes that all files are text files encoded in UTF-8. If your files use a different encoding, adjust the `encoding` parameter in the `open` function calls accordingly.