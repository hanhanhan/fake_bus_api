from time import time
from itertools import cycle
import sched, time

bus_stops = range(1, 11)
# routes servicing bus_stops
routes = [1, 2, 3]

# Minutes interval between sending buses on  route
same_route_start_interval = minutes_to_epoch(15)
different_route_start_interval = minutes_to_epoch(2)
drive_time_between_stops = minutes_to_epoch(2)

# create a dictionary of buses, continually update for time
scheduler = sched.scheduler()

def minutes_to_epoch(minutes):
    return time.gmtime(minutes * 60)


class Bus:

    def __init__(self, route, start_time):
        self.route = route
        self.time = start_time
        self.bus_stop_time = start_time
        self.on_route = True

    def move(self, cur_time):

        if self.bus_stop >= 10:
            self.on_route = False
            return

        if cur_time - self.bus_stop_time >= drive_time_between_stops:
            self.stop += 1
            self.stop_time += drive_time_between_stops





"""
pass in stop id, time
get out upcoming buses
route is an ordered set of stops
"""