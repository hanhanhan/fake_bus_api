# 0 15 30 45
# 2 17 32 47
# 4 19 34 49


# same_route_start_interval = minutes_to_epoch(15)
# different_route_start_interval = minutes_to_epoch(2)
# drive_time_between_stops = minutes_to_epoch(2)
BUS_STOPS = range(1, 11)
SAME_ROUTE_START_INTERVAL = 15
DIFFERENT_ROUTE_START_INTERVAL = 2
DRIVE_TIME_BETWEEN_STOPS = 2
schedule = {}


def make_route_schedule(minutes, schedule):
    ''' Pass in start time in minutes and schedule dictionary to build route schedule.
    '''
    for bus_stop in BUS_STOPS:

        if bus_stop not in schedule:
            schedule[bus_stop] = []

        schedule[bus_stop].append(minutes)
        minutes = (minutes + DRIVE_TIME_BETWEEN_STOPS) % 60

    return schedule


def main():
    # Routes dictionary 
    # to hold another dictionary of stops -> list of minutes past hour
    r1_schedule = {}
    r2_schedule = {}
    r3_schedule = {}

    # First bus of each hour for each route
    r1_start = 0
    r2_start = r1_start + DIFFERENT_ROUTE_START_INTERVAL
    r3_start = r2_start + DIFFERENT_ROUTE_START_INTERVAL
    
    # Bus start times at stop 1 throughout hour for each route
    r1_starts = range(r1_start, 60, SAME_ROUTE_START_INTERVAL)
    r2_starts = range(r2_start, 60, SAME_ROUTE_START_INTERVAL)
    r3_starts = range(r3_start, 60, SAME_ROUTE_START_INTERVAL)
    
    routes_starts = { 'r1': r1_starts, 
                      'r2': r2_starts, 
                      'r3': r3_starts, }

    schedules = { 'r1': r1_schedule,
                  'r2': r2_schedule,
                  'r3': r3_schedule, }

    for route, schedule in schedules:

        starts = routes_starts[route]

        for start in starts:
            make_route_schedule(start, schedule)

    return schedules


if __name__ == '__main__':
    main()
