#First of all import the required modules needed for the script. In this case the required module is time, and module numpy as np.
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.1 and as high as 1000. We arbitrarily ran the script for data rate value of 10 but the value can be changed as well. The data rate is basically same as the frequency. 
# Relay characteristics
data_rate = 10  # Data rate in Hz (Not directly applicable to a relay)
timing_resolution = 10e-3  # Timing resolution in seconds
frequency_response_low = 0.1  # Frequency response low limit in Hz
frequency_response_high = 1000  # Frequency response high limit in Hz

# Calculate the time step based on the data rate (for simulation purposes)
time_step = 1 / data_rate if data_rate > 0 else 0

# Virtual relay simulation
with open('relay_data.txt', 'a') as file:
    relay_state = False  # Initial state is OFF (False)
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate relay state (ON/OFF)
        relay_state = not relay_state  # Toggle the state
        relay_state_str = "ON" if relay_state else "OFF"

        # Print and save relay state
        data_line = f"Relay DPDT 12V Device Data:- Timestamp: {current_time:.6f}, Relay State Value: {relay_state_str}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on timing resolution
        time.sleep(timing_resolution)
