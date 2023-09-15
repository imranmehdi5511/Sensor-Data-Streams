import random
import time

# Function to generate a random motion detection (for simulation purposes)
def generate_random_motion():
    return random.choice([0, 1])  # Random motion detection (0: No motion, 1: Motion detected)

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the motion sensor and save data to file
with open('motion_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the motion sensor reading (random value for simulation)
        motion_detected = generate_random_motion()

        # Print and save motion sensor reading with timestamp
        data_line = f"Motion Sensor Data:- Timestamp: {current_time:.6f},Motion Detection: {motion_detected}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
