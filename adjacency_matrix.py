# Adjacency Matrix Implementation for WGUPS Routing Program
# Author: 001323392
import csv

def load_addresses_and_distances(addresses_csv, distances_csv):
    # Load addresses from the CSV file
    address_mapping = {}
    with open(addresses_csv, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            index = int(row[0])
            location_name = row[1]
            address = row[2]
            address_mapping[index] = {
                "Location Name": location_name,
                "Address": address
            }

    # Load distances from the CSV file and create an adjacency matrix
    adjacency_matrix = []
    with open(distances_csv, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Convert distance row values to floats, ignoring any empty cells
            distance_row = [float(value) if value else 0.0 for value in row]
            adjacency_matrix.append(distance_row)

    return address_mapping, adjacency_matrix
