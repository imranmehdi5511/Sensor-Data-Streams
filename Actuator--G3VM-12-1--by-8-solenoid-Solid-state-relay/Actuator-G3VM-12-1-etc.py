import numpy as np
import time

# Actuator characteristics
data_rate = 10  # Data rate in Hz
baud_rate = 9600  # Baud rate in bits per second
timing_resolution = 10e-3  # Timing resolution in seconds
frequency_response_low = 0.1  # Frequency response low limit in Hz
frequency_response_high = 1000  # Frequency response high limit in Hz

# Calculate the time step based on the data rate
time_step = 1 / data_rate

# Virtual actuator simulation
with open('actuator_data.txt', 'a') as file:
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate actuator behavior (Randomly open/close)
        actuator_state = "Open" if np.random.rand() < 0.5 else "Closed"

        # Print and save actuator state
        data_line = f"Actuator Solenoid Solid State Relay:- Timestamp: {current_time:.6f},Actuator State: {actuator_state}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on data rate
        time.sleep(time_step)
