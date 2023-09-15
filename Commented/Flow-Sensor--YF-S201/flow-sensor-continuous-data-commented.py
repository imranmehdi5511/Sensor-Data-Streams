#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module numpy as np.
import numpy as np
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.1 and as high as 1000. We arbitrarily ran the script for data rate value of 50 but the value can be changed as well. The data rate is basically same as the frequency. 
# Sensor characteristics
data_rate = 50  # Data rate in Hz
baud_rate = 9600  # Baud rate in bits per second
timing_resolution = 10e-3  # Timing resolution in seconds
frequency_response_low = 0.1  # Frequency response low limit in Hz
frequency_response_high = 1000  # Frequency response high limit in Hz

# Calculate the time step based on the data rate
time_step = 1 / data_rate

# Generate flow data indefinitely
while True:
    # Generate current time stamp
    current_time = time.time()
    
    # Generate synthetic flow data (pulses per second)
    flow_rate = np.random.uniform(frequency_response_low, frequency_response_high)

    # Save the data to a text file
    with open('flow_data.txt', 'a') as file:  # Open file in append mode
        file.write(f"Flow Sensor YF-S201 Data:- Timestamp: {current_time:.6f},Flow Rate: {flow_rate:.2f}\n")

    # Wait for the next data point based on data rate
    time.sleep(time_step)

    # You can add additional logic here to stop the data generation after a specific duration or based on a condition.
