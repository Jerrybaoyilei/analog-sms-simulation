import queue
import random
import time


class Sender:

    def __init__(self, failure_rate=0, wait_time_mean=100, wait_time_std=20):
        self.messages_queue = queue.Queue()
        self.success_counter, self.failure_counter, self.total_time, self.average_time = 0, 0, 0, 0
        self.failure_rate = failure_rate
        self.wait_time_mean = wait_time_mean
        self.wait_time_std = wait_time_std

    def add_message_to_queue(self, message):
        self.messages_queue.put(message)

    def send_message(self):
        try:
            message = self.messages_queue.get()
            # Prevent negative wait time
            wait_time = max(0, random.normalvariate(
                self.wait_time_mean, self.wait_time_std))
            # Wait to simulating sending a message, in ms
            time.sleep(wait_time / 1000)
            # Update total time
            self.total_time += wait_time
            # Simluating a failure
            rand_failure = random.random()
            # If failure, put the message back in the queue
            if rand_failure < self.failure_rate:
                self.failure_counter += 1
                self.messages_queue.put(message)
            # If success, update success counter and average time
            else:
                self.success_counter += 1
                # Update average time per message
                self.average_time = self.total_time / self.success_counter
        except queue.Empty:
            return
