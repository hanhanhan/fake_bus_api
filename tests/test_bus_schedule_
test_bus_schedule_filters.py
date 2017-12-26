import os, sys
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from bus_schedule_filter import get_next_bus_i, make_stop_filtered_schedule
from bus_schedule_builder import make_schedule


class TestBusScheduleFilterFunctions(unittest.TestCase):

    # Test get_next_bus_i and edge cases
    def test_get_next_bus_i_wrap(self):
        stop_times = [3, 18, 33, 48]
        timestamp = 5

        # import pdb; pdb.set_trace()
        index = get_next_bus_i(timestamp, stop_times)
        self.assertEqual(index, 1)

    def test_get_next_bus_i_with_wrap(self):
        stop_times = [18, 33, 48, 3]
        timestamp = 55
        index = get_next_bus_i(timestamp, stop_times)
        self.assertEqual(index, 3)

    def test_get_next_bus_i_no_wrap_stop_times_index_wraps(self):
        stop_times = [3, 18, 33, 48]
        timestamp = 55
        index = get_next_bus_i(timestamp, stop_times)
        self.assertEqual(index, 0)

    def test_get_next_bus_i_wrap_stop_times_index_wraps(self):
        stop_times = [18, 33, 48, 3]
        timestamp = 3
        index = get_next_bus_i(timestamp, stop_times)
        self.assertEqual(index, 0)

    # Test make_bus_stop_schedule
    def test_get_next_bus_i(self):
        stop_id = 1
        timestamp = 5
        schedule = make_schedule()
        expected_schedule = { 'r1':[15, 30],
                              'r2':[17, 32],
                              'r3':[19, 34], }

        filtered_schedule = make_stop_filtered_schedule(timestamp, stop_id)
        self.assertEqual(filtered_schedule, expected_schedule)

    def test_get_next_bus_i_wrap_schedule(self):
        stop_id = 10
        timestamp = 55
        schedule = make_schedule()
        expected_schedule = { 'r1':[3, 18],
                              'r2':[5, 20],
                              'r3':[7, 22], }

        filtered_schedule = make_stop_filtered_schedule(timestamp, stop_id)
        self.assertEqual(filtered_schedule, expected_schedule)


        def test_get_next_bus_i_wrap_index(self):
            stop_id = 2
            timestamp = 55
            schedule = make_schedule()
            expected_schedule = { 'r1':[2, 17],
                                  'r2':[4, 19],
                                  'r3':[7, 22], }

            filtered_schedule = make_stop_filtered_schedule(timestamp, stop_id, schedule)
            self.assertEqual(filtered_schedule, expected_schedule)
"""
Schedule:
{'r1': {1: [0, 15, 30, 45],
        2: [2, 17, 32, 47],
        3: [4, 19, 34, 49],
        4: [6, 21, 36, 51],
        5: [8, 23, 38, 53],
        6: [10, 25, 40, 55],
        7: [12, 27, 42, 57],
        8: [14, 29, 44, 59],
        9: [16, 31, 46, 1],
        10: [18, 33, 48, 3]},
 'r2': {1: [2, 17, 32, 47],
        2: [4, 19, 34, 49],
        3: [6, 21, 36, 51],
        4: [8, 23, 38, 53],
        5: [10, 25, 40, 55],
        6: [12, 27, 42, 57],
        7: [14, 29, 44, 59],
        8: [16, 31, 46, 1],
        9: [18, 33, 48, 3],
        10: [20, 35, 50, 5]},
 'r3': {1: [4, 19, 34, 49],
        2: [6, 21, 36, 51],
        3: [8, 23, 38, 53],
        4: [10, 25, 40, 55],
        5: [12, 27, 42, 57],
        6: [14, 29, 44, 59],
        7: [16, 31, 46, 1],
        8: [18, 33, 48, 3],
        9: [20, 35, 50, 5],
        10: [22, 37, 52, 7]}}
"""


if __name__ == '__main__':
    unittest.main()
