def get_nearest_bus_index(timestamp, stop_times):
    index = 0
    while stop_times[index] <= timestamp:
        index += 1
    
    # if index = 0:

    return index

def make_bus_stop_schedule(timestamp, stop_id):
    for route, stops in g.schedule.items():
        schedule[route] = stops[stop_id]

    return schedule