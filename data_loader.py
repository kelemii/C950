# Data Loader Implementation for WGUPS Routing Program
# Author: 001323392
import csv

def load_packages_from_csv(csv_file_path, hash_table):
    # Load the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate through the CSV file and insert each package into the hash table
        for row in csv_reader:
            package_id = int(row['Package ID'])  # Assuming Package ID is an integer
            address = row['Address']
            city = row['City']
            state = row['State']
            zip_code = row['Zip']
            deadline = row['Delivery Deadline']
            weight = row['Weight KILO']
            status = 'at the hub'  # All packages start at the hub
            notes = row.get('Special Notes', 'none')

            # Insert package into the hash table
            hash_table.insert(package_id, address, deadline, city, zip_code, weight, status, notes)
