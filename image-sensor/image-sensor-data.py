import random
import time

# Function to generate a random image data (for simulation purposes)
def generate_random_image_data():
    image_width = 640
    image_height = 480
    image_data = []
    for _ in range(image_height):
        row = [random.randint(0, 255) for _ in range(image_width)]
        image_data.append(row)
    return image_data

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the image sensor and save data to file
with open('image_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the image sensor reading (random image data for simulation)
        image_data = generate_random_image_data()

        # Print and save image sensor reading with timestamp
        data_line = f"Image Sensor Data:- Timestamp: {current_time:.6f},Image Data: {image_data}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
