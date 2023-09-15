#First of all import the required modules needed for the script. In this case the required module is time, and module random.
import random
import time

# Function to generate a random temperature reading (in Celsius)
def generate_random_temperature():
    return random.uniform(-40.0, 125.0)  # Random temperature between 20.0°C and 30.0°C

# Function to generate a random vibration reading
def generate_random_vibration():
    return random.uniform(0.0, 1.0)  # Random vibration between 0.0 and 1.0 (arbitrary units)

# Function to generate a random current reading (in Amperes)
def generate_random_current():
    return random.uniform(0.0, 50.0)  # Random current between 0.0A and 5.0A

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the virtual sensor and save data to file
with open('sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the sensor readings
        temperature_reading = generate_random_temperature()
        vibration_reading = generate_random_vibration()
        current_reading = generate_random_current()

        # Print and save sensor readings with timestamp
        data_line = f"Phantom All-in-One Sensor:- Timestamp: {current_time:.6f},Temperature Reading: {temperature_reading:.2f},Vibration Reading: {vibration_reading:.2f},Current Reading: {current_reading:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
