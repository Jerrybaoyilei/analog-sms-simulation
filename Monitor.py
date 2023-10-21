import Producer
import Sender


class Monitor:

    def __init__(self, update_interval):
        self.update_interval = update_interval
        self.num_senders = num_senders
        self.averge_times = []
        self.num_successes = []
        self.num_failures = []

    def get_update_interval(self):
        return self.update_interval

    def set_update_interval(self, update_interval):
        self.update_interval = update_interval

    def get_num_senders(self):
        return self.num_senders

    def set_num_senders(self, num_senders):
        self.num_senders = num_senders

    # def begin_monitor(self):
