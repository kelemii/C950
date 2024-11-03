# Driver Implementation for WGUPS Routing Program
# Author: 001323392

class Driver:
    def __init__(self, driver_id):
        """
        Initializes a driver for a truck
        :param driver_id:
        """
        self.driver_id = driver_id
        self.truck = None

    def receive_truck(self, truck):
        """
        Assigns a truck to a driver
        :param truck:
        :return:
        """
        truck.driver = self
        self.truck = truck
        return True

    def remove_truck(self):
        """
        Removes a truck from a driver
        :return:
        """
        if self.truck is not None:
            self.truck.driver = None
            self.truck = None
        return True