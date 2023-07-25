import time

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read sensor state and save data to file
with open('sensor_data.txt', 'a') as file:
    try:
        from gpiozero import DigitalInputDevice
        # GPIO pin connected to the sensor's output
        sensor_pin = 17

        # Create a digital input device for the sensor
        sensor = DigitalInputDevice(sensor_pin)

        while True:
            # Generate current timestamp
            current_time = get_current_timestamp()

            # Get the sensor state (Object detected or not)
            sensor_state = "Object detected" if sensor.is_active else "No object detected"

            # Print and save sensor state with timestamp
            data_line = f"Electro-Optical Sensor:- Timestamp: {current_time:.6f}, Sensor State: {sensor_state}\n"
            print(data_line.strip())  # Print without newline
            file.write(data_line)

            # Wait for a short time before recording the next data point
            time.sleep(0.1)

    except ImportError:
        # GPIO pins not available, use simulated sensor state
        while True:
            # Generate current timestamp
            current_time = get_current_timestamp()

            # Simulate sensor state (Object detected or not)
            # Modify this line to simulate different sensor states if needed
            sensor_state = "Simulated Object detected"

            # Print and save sensor state with timestamp
            data_line = f"Electro-Optical Sensor:- Timestamp: {current_time:.6f}, Sensor State: {sensor_state}\n"
            print(data_line.strip())  # Print without newline
            file.write(data_line)

            # Wait for a short time before recording the next data point
            time.sleep(0.1)
