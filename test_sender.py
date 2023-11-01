import unittest
from Sender import Sender


class TestSender(unittest.TestCase):

    def setUp(self):
        self.sender = Sender(
            failure_rate=0.2, wait_time_mean=100, wait_time_std=20)

    def test_add_message_to_queue(self):
        self.sender.add_message_to_queue("Test Message")
        self.assertEqual(self.sender.messages_queue.qsize(), 1)

    def test_get_success_counter(self):
        self.assertEqual(self.sender.get_success_counter(), 0)

    def test_reset_success_counter(self):
        self.sender.success_counter = 89
        self.sender.reset_success_counter()
        self.assertEqual(self.sender.success_counter, 0)

    def test_get_failure_counter(self):
        self.assertEqual(self.sender.get_failure_counter(), 0)

    def test_reset_failure_counter(self):
        self.sender.failure_counter = 64
        self.sender.reset_failure_counter()
        self.assertEqual(self.sender.failure_counter, 0)

    def test_get_total_time(self):
        self.assertEqual(self.sender.get_total_time(), 0)

    def test_reset_total_time(self):
        self.sender.total_time = 1357
        self.sender.reset_total_time()
        self.assertEqual(self.sender.total_time, 0)


if __name__ == '__main__':
    unittest.main()
