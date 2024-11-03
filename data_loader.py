# Data Loader Implementation for WGUPS Routing Program
# Author: 001323392
import pandas as pd
from PackageHashTable import PackageHashTable

def load_packages_from_csv(csv_file_path, hash_table):
    # Load the CSV file using pandas
    package_data = pd.read_csv(csv_file_path)

    # Iterate through the CSV file and insert each package into the hash table
    for index, row in package_data.iterrows():
        package_id = row['Package ID']
        address = row['Address']
        city = row['City']
        state = row['State']
        zip_code = row['Zip']
        deadline = row['Delivery Deadline']
        weight = row['Weight KILO']
        status = 'at the hub'  # Initially, all packages are at the hub
        notes = row.get('Special Notes', None)

        # Insert package into the hash table
        hash_table.insert(package_id, address, deadline, city, zip_code, weight, status, notes)
