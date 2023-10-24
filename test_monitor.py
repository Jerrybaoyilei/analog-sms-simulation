import io
import unittest
import sys
from producer import Producer
from sender import Sender
from monitor import Monitor


class TestMonitor(unittest.TestCase):

    def setUp(self):
        producer = Producer()
        senders_list = [Sender(), Sender(), Sender()]
        self.monitor = Monitor(1000, senders_list)

    def test_get_update_interval(self):
        self.assertEqual(self.monitor.get_update_interval(), 1000)

    def test_get_update_interval(self):
        self.assertEqual(self.monitor.get_update_interval(), 1000)

    def test_set_update_interval_positive_integer(self):
        self.monitor.set_update_interval(1234)
        self.assertEqual(self.monitor.get_update_interval(), 1234)

    def test_set_update_interval_invalid_value(self):
        self.monitor.set_update_interval(-500)
        self.assertEqual(self.monitor.get_update_interval(), 1000)

    def test_record(self):
        # test data for 3 Sender. Format: [success_counter, failure_counter, total_time] for each Sender
        test_data = [[5, 2, 300], [8, 1, 400], [10, 0, 500]]
        for i in range(3):
            self.monitor.senders_list[i].success_counter = test_data[i][0]
            self.monitor.senders_list[i].failure_counter = test_data[i][1]
            self.monitor.senders_list[i].total_time = test_data[i][2]
        self.assertTrue(self.monitor.record(1, 23))
        # Reference: https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        # Redirect stdout to capture print statement
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.monitor.record(2, 23)
        # restore original stdout
        sys.stdout = sys.__stdout__
        # Remove leading/trailing whitespace
        printed_content = captured_output.getvalue().strip()
        expected_output = f"""
        ================================
        Report #2
              
        Total number of successes: 23
        Total number of failures: 3
        Average time per message sent: 52.17391
        ================================
        """

        # Remove leading/trailing whitespace
        self.assertEqual(printed_content, expected_output.strip())


if __name__ == '__main__':
    unittest.main()
