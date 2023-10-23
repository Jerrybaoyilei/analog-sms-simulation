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
        self.num_messages = num_message
        self.generate_messages(
            self.characters, self.max_message_length, self.num_messages)

    def get_max_message_length(self):
        return self.max_message_length

    def set_max_message_length(self, max_message_length):
        # If the new max message length is less than the current message length, recreate messages
        if self.max_message_length < max_message_length:
            print(
                "Updating messages to conform with the new maximum length of {max_message_length} characters".format(max_message_length=self.max_message_length))
        self.max_message_length = max_message_length
        self.generate_messages()

    def get_characters(self):
        return self.characters

    def set_characters(self, characters):
        self.characters = characters
        self.generate_messages(
            self.characters, self.max_message_length, self.num_messages)

    def get_messages(self):
        return self.messages_list

    def generate_messages(self):
        self.messages_list.clear()
        characters = string.ascii_letters + string.digits + string.punctuation
        for i in range(self.num_messages):
            message = ''.join(random.choice(characters)
                              for _ in range(random.randint(1, self.max_message_length)))
            self.messages_list.append(message)
