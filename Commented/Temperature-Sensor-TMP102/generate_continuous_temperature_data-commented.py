#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module numpy as np.
import numpy as np
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.5 and as high as 10000. We arbitrarily ran the script for data rate value of 400 but the value can be changed as well. The data rate is basically same as the frequency. 
# Sensor characteristics
data_rate = 400  # Data rate in Hz
baud_rate = 115200  # Baud rate in bits per second
timing_resolution = 125e-6  # Timing resolution in seconds
frequency_response_low = 0.5  # Frequency response low limit in Hz
frequency_response_high = 10000  # Frequency response high limit in Hz
temperature_range = (-40, 125)  # Temperature range in Celsius

# Calculate the time step based on the data rate
time_step = 1 / data_rate

# Generate temperature data indefinitely
while True:
    # Generate current time stamp
    current_time = time.time()
    
    # Generate synthetic temperature data
    temperature = np.random.uniform(temperature_range[0], temperature_range[1])

    # Save the data to a text file
    with open('temperature_sensor_TMP102_data.txt', 'a') as file:  # Open file in append mode
        file.write(f"Temperature Sensor TMP102 Data: Timestamp:{current_time:.6f},Temperature:{temperature:.2f} Degree Celsius\n")

    # Wait for the next data point based on data rate
    time.sleep(time_step)

    # You can add additional logic here to stop the data generation after a specific duration or based on a condition.
