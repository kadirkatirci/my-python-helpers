Python script that converts a CSV file with the specified format into JSON for each row, filling the `json` column

### How the Script Works:
1. **Reading the CSV File**: The script reads the input CSV file using `csv.DictReader`.
2. **Processing Each Row**: For each row, it extracts the `id`, `name`, and `images_url`. It then splits the `images_url` into a list of URLs.
3. **Creating JSON Entries**: It iterates through the list of URLs, creating a JSON entry for each URL with a unique `id`, `url`, and modified `name`.
4. **Appending JSON to Row**: The JSON list is then converted to a JSON string and added to the `json` field of the row.
5. **Writing to Output CSV**: Finally, the script writes the modified rows to a new CSV file with the additional `json` column.