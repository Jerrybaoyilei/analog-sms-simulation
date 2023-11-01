import unittest
from unittest.mock import patch
from io import StringIO
from Producer import Producer
from Sender import Sender
from Monitor import Monitor
from Simulation import Simulation


class TestSimulation(unittest.TestCase):
    # reference: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

    @patch("builtins.input", side_effect=["sdklafj", "-100", "1232.4", "1234"])
    def test_get_num_messages_from_input(self, mock_input):
        sim = Simulation()
        # First 3 values should not be accepted, only the last value of 1000 should be accepted and used
        num_messages = sim.get_num_messages_from_input()
        self.assertEqual(num_messages, 1234)

    @patch("builtins.input", side_effect=[""])
    def test_get_num_messages_from_input_empty_input(self, mock_input):
        sim = Simulation()
        # Simulate when user presses enter without entering any value
        num_messages = sim.get_num_messages_from_input()
        self.assertEqual(num_messages, 1000)

    @patch("builtins.input", side_effect=["sdafwefew", "-2356", "123445.6544", "560"])
    def test_get_max_message_length_from_input(self, mock_input):
        sim = Simulation()
        max_message_length = sim.get_max_message_length_from_input()
        self.assertEqual(max_message_length, 560)

    @patch("builtins.input", side_effect=[""])
    def test_get_max_message_length_from_input_empty_input(self, mock_input):
        sim = Simulation()
        max_message_length = sim.get_max_message_length_from_input()
        self.assertEqual(max_message_length, 100)

    @patch("builtins.input", side_effect=["sdafwefew", "-2356", "123445.6544", "1200", "600"])
    def test_get_num_sender_from_input(self, mock_input):
        sim = Simulation()
        num_messages = 1000
        # Only the last value of 600 should be accepted and used; 1200 is used to simulate when there are more senders than messages
        num_senders = sim.get_num_sender_from_input(num_messages)
        self.assertEqual(num_senders, 600)

    @patch("builtins.input", side_effect=[""])
    def test_get_num_sender_from_input_empty_input(self, mock_input):
        sim = Simulation()
        num_messages = 1000
        # Only the last value of 600 should be accepted and used; 1200 is used to simulate when there are more senders than messages
        num_senders = sim.get_num_sender_from_input(num_messages)
        self.assertEqual(num_senders, 10)

    @patch("builtins.input", side_effect=["1.2", "asfwefe", "-0.05", "0.5"])
    def test_get_failure_rate_from_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 1
        # the first value in side_effect simulates when failure rate is greater than 100%
        failure_rate = sim.get_failure_rate_from_input(sender_num)
        self.assertEqual(failure_rate, 0.5)

    @patch("builtins.input", side_effect=[""])
    def test_get_failure_rate_from_input_empty_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 2
        # the first value in side_effect simulates when failure rate is greater than 100%
        failure_rate = sim.get_failure_rate_from_input(sender_num)
        self.assertEqual(failure_rate, 0.2)

    @patch("builtins.input", side_effect=["flawkejf", "-2138943", "0.1", "239"])
    def test_get_wait_time_mean_from_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 1
        wait_time_mean = sim.get_wait_time_mean_from_input(sender_num)
        self.assertEqual(wait_time_mean, 239)

    @patch("builtins.input", side_effect=[""])
    def test_get_wait_time_mean_from_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 1
        wait_time_mean = sim.get_wait_time_mean_from_input(sender_num)
        self.assertEqual(wait_time_mean, 200)

    @patch("builtins.input", side_effect=["sadfwefsd", "-2143", "0.1738", "101"])
    def test_get_wait_time_std_from_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 1
        wait_time_std = sim.get_wait_time_std_from_input(sender_num)
        self.assertEqual(wait_time_std, 101)

    @patch("builtins.input", side_effect=[""])
    def test_get_wait_time_std_from_input_empty_input(self, mock_input):
        sim = Simulation()
        # The 1st sender
        sender_num = 1
        wait_time_std = sim.get_wait_time_std_from_input(sender_num)
        self.assertEqual(wait_time_std, 10)

    @patch("builtins.input", side_effect=["qweiofkje", "-1", "29432.234", "-19238", "3456"])
    def test_get_update_interval_from_input(self, mock_input):
        sim = Simulation()
        update_interval = sim.get_update_interval_from_input()
        self.assertEqual(update_interval, 3456)

    @patch("builtins.input", side_effect=[""])
    def test_get_update_interval_from_input(self, mock_input):
        sim = Simulation()
        update_interval = sim.get_update_interval_from_input()
        self.assertEqual(update_interval, 1000)


if __name__ == "__main__":
    unittest.main()
