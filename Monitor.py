import Producer
import Sender


class Monitor:

    def __init__(self, update_interval):
        self.update_interval = update_interval
        self.averge_times = []
        self.num_successes = []
        self.num_failures = []

    def get_update_interval(self):
        return self.update_interval

    def set_update_interval(self, update_interval):
        self.update_interval = update_interval

    def begin_monitor(self):
        total_num_successes = sum(self.num_successes)
        total_num_failures = sum(self.num_failures)
        total_average_time = sum([average_time * num_success for average_time, num_success in zip(
            self.average_times, self.num_successes)]) / total_num_successes
        print(f"Total number of successes: {total_num_successes}")
        print(f"Total number of failures: {total_num_failures}")
        print(f"Average time per message sent: {total_average_time}")
