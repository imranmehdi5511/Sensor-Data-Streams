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
