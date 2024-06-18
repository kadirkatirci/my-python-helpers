
## Markdown Conversion Script

This script reads a CSV file containing HTML content, converts the HTML content to Markdown format, and saves the converted content into individual Markdown files.

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Pandas**: A Python library for data manipulation and analysis.
3. **html2text**: A Python library that converts HTML to Markdown.
4. **unidecode**: A Python library for ASCII transliterations of Unicode text.

You can install the required libraries using pip:

```bash
pip install pandas html2text unidecode
```

### Script Details

- **Input**: A CSV file (`your_file.csv`) with HTML content.
- **Output**: A directory (`output_md_files`) containing individual Markdown files, one for each row of the CSV.

### Script Description

1. **Reading the CSV File**:
    - The script reads a CSV file into a Pandas DataFrame.
    - The file path is specified by the `file_path` variable.

2. **Creating the Output Directory**:
    - The script checks if the specified output directory (`output_md_files`) exists. If not, it creates the directory.

3. **HTML to Markdown Conversion**:
    - The script initializes the `html2text` converter, which is used to convert HTML content to Markdown.
    - It iterates over each row of the DataFrame, converting the HTML content in each row to Markdown.

4. **Saving Markdown Files**:
    - The converted Markdown content is saved in individual files within the output directory.
    - Each file is named with a zero-padded index (e.g., `000.md`, `001.md`).

### How to Run

1. **Prepare your CSV file**: Ensure your CSV file (`your_file.csv`) is in the same directory as the script or update the `file_path` variable to the correct path.
2. **Run the Script**: Execute the script using Python.

```bash
python script_name.py
```

3. **Check the Output**: The converted Markdown files will be in the `output_md_files` directory.

### Example

If your CSV file looks like this:

| Index | HTML Content |
|-------|--------------|
| 0     | <p>Hello, World!</p> |
| 1     | <h1>Welcome</h1><p>This is a test.</p> |

The script will generate two Markdown files:

- `output_md_files/000.md` containing:
  ```
  Hello, World!
  ```

- `output_md_files/001.md` containing:
  ```
  # Welcome

  This is a test.
  ```

### Notes

- Ensure the HTML content in your CSV file is properly formatted to avoid conversion errors.
- The script uses the second column of the DataFrame (`row[1]`) for HTML content. If your HTML content is in a different column, adjust the script accordingly.