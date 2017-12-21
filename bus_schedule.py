# 0 15 30 45
# 2 17 32 47
# 4 19 34 49

bus_stops = range(1, 11)
# same_route_start_interval = minutes_to_epoch(15)
# different_route_start_interval = minutes_to_epoch(2)
# drive_time_between_stops = minutes_to_epoch(2)

same_route_start_interval = 15
different_route_start_interval = 2
drive_time_between_stops = 2

# dictionary of routes -> bus_stops -> stop times


schedule = {}
route1_starts = range(0, 60, same_route_start_interval)
r1_schedule = {}

for route1_start in route1_starts:

    minutes = route1_start
    
    for bus_stop in bus_stops:

        if bus_stop not in r1_schedule:
            r1_schedule[bus_stop] = []
        
        r1_schedule[bus_stop].append(minutes)
        minutes = (minutes + drive_time_between_stops) % 60

