from producer import Producer
from sender import Sender
import time


class Monitor:

    def __init__(self, update_interval, senders_list):
        self.update_interval = update_interval
        self.senders_list = senders_list

    def get_update_interval(self):
        return self.update_interval

    def set_update_interval(self, update_interval):
        self.update_interval = update_interval

    def record(self, report_counter, total_num_messages):
        total_num_successes = sum([sender.get_success_counter()
                                  for sender in self.senders_list])
        total_num_failures = sum([sender.get_failure_counter()
                                 for sender in self.senders_list])
        # Prevent division by zero
        if total_num_successes == 0:
            overall_average_time_per_message = "N/A"
        else:
            overall_average_time_per_message = sum(
                [sender.get_total_time() for sender in self.senders_list]) / total_num_successes
        print("================================")
        print(f"Report #{report_counter}\n")
        print(f"Total number of successes: {total_num_successes}\n")
        print(f"Total number of failures: {total_num_failures}\n")
        print(
            f"Average time per message sent: {overall_average_time_per_message}\n")
        print("================================")
        # Set a termination condition for recording so it won't record forever after all messages have been sent
        if total_num_successes == total_num_messages:
            return True
        else:
            return False

    def begin_monitor(self, total_num_messages):
        report_counter = 0
        reached_end = False
        while not reached_end:
            time.sleep(self.update_interval/1000)
            report_counter += 1
            reached_end = self.record(report_counter, total_num_messages)
