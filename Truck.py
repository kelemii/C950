# Truck Implementation for WGUPS Routing Program
# Author: 001323392
import time
from settings import hub, pause_event

class Truck:
    def __init__(self, truck_id, clock, capacity=16, speed=18):
        """
        Initialize a truck with a given capacity and speed.

        :param truck_id: Unique identifier for the truck.
        :param capacity: Maximum number of packages the truck can carry.
        :param speed: Speed of the truck in miles per hour.
        """
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed  # Speed in miles per hour
        self.packages = []  # List to store packages loaded on the truck
        self.current_location = hub  # Starting location (Hub)
        self.mileage = 0.0  # Total mileage covered by the truck
        self.clock = clock
        self.driver = None

    def load_package(self, package):
        """
        Load a package onto the truck if capacity allows.

        :param package: The package being loaded.
        :return: True if the package was loaded, False if the truck is full.
        """
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        return False

    def deliver_package_and_drive(self, package, distance):
        """
        Deliver a package and update the truck's current time and mileage.

        :param package: The package to be delivered.
        :param distance: The distance traveled to deliver the package.
        """
        if package:
            time.sleep(.1) # slows down delivery so pause/update time is more accurate
            # Drive to the location and update truck status
            self.mileage += distance
            travel_time_minutes = (distance / self.speed) * 60
            self.clock.advance_time(travel_time_minutes)

            # Deliver the package
            package_id = package["package_id"]
            package["status"] = "delivered"
            package["timestamp"] = self.clock.get_current_time().strftime("%I:%M %p")
            print(f"Package {package_id} delivered at {package['timestamp']}")

    def load_packages_onto_truck(truck, package_ids, hash_table):
        """
        Loads multiple packages onto the truck.

        :param truck: The truck instance.
        :param package_ids: List of package IDs to load.
        :param hash_table: The hash table containing package information.
        """
        for package_id in package_ids:
            package = hash_table.lookup(package_id)
            if package:
                loaded = truck.load_package(package)
                if loaded:
                    print(f"Package {package_id} successfully loaded onto Truck {truck.truck_id}.")
                else:
                    print(f"Failed to load Package {package_id} onto Truck {truck.truck_id}.")
            else:
                print(f"Package {package_id} not found in hash table.")

    def find_nearest_location(self, current_index, unvisited_indices, adjacency_matrix):
        """
        Find the nearest unvisited location from the current location.

        :param current_index: The current location index.
        :param unvisited_indices: List of indices of unvisited locations.
        :param adjacency_matrix: The adjacency matrix with distances between locations.
        :return: The index of the nearest unvisited location.
        """
        nearest_index = None
        shortest_distance = float('inf')

        for index in unvisited_indices:
            distance = adjacency_matrix[current_index, index]
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_index = index

        return nearest_index

    def deliver_packages_nearest_neighbor(self, adjacency_matrix, address_mapping, update_package_callback):
        """
        Deliver all packages on the truck using the nearest neighbor algorithm.

        :param adjacency_matrix: The adjacency matrix with distances between locations.
        :param address_mapping: The address mapping containing location indices and details.
        :param update_package_callback: A callback function to update the package information in the hash table.
        """
        # Ensure the truck has a driver before starting delivery
        if self.driver is None:
            print(f"Truck {self.truck_id} cannot start delivery without a driver.")
            return

        # Update all packages to 'en route' before starting the delivery
        for package in self.packages:
            package['status'] = 'en route'
            update_package_callback(package['package_id'], package)

        # Get the indices of locations the truck has packages for
        package_locations = [package['address'] for package in self.packages]
        unvisited_indices = []
        print(f"Truck {self.truck_id} has {len(self.packages)} packages and is starting delivery route")

        for location_index, address_data in address_mapping.items():
            if any(package_location in address_data["Address"] for package_location in package_locations):
                unvisited_indices.append(location_index)

        # Start from the hub
        current_index = 0  # Assuming index 0 is the hub

        while unvisited_indices:
            # Check if pause_event is set, if so, pause the thread
            while pause_event.is_set():
                time.sleep(1)
            # Find the nearest location
            nearest_index = self.find_nearest_location(current_index, unvisited_indices, adjacency_matrix)

            # Extract the distance, convert to float to prevent type errors
            distance_to_nearest = float(adjacency_matrix[current_index, nearest_index])

            # Deliver all packages at the nearest location and drive
            for package in list(self.packages):  # Iterate over a copy to modify the list
                if package['address'].strip().lower() == address_mapping[nearest_index]["Address"].strip().lower():
                    self.deliver_package_and_drive(package, distance_to_nearest)
                    # Update the package in the hash table using the callback
                    update_package_callback(package["package_id"], package)

            # Mark the location as visited
            unvisited_indices.remove(nearest_index)

            # Update the current index
            current_index = nearest_index

        print(f"Truck {self.truck_id} completed all deliveries. Total mileage: {self.mileage} miles.")
        if self.driver:
            self.driver.remove_truck()

    def update_loaded_package(self, package_id, updated_info):
        """
        Update an existing package that is currently loaded on the truck.

        :param package_id: Unique identifier for the package.
        :param updated_info: A dictionary with the updated package details.
        :return: True if the package was updated, False if not found.
        """
        for package in self.packages:
            if package['package_id'] == package_id:
                package.update(updated_info)
                print(f"Package {package_id} on Truck {self.truck_id} updated successfully.")
                return True
        print(f"Package {package_id} not found on Truck {self.truck_id}.")
        return False

    def view_current_packages_status(self):
        """
        Returns the status of all packages on this truck.
        """
        status_list = []
        for package in self.packages:
            status_list.append(
                f"=======================\n"
                f"Package ID: {package['package_id']}, Status: {package['status']}, Timestamp: {package.get('timestamp', 'N/A')}\n"
                f"=======================\n")

        return status_list



