from time import time
from itertools import cycle

bus_stops = range(1, 11)
# routes servicing bus_stops
routes = [1, 2, 3]

# Minutes interval between sending buses on  route
same_route_start_interval = 15
different_route_start_interval = 2
drive_time_between_stops = 2

# create a dictionary of buses, continually update for time


def minutes_to_epoch(minutes):
    return time.gmtime(minutes * 60)


class Bus:

    def __init__(self, route, start_time):
        self.route = route
        self.time = start_time
        self.bus_stop_time = start_time
        self.in_service = True


    def __iter__(self, time):

        for bus_stop in cycle(bus_stops):
            self.stop = bus_stop
            self.stop_time += drive_time_between_stops
            yield (self.stop, self.bus_stop_time)


class Stop:

    def __init__(self, stop_id, buses):
        self.stop_id = stop_id
        self.buses = buses

    def get_next_buses(self, time):

        return bus

"""
pass in stop id, time
get out upcoming buses
route is an ordered set of stops
"""