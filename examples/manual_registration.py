"""
This example demonstrates how to manually register an exit handler with the ExitCallHandler.

In this example, we create a singleton instance of the ExitCallHandler and register an exit handler with it. The exit
handler will be called when the script exits.
"""
from easy_exit_calls import ExitCallHandler
from easy_exit_calls.example_helpers import clear_screen, simple_example_handler

from time import sleep


# Create the singleton instance of the ExitCallHandler
ECH = ExitCallHandler()


# Register the exit handler
ECH.register_handler(simple_example_handler)


# Main loop example
clear_screen()
for i in range(5):
    print(f"Main loop iteration {i}")
    sleep(1)


# When the script exits, the exit handler will be called
