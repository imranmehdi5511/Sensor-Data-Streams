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
            save_data_to_file('stepper_motor_data.txt', f'Stepper Motor 28BYJ-48:- Direction: clockwise: Step {step_count}')

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
            save_data_to_file('stepper_motor_data.txt', f'Stepper Motor 28BYJ-48:- Direction: counterclockwise: Step {step_count}')
            #Data has been saved to file.
except KeyboardInterrupt:
    # Clean up any resources and exit on keyboard interrupt (Ctrl+C)
    pass
