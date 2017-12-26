import os, sys
import unittest
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import json
from flask import Flask
from main import app


class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 6000
        app.config['LIVESERVER_TIMEOUT'] = 10
        self.client = app.test_client()

    def test_api_endpoint_gets_json(self):
        bus_stop = 10
        url = f'/api/{bus_stop}'
        response = self.client.get(url)
        schedule = json.loads(response.data)
        sched_str = json.dumps(schedule)
        self.assertSequenceEqual(["r1", "r2", "r3"], list(schedule.keys()))

    def test_out_of_range_bus_stop_returns_404(self):
        bus_stop = 11
        url = f'/api/{bus_stop}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()