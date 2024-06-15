import pandas as pd

def split_csv(file_path, rows_per_file=1350):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get the total number of rows
    total_rows = len(df)
    
    # Calculate the number of files needed
    num_files = (total_rows // rows_per_file) + 1
    
    # Split the DataFrame and write each part to a new CSV file
    for i in range(num_files):
        start_row = i * rows_per_file
        end_row = start_row + rows_per_file
        split_df = df[start_row:end_row]
        
        # Define the new file name
        new_file_path = f"{file_path.split('.csv')[0]}_part_{i+1}.csv"
        
        # Write the split DataFrame to a new CSV file
        split_df.to_csv(new_file_path, index=False)
        print(f"Created: {new_file_path}")

# Usage
file_path = 'mail.csv'  # Replace with your CSV file path
split_csv(file_path)
