import os, sys
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from helper_functions import get_nearest_bus_index, make_bus_stop_schedule


class TestHelperFunctions(unittest.TestCase):

    def test_get_nearest_bus_index(self):
        stop_times = [18, 33, 48, 3]
        timestamp = 55  
        get_nearest_bus_index(timestamp, stop_times)
        assertEquals(3)

        stop_times = [18, 33, 48, 3]
        timestamp = 3  
        get_nearest_bus_index(timestamp, stop_times)

        stop_times = [18, 33, 48, 3]
        timestamp = 3  
        get_nearest_bus_index(timestamp, stop_times)
"""

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