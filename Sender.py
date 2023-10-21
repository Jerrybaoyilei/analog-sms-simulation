import queue
import random


class Sender:

    def __init__(self, failure_rate=0, wait_time_mean=100, wait_time_std=20):
        self.messages_queue = queue.Queue()
        self.success_counter, self.failure_counter, self.total_time, self.average_time = 0, 0, 0, 0
        self.failure_rate = failure_rate
        self.wait_time_mean = wait_time_mean
        self.wait_time_std = wait_time_std

    def fill_messages_queue(self, message, num_messages):
        for i in range(num_messages):
            self.messages_queue.put(message)

    def send_message(self):
        message = self.messages_queue.get()
        # Prevent negative wait time
        wait_time = max(0, random.normalvariate(
            self.wait_time_mean, self.wait_time_std))
        # Update total time
        self.total_time += wait_time
        # Update average time per message
        self.average_time = self.total_time / self.success_counter
        rand_failure = random.random()
        # If fail, put the message back in the queue
        if rand_failure < self.failure_rate:
            self.failure_counter += 1
            self.messages_queue.put(message)
        else:
            self.success_counter += 1
