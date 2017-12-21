import os, sys
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from bus_schedule_builder import make_schedule


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
        r1_stop1_departures = self.schedule['r1'][1]
        self.assertEqual(r1_stop1_departures, [0, 15, 30, 45])

    def test_route_2_start_times(self):
        r2_stop1_departures = self.schedule['r2'][1]
        self.assertEqual(r2_stop1_departures, [2, 17, 32, 47])

    def test_route_3_start_times(self):
        r3_stop1_departures = self.schedule['r3'][1]
        self.assertEqual(r3_stop1_departures, [4, 19, 34, 49])

    def test_route1_bus_stop_intervals_for_first_bus(self):
        r1 = self.schedule['r1']
        for stop in range(1, len(r1) - 1):
            stop_time = r1[stop][0]
            next_stop_time = r1[stop + 1][0]
            minutes = minutes_diff(stop_time, next_stop_time)
            self.assertEqual(2, minutes)


if __name__ == '__main__':
    unittest.main()