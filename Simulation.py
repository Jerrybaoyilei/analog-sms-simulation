from producer import Producer
from sender import Sender
from monitor import Monitor
import threading


class Simulation:

    def get_num_messages_from_input(self, default_value):
        input_num_messages = input(
            "How many messages would you like to send? Please provide an integer value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
        while True:
            if input_num_messages.strip() == "":
                return default_value
            try:
                num_messages = int(input_num_messages)
                if num_messages > 0:
                    return num_messages
                # Deal wtih negative number
                else:
                    print("Please provide a positive integer velue.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive integer.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_max_message_length_from_input(self, default_value):
        input_max_message_length = input(
            "What is the maximum length of each message? Please provide an integer value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
        while True:
            if input_max_message_length.strip() == "":
                return default_value
            try:
                max_message_length = int(input_max_message_length)
                # Negative number
                if max_message_length > 0:
                    return max_message_length
                else:
                    print("Please provide a positive integer velue.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive integer.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_num_sender_from_input(self, num_messages, default_value):
        input_num_senders = input(
            "How many senders would you like to use? Please provide an integer value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
        while True:
            if input_num_senders.strip() == "":
                return default_value
            try:
                num_senders = int(input_num_senders)
                # Negative number
                if num_senders > 0:
                    if num_senders > num_messages:
                        print(
                            "The number of senders cannot be greater than the number of messages. Please try again.\n")
                    else:
                        return num_senders
                else:
                    print("Please provide a positive integer velue.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive integer.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_failure_rate_from_input(self, default_value):
        input_failure_rate = input(
            "What is the failure rate of each sender? Please provide a float value between 0 and 1. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
        while True:
            if input_failure_rate.strip() == "":
                return default_value
            try:
                failure_rate = float(input_failure_rate)
                # Deal with out of range failure rate
                if failure_rate >= 0 and failure_rate <= 1:
                    return failure_rate
                # Deal with out of range failure rate
                else:
                    print("Please provide a float value between 0 and 1.\n")
            except ValueError:
                print("Invalid input. Please provide a valid float.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_wait_time_mean_from_input(self, default_value):
        input_wait_time_mean = input(
            "What is the mean wait time in ms of each sender? Please provide a positive int value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
        while True:
            if input_wait_time_mean.strip() == "":
                return default_value
            try:
                wait_time_mean = int(input_wait_time_mean)
                # Negative number
                if wait_time_mean > 0:
                    return wait_time_mean
                else:
                    print("Please provide a positive float value for mean wait time.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive float.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_wait_time_std_from_input(self, default_value):
        while True:
            input_wait_time_std = input(
                "What is the standard deviation of the wait time in ms of each sender? Please provide a positive int value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
            if input_wait_time_std.strip() == "":
                return default_value
            try:
                wait_time_std = int(input_wait_time_std)
                # Negative number
                if wait_time_std > 0:
                    return wait_time_std
                else:
                    print(
                        "Please provide a positive float value for standard deviation of wait time.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive float.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def get_update_interval_from_input(self, default_value):
        while True:
            input_update_interval = input(
                "What is the update interval in ms of the monitor? Please provide a positive integer value. If you do not provide a value, the default value of {default_value} will be used.\n".format(default_value=default_value))
            if input_update_interval.strip() == "":
                return default_value
            try:
                update_interval = int(input_update_interval)
                # Negative number
                if update_interval > 0:
                    return update_interval
                else:
                    print(
                        "Please provide a positive float value for the update interval.\n")
            except ValueError:
                print("Invalid input. Please provide a valid positive float.\n")
            except OverflowError:
                print("The number you provided is too large. Please try again.\n")
            except TypeError:
                print(
                    "The input you provided is not a valid number or string. Please try again.\n")

    def main(self):
        # Create a new producer with the given number of messages and max message length
        num_messages = self.get_num_messages_from_input(1000)
        max_message_length = self.get_max_message_length_from_input(100)
        producer = Producer(
            num_messages, max_message_length)
        producer.generate_messages()

        # Obtain parameters for Senders
        num_senders = self.get_num_sender_from_input(num_messages, 10)
        failure_rate = self.get_failure_rate_from_input(0.2)
        wait_time_mean = self.get_wait_time_mean_from_input(100)
        wait_time_std = self.get_wait_time_std_from_input(20)
        # Generate senders
        senders = []
        for i in range(num_senders):
            senders.append(Sender(failure_rate=failure_rate,
                           wait_time_mean=wait_time_mean, wait_time_std=wait_time_std))

        # Give each sender a copy of the messages
        # Calculate the number of messages each sender will send
        num_messages_per_sender = num_messages // num_senders
        # Calculate the remainder of messages
        remainder = num_messages % num_senders
        # Distribute the messages among the senders
        for i in range(num_senders):
            for j in range(num_messages_per_sender):
                message = producer.get_messages(
                )[i * num_messages_per_sender + j]
                senders[i].add_message_to_queue(message)
        # Distribute the remainder of messages
        for i in range(remainder):
            message = producer.get_messages(
            )[num_messages - remainder + i]
            senders[i].add_message_to_queue(message)

        # Obtain the update interval for the monitor
        update_interval = self.get_update_interval_from_input(10)
        # Create a new monitor with the given update interval
        monitor = Monitor(update_interval, senders)

        # Create threads for each sender, and a thraed for the monitor
        sender_threads = [threading.Thread(
            target=sender.send_messages) for sender in senders]
        monitor_thread = threading.Thread(
            target=monitor.begin_monitor, args=(num_messages,))

        # Start the threads
        for thread in sender_threads:
            thread.start()
        monitor_thread.start()
        # Wait for the threads to finish
        for thread in sender_threads:
            thread.join()
        monitor_thread.join()

        sys.exit()


if __name__ == "__main__":
    simulation = Simulation()
    simulation.main()
