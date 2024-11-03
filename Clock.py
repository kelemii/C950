# Clock Implementation for WGUPS Routing Program
# Author: 001323392
import datetime

class Clock:
    def __init__(self, start_time=None):
        self.current_time = start_time if start_time else datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

    def advance_time(self, minutes):
        self.current_time += datetime.timedelta(minutes=minutes)

    def get_current_time(self):
        return self.current_time
