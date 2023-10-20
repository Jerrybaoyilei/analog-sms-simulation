class Producer:

    def __init__(self, message="", num_message=1000, max_message_length=100):
        self.num_message = num_message
        self.max_message_length = max_message_length
        self.message = message
        self.messages = []
        # message is too long, warn the user that it will be segmented into multiple messages when sent
        if len(self.message) > self.max_message_length:
            print(
                "Message is longer than max length of (${self.max_message_length}); it will be segmented into multiple messages when sent.")

    def get_num_message(self):
        return self.num_message

    def set_num_message(self, num_message):
        if num_message < 1:
            print("Number of messages must be greater than 0. Please try again.")
            return
        self.num_message = num_message
        self.set_messages()

    def get_message(self):
        return self.message

    def set_message(self, message):
        if len(message) > self.max_message_length:
            print(
                "Message is longer than max length of (${self.max_message_length}); it will be segmented into multiple messages when sent.")
        self.message = message
        self.set_messages()

    def get_max_message_length(self):
        return self.max_message_length

    def set_max_message_length(self, max_message_length):
        if max_message_length < 1:
            print("Messages cannot be empty. Please try again.")
            return
        self.max_message_length = max_message_length

    def set_messages(self):
        self.messages.clear()
        for i in range(self.num_message):
            self.messages.append(self.message)
