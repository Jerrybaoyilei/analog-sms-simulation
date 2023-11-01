import unittest
from Producer import Producer


class TestProducer(unittest.TestCase):

    def setUp(self):
        # Create a Producer instance to test
        self.producer = Producer()

    def test_get_num_messages(self):
        self.assertEqual(self.producer.get_num_messages(), 1000)

    def test_set_num_messages(self):
        self.producer.set_num_messages(1234)
        self.assertEqual(self.producer.get_num_messages(), 1234)

    def test_set_num_messages_negative_int(self):
        self.producer.set_num_messages(-1234)
        # self.num_messages should not be updated
        self.assertEqual(self.producer.get_num_messages(), 1000)

    def test_set_num_messages_float(self):
        self.producer.set_num_messages(5678)
        self.assertEqual(self.producer.get_num_messages(), 5678)
        self.producer.set_num_messages(1234.5)
        # self.num_messages should not be updated
        self.assertEqual(self.producer.get_num_messages(), 5678)

    def test_set_num_messages_string(self):
        self.producer.set_num_messages(5678)
        self.assertEqual(self.producer.get_num_messages(), 5678)
        self.producer.set_num_messages("1234")
        # self.num_messages should not be updated
        self.assertEqual(self.producer.get_num_messages(), 5678)

    def test_get_max_message_length(self):
        self.assertEqual(self.producer.get_max_message_length(), 100)

    def test_set_max_message_length(self):
        self.producer.set_max_message_length(89)
        print(self.producer.get_max_message_length())
        self.assertEqual(self.producer.get_max_message_length(), 89)

    def test_set_max_message_length_negative_int(self):
        self.producer.set_max_message_length(89)
        self.assertEqual(self.producer.get_max_message_length(), 89)
        self.producer.set_max_message_length(-89)
        # self.max_message_length should not be updated
        self.assertEqual(self.producer.get_max_message_length(), 89)

    def test_set_max_message_length_float(self):
        self.producer.set_max_message_length(89)
        self.assertEqual(self.producer.get_max_message_length(), 89)
        self.producer.set_max_message_length(89.5)
        # self.max_message_length should not be updated
        self.assertEqual(self.producer.get_max_message_length(), 89)

    def test_set_max_message_length_string(self):
        self.producer.set_max_message_length(89)
        self.assertEqual(self.producer.get_max_message_length(), 89)
        self.producer.set_max_message_length("89")
        # self.max_message_length should not be updated
        self.assertEqual(self.producer.get_max_message_length(), 89)

    # At the moment, there should be no messages in the list
    # In the next test method, it will be checked again when there are messages in the list
    def test_get_messages(self):
        self.assertEqual(len(self.producer.get_messages()), 0)

    def test_generate_messages(self):
        self.producer.set_num_messages(89)
        self.producer.set_max_message_length(64)
        self.producer.generate_messages()
        # Check the total number of messages generated
        self.assertEqual(len(self.producer.get_messages()), 89)
        # For each message, check the length is within the max message length bound
        for message in self.producer.get_messages():
            self.assertLessEqual(len(message), 64)


if __name__ == '__main__':
    unittest.main()
