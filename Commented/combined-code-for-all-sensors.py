#Actuator Solid State Relay
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of All import the required modules needed for the script. In this case the required module is time, and module numpy as np.
import numpy as np
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.1 and as high as 1000. We arbitrarily ran the script for data rate value of 10 but the value can be changed as well. The data rate is basically same as the frequency. 
# Actuator characteristics
data_rate = 10  # Data rate in Hz
baud_rate = 9600  # Baud rate in bits per second
timing_resolution = 10e-3  # Timing resolution in seconds
frequency_response_low = 0.1  # Frequency response low limit in Hz
frequency_response_high = 1000  # Frequency response high limit in Hz

# Calculate the time step based on the data rate
time_step = 1 / data_rate

# Virtual actuator simulation
with open('actuator_solenoid_solid_state_relay_data.txt', 'a') as file:
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate actuator behavior (Randomly open/close)
        actuator_state = "Open" if np.random.rand() < 0.5 else "Closed"

        # Print and save actuator state
        data_line = f"Actuator Solenoid Solid State Relay: Timestamp: {current_time:.6f},Actuator State: {actuator_state}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on data rate
        time.sleep(time_step)

#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.
#Actuator Stepper Motor
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of All import the required modules needed for the script. In this case the required module is time.
import time

# Define the stepper motor sequence (order of activation for each coil)
sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

# Function to save data to a text file
def save_data_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(f'{data}\n')

# Number of steps per revolution (full cycle) for the 28BYJ-48 motor
STEPS_PER_REVOLUTION = 4096

# Set the delay between steps to control the motor speed
delay = 0.001
#revolutions = 0
try:
    step_count = 0

    while True:
        # Rotate the stepper motor clockwise (forward) for one full revolution
        for _ in range(STEPS_PER_REVOLUTION):
            for step in range(8):
                # Set the stepper motor coil based on the step in the sequence
                for pin, value in zip([1, 2, 3, 4], sequence[step]):
                    # Simulate the stepper motor movement by printing the step and pin state
                    print(f'Step {step_count}: Pin {pin} = {value}')

                time.sleep(delay)

            # Update step count and save it to a text file
            step_count += 1
            #revolutions += 1
            save_data_to_file('actuator_stepper_motor_data.txt', f'Stepper Motor 28BYJ-48: Direction: clockwise: Step {step_count}')

        # Rotate the stepper motor counterclockwise (backward) for one full revolution
        for _ in range(STEPS_PER_REVOLUTION):
            for step in range(8):
                # Set the stepper motor coil based on the step in the sequence
                for pin, value in zip([1, 2, 3, 4], sequence[7 - step]):
                    # Simulate the stepper motor movement by printing the step and pin state
                    print(f'Step {step_count}: Pin {pin} = {value}')

                time.sleep(delay)

            # Update step count and save it to a text file
            step_count -= 1
            #revolutions += 1
            save_data_to_file('actuator_stepper_motor_data.txt', f'Stepper Motor 28BYJ-48: Direction: counterclockwise: Step {step_count}')
            #Data has been saved to file.
except KeyboardInterrupt:
    # Clean up any resources and exit on keyboard interrupt (Ctrl+C)
    pass
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Electro Optical Sensor
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of All import the required modules needed for the script. In this case the required module is time.
import time

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read sensor state and save data to file
with open('electro_optical_sensor_data.txt', 'a') as file:
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
            data_line = f"Electro-Optical Sensor: Timestamp: {current_time:.6f}, Sensor State: {sensor_state}\n"
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
            data_line = f"Electro-Optical Sensor: Timestamp: {current_time:.6f}, Sensor State: {sensor_state}\n"
            print(data_line.strip())  # Print without newline
            file.write(data_line)

            # Wait for a short time before recording the next data point
            time.sleep(0.1)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Field Devices and Switches
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
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
with open('field_devices_switch_data.txt', 'a') as file:
    switch_state = False  # Initial state is OFF (False)
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate switch state (ON/OFF)
        switch_state = not switch_state  # Toggle the state
        switch_state_str = "ON" if switch_state else "OFF"

        # Print and save switch state
        data_line = f"Switch Field Device: Timestamp: {current_time:.6f},Switch State: {switch_state_str}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on timing resolution
        time.sleep(timing_resolution)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Flow Sensor
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
    with open('flow_sensor_YF-S201_data.txt', 'a') as file:  # Open file in append mode
        file.write(f"Flow Sensor YF-S201 Data: Timestamp: {current_time:.6f},Flow Rate: {flow_rate:.2f}\n")

    # Wait for the next data point based on data rate
    time.sleep(time_step)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.
#You can add additional logic here to stop the data generation after a specific duration or based on a condition.
#Humidity Sensor Data
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module random.
import random
import time

# Function to generate a random humidity reading (for simulation purposes)
def generate_random_humidity():
    return random.uniform(30, 70)  # Random humidity reading between 30% and 70%

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the humidity sensor and save data to file
with open('humidity_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the humidity sensor reading (random value for simulation)
        humidity_reading = generate_random_humidity()

        # Print and save humidity sensor reading with timestamp
        data_line = f"Humidity Sensor Data: Timestamp: {current_time:.6f},Humidity Reading: {humidity_reading:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Light Sensor Data
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module random.

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
        data_line = f"Light Sensor Data: Timestamp: {current_time:.6f},Light Intensity: {light_intensity:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Phantom Sensor Data
#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
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
with open('phantom_all-in-one_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the sensor readings
        temperature_reading = generate_random_temperature()
        vibration_reading = generate_random_vibration()
        current_reading = generate_random_current()

        # Print and save sensor readings with timestamp
        data_line = f"Phantom All-in-One Sensor: Timestamp: {current_time:.6f},Temperature Reading: {temperature_reading:.2f},Vibration Reading: {vibration_reading:.2f},Current Reading: {current_reading:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Pressure Sensor

#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module numpy as np.

import numpy as np
import time
#We used the Following values for the virtual sensor script. The maximum and minimum possible values of Frequency can be as low as 0.01 and as high as 100000. We arbitrarily ran the script for data rate value of 100 but the value can be changed as well. The data rate is basically same as the frequency. 

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
    with open('pressure_sensor_MPX5010DP_data.txt', 'a') as file:  # Open file in append mode
        file.write(f"Pressure Sensor MPX5010DP: Timestamp: {current_time:.6f},Pressure: {pressure:.2f}\n")

    # Wait for the next data point based on data rate
    time.sleep(time_step)

    # You can add additional logic here to stop the data generation after a specific duration or based on a condition.
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Relay DPDT

#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
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
with open('relay_DPDT_12V_Device_data.txt', 'a') as file:
    relay_state = False  # Initial state is OFF (False)
    while True:
        # Generate current time stamp
        current_time = time.time()

        # Simulate relay state (ON/OFF)
        relay_state = not relay_state  # Toggle the state
        relay_state_str = "ON" if relay_state else "OFF"

        # Print and save relay state
        data_line = f"Relay DPDT 12V Device Data: Timestamp: {current_time:.6f}, Relay State Value: {relay_state_str}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for the next data point based on timing resolution
        time.sleep(timing_resolution)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Temperature Sensor Data

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
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.


#Vibration Sensor Data

#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module random.
import random
import time

# Function to generate a random vibration reading (for simulation purposes)
def generate_random_vibration():
    return random.uniform(0, 100)  # Random vibration reading between 0 and 100 units

# Function to generate timestamp in seconds with milliseconds precision
def get_current_timestamp():
    return time.time()

# Main loop to read the vibration sensor and save data to file
with open('vibration_sensor_data.txt', 'a') as file:
    while True:
        # Generate current timestamp
        current_time = get_current_timestamp()

        # Simulate the vibration sensor reading (random value for simulation)
        vibration_reading = generate_random_vibration()

        # Print and save vibration sensor reading with timestamp
        data_line = f"Vibration Sensor Data: Timestamp: {current_time:.6f}, Vibrations Reading: {vibration_reading:.2f}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#image sensor

#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module random.
import random
import time

# Function to generate a random image data (for simulation purposes)
def generate_random_image_data():
    #The values for image width and height have been set to 640 and 480 respectively, but we can alter them as well.
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
        data_line = f"Image Sensor Data: Timestamp: {current_time:.6f},Image Data: {image_data}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.

#Motion Sensor Data

#Important Note:-
#You can find the details of the maximum and minimum possible values of different parameters, that can be used for each of the sensor script in the files named 'Tested for Minimum Frequencies', and 'Tested for Maximum Frequencies.txt'. These files are located in the Sensor-Data-Streams/Commented/*.txt directory of this repository. 
#First of all import the required modules needed for the script. In this case the required module is time, and module random.
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
        data_line = f"Motion Sensor Data: Timestamp: {current_time:.6f},Motion Detection: {motion_detected}\n"
        print(data_line.strip())  # Print without newline
        file.write(data_line)

        # Wait for a short time before recording the next data point
        time.sleep(1)  # You can adjust the time interval (e.g., 0.5 for half a second)
#The time to sleep is basically the period taken to produce one value, see the 'Tested for Minimum Frequencies.txt' and 'Tested for Maximum Frequencies.txt', for details.
