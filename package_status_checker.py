from settings import pause_event


def package_status_checker(clock, hash_table, truck_list, stop_time):
    """
    Checks for time, and executes method for creating user interface when time is reached
    :param stop_time:
    :param clock:
    :param hash_table:
    :param truck_list:
    :return:
    """
    truck1 = truck_list[0]
    truck2 = truck_list[1]
    truck3 = truck_list[2]
    while True:
        # Check the current time
        current_time = clock.get_current_time()
        if current_time >= stop_time:
            # if time has been reached/passed pause truck threads
            print("Pausing Truck threads for status check")
            pause_event.set()
            user_interface(clock, hash_table, truck1, truck2, truck3)
            print("Resuming Truck threads")
            pause_event.clear() #stops event
            break

def user_interface(clock, hash_table, truck1, truck2, truck3):
    """
    Creates a user interface to view status of packages
    :param clock:
    :param hash_table:
    :param truck1:
    :param truck2:
    :param truck3:
    :return:
    """
    while True:
        print("\nSelect an option:")
        print("1: View status of a specific package")
        print("2: View status of all packages")
        print("3: View current total mileage of all trucks")
        print("4: View current status of all packages on each truck")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            package_id = int(input("Enter the Package ID: "))
            print(f"==============================================\n"
            f"Current Time {clock.current_time}")
            print(hash_table.view_package_status(package_id))

        elif choice == "2":
            statuses = hash_table.view_all_packages_status()
            print(f"==============================================\n"
            f"Current Time {clock.current_time}")
            for status in statuses:
                print(status)

        elif choice == "3":
            total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
            print(f"Total mileage of all trucks: {total_mileage} miles at {clock.current_time}")

        elif choice == "4":
            print("\nTruck 1 Packages Status:")
            print(f"==============================================\n"
            f"Current Time {clock.current_time}")
            for status in truck1.view_current_packages_status():
                print(status)

            print("\nTruck 2 Packages Status:")
            print(f"==============================================\n"
            f"Current Time {clock.current_time}")
            for status in truck2.view_current_packages_status():
                print(status)

            print("\nTruck 3 Packages Status:")
            print(f"==============================================\n"
            f"Current Time {clock.current_time}")
            for status in truck3.view_current_packages_status():
                print(status)

        elif choice == "5":
            print("Exiting the interface.")
            break

        else:
            print("Invalid choice. Please try again.")







