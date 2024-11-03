# Hash Table Implementation for WGUPS Routing Program
# Author: 001323392
class PackageHashTable:
    def __init__(self, capacity=10):
        """
        Initializes the hash table with a given capacity.
        The default capacity is set to 10 but can be expanded as needed.
        """
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        """
        Hash function to determine the index for a given key.
        """
        return key % self.capacity

    def insert(self, package_id, address, deadline, city, zip_code, weight, status, notes='none'):
        """
        Insert a package into the hash table.

        :param package_id: Unique identifier for the package.
        :param address: Delivery address of the package.
        :param deadline: Delivery deadline of the package.
        :param city: Delivery city.
        :param zip_code: Delivery zip code.
        :param weight: Weight of the package.
        :param status: Delivery status (e.g., 'at the hub', 'en route', 'delivered').
        :param notes: Delivery notes.
        """
        index = self._hash(package_id)
        # Check if package ID already exists
        for package in self.table[index]:
            if package["package_id"] == package_id:
                # Update existing package information
                package.update({
                    "address": address,
                    "deadline": deadline,
                    "city": city,
                    "zip_code": zip_code,
                    "weight": weight,
                    "status": status,
                    "notes": notes
                })
                return
        # If not found, insert as a new entry
        self.table[index].append({
            "package_id": package_id,
            "address": address,
            "deadline": deadline,
            "city": city,
            "zip_code": zip_code,
            "weight": weight,
            "status": status,
            "notes": notes
        })

    def lookup(self, package_id):
        """
        Look up a package by its package ID.

        :param package_id: Unique identifier for the package.
        :return: A dictionary with package details if found, else None.
        """
        index = self._hash(package_id)
        for package in self.table[index]:
            if package["package_id"] == package_id:
                return package
        return None

    def remove(self, package_id):
        """
        Remove a package from the hash table by its package ID.

        :param package_id: Unique identifier for the package.
        :return: True if the package was removed, False if not found.
        """
        index = self._hash(package_id)
        for i, package in enumerate(self.table[index]):
            if package["package_id"] == package_id:
                del self.table[index][i]
                return True
        return False

    def update(self, package_id, updated_package):
        """
        Update an existing package in the hash table.

        :param package_id: Unique identifier for the package.
        :param updated_package: A dictionary with the updated package details.
        :return: True if the package was updated, False if not found.
        """
        index = self._hash(package_id)
        for i, package in enumerate(self.table[index]):
            if package["package_id"] == package_id:
                self.table[index][i] = updated_package
                return True
        return False

    def view_package_status(self, package_id):
        """
        View the delivery status of a package.

        :param package_id: Unique identifier for the package.
        :return: A string describing the package status, or None if not found.
        """
        package = self.lookup(package_id)
        if package:
            return (f"==============================================\n"
                    f"Package ID: {package['package_id']}\n"
                    f"Address: {package['address']}, {package['city']}, {package['zip_code']}\n"
                    f"Deadline: {package['deadline']} "
                    f"Weight: {package['weight']} kg "
                    f"Status: {package['status']} "
                    f"Timestamp: {package.get('timestamp', 'N/A')}\n"
                    f"==============================================")
        return "Package not found."

    def view_all_packages_status(self):
        """
        View the delivery status of all packages in the hash table.

        :return: A list of strings describing the status of all packages.
        """
        statuses = []
        for bucket in self.table:
            for package in bucket:
                statuses.append(self.view_package_status(package['package_id']))
        return statuses