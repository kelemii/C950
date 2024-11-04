# WGUPS Routing Program
# Author: 001323392
import threading
from Truck import Truck
from data_loader import load_packages_from_csv
from adjacency_matrix import load_addresses_and_distances
from package_updater import schedule_package_update
from Driver import Driver
import package_status_checker
from settings import hash_table, csv_file_path, addresses_csv, distances_csv, clock, new_address

def update_package_in_hash_table(package_id, updated_package):
    hash_table.update(package_id, updated_package)

load_packages_from_csv(csv_file_path, hash_table)

address_mapping, adjacency_matrix = load_addresses_and_distances(addresses_csv, distances_csv)

# Creating truck instances
truck1 = Truck(1, clock)
truck2 = Truck(2, clock)
truck3 = Truck(3, clock)
truck_list = [truck1, truck2, truck3]

# Creating drivers
driver1 = Driver(1)
driver2 = Driver(2)

# Loading packages onto the trucks
truck1_package_ids = [1, 6, 13, 14, 15, 16, 20, 29, 30, 2, 4, 7] # 12 packages
truck2_package_ids = [3, 18, 25, 34, 36, 37, 38, 40, 10, 11, 12, 17] # 12 packages
truck3_package_ids = [5, 8, 9, 28, 31, 32, 19, 21, 22, 23, 24, 26, 27, 33, 35, 39] # 16 packages

Truck.load_packages_onto_truck(truck1, truck1_package_ids, hash_table)
Truck.load_packages_onto_truck(truck2, truck2_package_ids, hash_table)
Truck.load_packages_onto_truck(truck3, truck3_package_ids, hash_table)

# Assigning Trucks to Drivers
driver1.receive_truck(truck1)
driver2.receive_truck(truck2)

# Threads allow for multiple trucks to be running simultaneously
truck1_thread = threading.Thread(target=truck1.deliver_packages_nearest_neighbor, args=(adjacency_matrix, address_mapping, update_package_in_hash_table))
truck2_thread = threading.Thread(target=truck2.deliver_packages_nearest_neighbor, args=(adjacency_matrix, address_mapping, update_package_in_hash_table))
truck3_thread = threading.Thread(target=truck3.deliver_packages_nearest_neighbor, args=(adjacency_matrix, address_mapping, update_package_in_hash_table))
scheduled_update_thread = threading.Thread(target=schedule_package_update, args=(clock, hash_table, 9, new_address))
package_status_thread = threading.Thread(target=package_status_checker.package_status_checker, args=(clock, hash_table, truck_list))

# Starting threads
truck1_thread.start()
truck2_thread.start()
scheduled_update_thread.start()
package_status_thread.start()

# Checking to see when Truck 1 or Truck 2 returns to assign a driver to Truck 3, then begin its route
while truck1_thread.is_alive() or truck2_thread.is_alive():
    if not truck1_thread.is_alive():
        driver1.receive_truck(truck3)
        truck3_thread.start()
        break

    if not truck2_thread.is_alive():
        driver2.receive_truck(truck3)
        truck3_thread.start()
        break

truck3_thread.join()
total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
print(f"Total Mileage: {total_mileage}")












