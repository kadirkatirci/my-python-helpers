import csv
import json

def convert_csv_to_json(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['json']
        
        rows = []
        for row in reader:
            id = row['id']
            name = row['name']
            images_urls = row['images_url'].split(', ')
            
            json_list = []
            for i, url in enumerate(images_urls):
                json_list.append({
                    "id": f"{id}-{i+1}",
                    "url": url,
                    "name": f"{name} - {i+1}"
                })
                
            row['json'] = json.dumps(json_list, ensure_ascii=False)
            rows.append(row)
        
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

# Usage
input_csv = 'input.csv'  # Replace with your input CSV file path
output_csv = 'output.csv'  # Replace with your desired output CSV file path
convert_csv_to_json(input_csv, output_csv)