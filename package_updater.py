import time

def schedule_package_update(clock, hash_table, package_id, new_address, scheduled_time):
    """
    Schedule a package address update for a specified time.

    :param clock: The clock instance managing the current time.
    :param hash_table: The hash table containing package information.
    :param package_id: The ID of the package to update.
    :param new_address: The new address to set.
    :param scheduled_time: The time at which to update the package.
    """
    while True:
        # Continuously check the current time
        current_time = clock.get_current_time()
        if current_time >= scheduled_time:
            # If the scheduled time has been reached, update the package
            package = hash_table.lookup(package_id)
            if package:
                updated_package = package.copy()
                updated_package["address"] = new_address
                hash_table.update(package_id, updated_package)
                print(
                    f"Package {package_id} address updated to {new_address} at {clock.get_current_time().strftime('%I:%M %p')}")
            break  # Exit the loop after the package has been updated

        # Sleep for a short interval to avoid busy waiting
        time.sleep(0.0005)
