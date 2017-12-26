import os, sys
import unittest
sys.path.append("..")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import json
from flask import Flask
from main import app


class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        # app = Flask(__name__)
        app.config['TESTING'] = True
        # app.config['DEBUG'] = True
        app.config['LIVESERVER_PORT'] = 6000
        app.config['LIVESERVER_TIMEOUT'] = 10
        self.client = app.test_client()

    def test_api_endpoint_gets_json(self):
        bus_stop = 10
        url = f'/api/{bus_stop}'
        response = self.client.get(url)
        schedule = json.loads(response.data)
        sched_str = json.dumps(schedule)
        self.assertEqual(200, response.status_code)
        
        import re
        reg = re.compile(r"r1")
        # self.assertRegex(sched_str, reg)
        # import pdb; pdb.set_trace()
        rge = re.compile(r'{"r1":\s\W\d\d?,\s\d\d?\W,\s"r2":\s\W\d\d?,\s\d\d?\W,\s"r3":\s\W\d\d?,\s\d\d?\W}')
        # self.assertRegex('sched_str', rge)

    def test_out_of_range_bus_stop_returns_404(self):
        bus_stop = 11
        url = f'/api/{bus_stop}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()