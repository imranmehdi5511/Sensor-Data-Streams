import os
import time

def main():
    # create a mega text file if it doesn't exist
    if not os.path.exists('mega_text_file.txt'):
        open('mega_text_file.txt', 'w').close()

    # read the file with folder names
    with open('folders.txt', 'r') as file:
        folder_names = file.readlines()

    # dictionary to store the last read position for each file
    last_positions = {}

    # infinite loop to continuously update the mega text file
    while True:
        with open('mega_text_file.txt', 'a') as mega_file:
            # loop through the folder names
            for folder_name in folder_names:
                folder_name = folder_name.strip()
                files = os.listdir(folder_name)
                # loop through the files in the folder
                for file in files:
                    # check if file is txt file
                    if file.endswith('.txt'):
                        file_path = os.path.join(folder_name, file)

                        # get the last read position for the file
                        last_position = last_positions.get(file_path, 0)

                        # open the text file in binary mode to handle newlines properly
                        with open(file_path, 'rb') as text_file:
                            # move to the last read position
                            text_file.seek(last_position)
                            # read the new data from the text file
                            new_data = text_file.read()

                            # write the new data to the mega text file
                            mega_file.write(new_data.decode())

                            # update the last read position for the file
                            last_positions[file_path] = text_file.tell()

        # sleep for 1 second before updating the mega text file again
        time.sleep(1)

if __name__ == '__main__':
    main()
    
