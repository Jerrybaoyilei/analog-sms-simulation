import queue
import random
import string


class Producer:

    def __init__(self, num_messages=1000, max_message_length=100):
        self.num_messages = num_messages
        self.max_message_length = max_message_length
        self.messages_list = []

    def get_num_messages(self):
        return self.num_messages

    def set_num_messages(self, num_message):
        # check if num_message is a positive integer and update self.num_messages
        if isinstance(num_message, int) and num_message > 0:
            self.num_messages = num_message
            self.generate_messages()
        else:
            print("Invalid value for num_message. It must be a positive integer.")

    def get_max_message_length(self):
        return self.max_message_length

    def set_max_message_length(self, max_message_length):
        if isinstance(max_message_length, int) and max_message_length > 0:
            # If the new max message length is less than the current message length, recreate messages
            if self.max_message_length < max_message_length:
                print(
                    "Updating messages to conform with the new maximum length of {max_message_length} characters".format(max_message_length=self.max_message_length))
                self.max_message_length = max_message_length
                self.generate_messages()
            else:
                self.max_message_length = max_message_length
        else:
            print(
                "Invalid value for max_message_length. It must be a positive integer.")

    def get_messages(self):
        return self.messages_list

    def generate_messages(self):
        self.messages_list.clear()
        characters = string.ascii_letters + string.digits + \
            string.punctuation + string.whitespace
        # Generate messages made up of random characters
        for i in range(self.num_messages):
            message = ''.join(random.choice(characters)
                              for _ in range(random.randint(1, self.max_message_length)))
            self.messages_list.append(message)
