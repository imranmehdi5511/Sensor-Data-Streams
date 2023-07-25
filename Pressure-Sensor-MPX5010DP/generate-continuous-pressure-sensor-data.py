import numpy as np
import time

# Sensor characteristics
data_rate = 100  # Data rate in Hz
baud_rate = 9600  # Baud rate in bits per second
timing_resolution = 1e-3  # Timing resolution in seconds
frequency_response_low = 0.01  # Frequency response low limit in Hz
frequency_response_high = 100000  # Frequency response high limit in Hz
pressure_range = (0, 100)  # Pressure range in units (e.g., kPa, psi)

# Calculate the time step based on the data rate
time_step = 1 / data_rate

# Generate pressure data indefinitely
while True:
    # Generate current time stamp
    current_time = time.time()
    
    # Generate synthetic pressure data
    pressure = np.random.uniform(pressure_range[0], pressure_range[1])

    # Save the data to a text file
    with open('pressure_data.txt', 'a') as file:  # Open file in append mode
        file.write(f"Pressure Sensor MPX5010DP:- Timestamp: {current_time:.6f},Pressure: {pressure:.2f}\n")

    # Wait for the next data point based on data rate
    time.sleep(time_step)

    # You can add additional logic here to stop the data generation after a specific duration or based on a condition.
