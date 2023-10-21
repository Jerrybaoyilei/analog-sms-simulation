class Producer:

    def __init__(self, num_senders, message="", num_message=1000, max_message_length=100):
        self.num_senders = num_senders
        self.message = message
        self.num_message = num_message
        self.max_message_length = max_message_length
        self.set_messages()

    def get_num_senders(self):
        return self.num_senders

    def set_num_senders(self, num_senders):
        self.num_senders = num_senders
        self.set_messages()

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
        # If the max_message_length is less than the length of the message, then truncate the message
        if self.max_message_length < len(self.message):
            print(
                "Truncating message to max_message_length; you can always set the message to a shorter message")
            self.message = self.message[:self.max_message_length]
            self.set_messages()

    def set_messages(self):
        self.messages = [[] for _ in range(self.num_senders)]
        # Calculate the number of messages per sender
        num_messages_per_sender = self.num_message // self.num_senders
        # Calculate the number of messages left over (i.e., n), which will be assigned to the first nth senders
        num_messages_left = self.num_message % self.num_senders
        # Assign the messages to the senders
        for i in range(self.num_senders):
            for j in range(num_messages_per_sender):
                self.messages[i].append(self.message)
            # Assign the leftover messages to the first nth senders
            if i < num_messages_left:
                self.messages[i].append(self.message)
