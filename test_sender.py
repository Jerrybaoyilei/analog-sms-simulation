import unittest
from sender import Sender

class TestSender(unittest.TestCase):
    
    def setUp(self):
        self.sender = Sender(failure_rate = 0.2, wait_time_mean = 100, wait_time_std = 20)
        
    def test_get_success_counter(self):
        