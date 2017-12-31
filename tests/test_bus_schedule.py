import os, sys
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from bus_schedule import make_schedule


# Helper function
def minutes_diff(t1, t2):
    """ Return the difference of two minute times
    which are within an hour of each other.
    """
    if t2 > t1:
        return t2 - t1
    else:
        return 60 - t1 + t2


class TestBusSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = make_schedule()

    def test_route_1_start_times(self):
        r1_stop1_departures = self.schedule[1][1]
        self.assertEqual(r1_stop1_departures, [0, 15, 30, 45])

    def test_route_2_start_times(self):
        r2_stop1_departures = self.schedule[1][2]
        self.assertEqual(r2_stop1_departures, [2, 17, 32, 47])

    def test_route_3_start_times(self):
        r3_stop1_departures = self.schedule[1][3]
        self.assertEqual(r3_stop1_departures, [4, 19, 34, 49])

    def test_bus_stop_intervals_for_first_bus_on_each_route(self):
        stops = range(1, 10)
        routes = range(1, 4)

        for route in routes:
            for stop in stops:
                # Minutes difference between stops along same route
                diff = self.schedule[stop + 1][route][0] - self.schedule[stop][route][0]
                self.assertEqual(2, diff)


if __name__ == '__main__':
    unittest.main()