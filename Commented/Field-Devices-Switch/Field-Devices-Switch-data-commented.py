#First of All import the required modules needed for the script. In this case the required module is time.
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.1 and as high as 1000. We arbitrarily ran the script for data rate value of 10 but the value can be changed as well. The data rate is basically same as the frequency. 
# Switch characteristics
data_rate = 10  # Data rate in Hz (Not directly applicable to a switch)
timing_resolution = 10e-3  # Timing resolution in seconds
frequency_response_low = 0.1  # Frequency response low limit in Hz
frequency_response_high = 1000  # Frequency response high limit in Hz

# Calculate the time step based on the data rate (for simulation purposes)
time_step = 1 / data_rate if data_rate > 0 else 0

# Virtual switch simulation
with open('switch_data.txt', 'a') as file:
    switch_state = False  # Initial state is OFF (False)
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate switch state (ON/OFF)
        switch_state = not switch_state  # Toggle the state
        switch_state_str = "ON" if switch_state else "OFF"

        # Print and save switch state
        data_line = f"Switch Field Device:- Timestamp: {current_time:.6f},Switch State: {switch_state_str}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on timing resolution
        time.sleep(timing_resolution)
