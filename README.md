# analog-sms-simulation

## How to run the program?

1. Open terminal and navigate to the folder containing all the python files.
2. In terminal, run "python simulation.py"
3. Follow the instruction in the terminal
4. If you want to terminate the program, press ctrl+c like how you would exit any other python program from terminal.

## What is this program?

This is a small program that simulates sending many messages via a number of senders. Each message contains random characters up to a configurable maximum length.  
There is one producer that produces a configurable number of messages.
There are a configurable number of senders who gets the messages they need to send and send them. Each sending action has a wait time to simulate the actual sending process, and a failure rate. If one message fails to send, it will be added back to the message queue for this sender.  
There is also a monitor that prints out key information periodically (i.e., a configurable amount of interval time), including the total number of successfully sent messages, the total number of messages that failed to be sent, and the average time of sending one message. Notice if one message fails to send, its wait time still contributes to the total wait time, but the number of successfully sent messages will not be incremented.  
Finally, the simulation class set up the message producer, senders, and the monitor from user input in terminal, and run the simulation.  

## What online resources have I used?

1. Python documentation, specifically on unit testing and multi threading.
2. Some usage of stack overflow when I ran into some errors I could not solve for a longer time.
