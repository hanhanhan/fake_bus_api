""" Helper functions used to filter the overall bus schedule.
"""
from bus_schedule_builder import make_schedule


def get_next_bus_i(time, stop_times):
    """ Return the index for the current 
    or next bus at the stop from the stop times schedule.
    """

    def minutes_wrap(i):
        """ Check if minutes go from 60 to 0.
        """
        wrapped_stop_times = stop_times + [stop_times[0]]
        return wrapped_stop_times[i + 1] < stop_times[i]
    
    next_bus_i = 0
    for i, stop_time in enumerate(stop_times):

        if time > stop_time and not minutes_wrap(i):  #
            next_bus_i += 1

        elif time > stop_time and minutes_wrap(i):
            next_bus_i += 1
            break

        else:
            break

    # If the next bus is at the beginning of the list
    if next_bus_i > len(stop_times) - 1:
        next_bus_i = 0

    return next_bus_i


def get_next_next_bus_i(i, stop_times):
    """ Return the index for the second
    next bus at the stop.
    """
    # If next value is greater than last index then wrap the schedule
    if i + 1 > len(stop_times) - 1:
        return 0
    else:
        return i + 1


def make_stop_filtered_schedule(timestamp, stop_id):
    # Filter the complete schedule to return a dictionary of
    # the next two buses arriving on each route

    filtered_schedule = {}
    schedule = make_schedule()

    for route, bus_stops_schedules in schedule.items():
        next_two_buses = []
        stop_times = bus_stops_schedules[stop_id]

        next_bus_index = get_next_bus_i(timestamp, stop_times)
        next_next_bus_index = get_next_next_bus_i(next_bus_index, stop_times)

        next_two_buses.append(stop_times[next_bus_index])
        next_two_buses.append(stop_times[next_next_bus_index])

        filtered_schedule[route] = next_two_buses

    return filtered_schedule