class Producer:

    def __init__(self, message="", num_message=1000, max_message_length=100):
        self.num_message = num_message
        self.max_message_length = max_message_length
        self.message = message
        self.messages = []

    def get_num_message(self):
        return self.num_message

    def set_num_message(self, num_message):
        self.num_message = num_message
        self.set_messages()

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message
        self.set_messages()

    def get_max_message_length(self):
        return self.max_message_length

    def set_max_message_length(self, max_message_length):
        self.max_message_length = max_message_length

    def set_messages(self):
        self.messages.clear()
        for i in range(self.num_message):
            self.messages.append(self.message)
