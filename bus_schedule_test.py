import unittest
from bus_schedule_builder import make_schedule


class TestBusSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = make_schedule()
        import pdb; pdb.set_trace

    def test_route_1_start_times(self):
        import pdb; pdb.set_trace()
        r1_stop1_departures = self.schedule['r1'][1]
        self.assertEqual(r1_stop1_departures,[0, 15, 30, 45])


    def test_route_2_start_times(self):
        import pdb; pdb.set_trace()
        r2_stop1_departures = self.schedule['r2'][1]
        self.assertEqual(r2_stop1_departures,[2, 17, 32, 47])


    def test_route_3_start_times(self):
        # import pdb; pdb.set_trace()
        r3_stop1_departures = self.schedule['r3'][1]
        self.assertEqual(r3_stop1_departures,[4, 19, 34, 49])


if __name__ == '__main__':
    unittest.main()