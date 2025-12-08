import csv
from database import insert_entry  

csv_file = 'sample_data.csv'

try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            email = row['email']
            
            success = insert_entry(name, email)
            if success:
                print(f"Added: {name}, {email}")
            else:
                print(f"Duplicate found: {name}, {email}")

except FileNotFoundError:
    print(f"Error: CSV file '{csv_file}' not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

