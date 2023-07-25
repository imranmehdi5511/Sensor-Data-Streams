import random
import time

# Function to generate a random light intensity reading (for simulation purposes)
def generate_random_light_intensity():
    return random.uniform(0, 1000)  # Random light intensity between 0 and 1000 lux

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the light sensor and save data to file
with open('light_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the light sensor reading (random value for simulation)
        light_intensity = generate_random_light_intensity()

        # Print and save light sensor reading with timestamp
        data_line = f"Light Sensor Data:- Timestamp: {current_time:.6f},Light Intensity: {light_intensity:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
