""" This script creates a dictionary of routes -> 
bus stops -> a list of times
"""

BUS_STOPS = range(1, 11)
SAME_ROUTE_START_INTERVAL = 15
DIFFERENT_ROUTE_START_INTERVAL = 2
DRIVE_TIME_BETWEEN_STOPS = 2

R1 = 1
R2 = 2
R3 = 3
# Setup

# Routes dictionary 
# to hold another dictionary of stops -> list of minutes past hour
routes = [R1, R2, R3]

# First bus of each hour for each route
r1_start = 0
r2_start = r1_start + DIFFERENT_ROUTE_START_INTERVAL
r3_start = r2_start + DIFFERENT_ROUTE_START_INTERVAL

# Bus start times at stop 1 throughout hour for each route
r1_starts = list(range(r1_start, 60, SAME_ROUTE_START_INTERVAL))
r2_starts = list(range(r2_start, 60, SAME_ROUTE_START_INTERVAL))
r3_starts = list(range(r3_start, 60, SAME_ROUTE_START_INTERVAL))


routes_starts = { R1: r1_starts, 
                  R2: r2_starts, 
                  R3: r3_starts, }


def get_route_times(route, bus_stop):
    route_times = []
    
    for start in routes_starts[route]:
        minutes = (start + (bus_stop - 1) * DRIVE_TIME_BETWEEN_STOPS) % 60
        route_times.append(minutes)

    return route_times


def make_schedule():
    """ Return a dictionary of bus stops -> routes -> arrival times in minutes
    """
    route_schedule = {route: None for route in routes}
    schedule = {bus_stop: route_schedule for bus_stop in BUS_STOPS}

    for bus_stop, route_schedule in schedule.items():
        for route in route_schedule:
            stop_times = get_route_times(route, bus_stop)
            route_schedule[route] = stop_times

    return schedule


if __name__ == '__main__':
    make_schedule()
