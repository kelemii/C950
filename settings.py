import threading
from Clock import Clock
from PackageHashTable import PackageHashTable

# This file is for easily changing variables, and cleanliness

clock = Clock()
hub = "4001 South 700 East"
pause_event = threading.Event()
hash_table = PackageHashTable(40)
csv_file_path = 'Files/WGUPS Package File.csv'
addresses_csv = 'Files/WGUPS Address File.csv'
distances_csv = 'Files/WGUPS Distance Table.csv'
scheduled_time = clock.get_current_time().replace(hour=10, minute=20)
new_address = "410 S. State St., Salt Lake City, UT 84111"
updated_package_info = hash_table.lookup(9)

stop_time = clock.get_current_time().replace(hour=12, minute=3)  # UPDATE THIS TO CHANGE WHEN PAUSE HAPPENS



