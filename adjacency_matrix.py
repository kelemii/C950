# Adjacency Matrix Implementation for WGUPS Routing Program
# Author: 001323392
import pandas as pd

def load_addresses_and_distances(addresses_csv, distances_csv):
    # Load addresses from the CSV file
    addresses_data = pd.read_csv(addresses_csv, header=None, names=["Index", "Location Name", "Address"])
    address_mapping = addresses_data.set_index("Index").to_dict(orient="index")

    # Load distances from the CSV file and create an adjacency matrix
    distances_data = pd.read_csv(distances_csv, header=None)
    adjacency_matrix = distances_data.values
    return address_mapping, adjacency_matrix



# Example usage:
# adjacency_matrix, locations = load_adjacency_matrix('WGUPS_Distance_Table.csv')
