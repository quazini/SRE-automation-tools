#!/usr/bin/env python3

import subprocess
import sys

def get_filesystem_info():
    """
    Get information about mounted filesystems using the 'df' command.
    Returns a list of tuples containing filesystem info.
    """
    # Run the 'df' command and capture its output. The '-h' flag gives us human-readable sizes.
    df_command_output = subprocess.check_output(['df', '-h']).decode('utf-8')
    
    # Split the output into lines and ignore the header (first line)
    output_lines = df_command_output.strip().split('\n')[1:]
    
    filesystem_list = []
    for line in output_lines:
        # Split each line into columns. Each column represents different info about the filesystem.
        column_data = line.split()
        # Make sure we have all the data we need (should be at least 6 columns)
        if len(column_data) >= 6:
            # Extract all the juicy details about this filesystem
            device_name = column_data[0]
            total_size = column_data[1]
            used_space = column_data[2]
            available_space = column_data[3]
            used_percentage = int(column_data[4].rstrip('%'))  # Remove the '%' sign and convert to int
            mount_point = column_data[5]
            
            # Pack all this info into a tuple and add it to our list
            filesystem_list.append((device_name, total_size, used_space, available_space, used_percentage, mount_point))
    
    return filesystem_list

def main():
    # First things first: let's figure out what threshold we're working with
    if len(sys.argv) == 2:
        # If the user provided a threshold as an argument, let's use that
        try:
            free_space_threshold = int(sys.argv[1])
        except ValueError:
            # Oops! The user didn't give us a valid number. Let's tell them and quit.
            print("Error: Free space threshold must be an integer")
            sys.exit(1)
    else:
        # No threshold provided? No problem! We'll ask for one.
        while True:
            try:
                free_space_threshold = int(input("Please enter the free space threshold percentage: "))
                break
            except ValueError:
                print("Error: Please enter a valid integer.")

    # Time to get the lowdown on our filesystems
    filesystem_info = get_filesystem_info()
    
    # This flag will help us remember if we saw any filesystems below the threshold
    warning_flag = False
    
    # Let's check out each filesystem one by one
    for fs in filesystem_info:
        device_name, total_size, used_space, available_space, used_percentage, mount_point = fs
        free_space_percentage = 100 - used_percentage
        
        # Print out all the details. Knowledge is power!
        print(f"Filesystem: {device_name}")
        print(f"Mount Point: {mount_point}")
        print(f"Total Size: {total_size}")
        print(f"Used Space: {used_space}")
        print(f"Available Space: {available_space}")
        print(f"Free Space Percentage: {free_space_percentage}%")
        print()
        
        # Uh-oh, this filesystem is running low on space. Let's raise a red flag!
        if free_space_percentage < free_space_threshold:
            print(f"Warning: Free space on {device_name} ({mount_point}) is below {free_space_threshold}%")
            print()
            warning_flag = True
    
    # Time to say goodbye. But first, let's set the exit code.
    # If we saw any warnings, we'll exit with 1 to indicate something's up.
    if warning_flag:
        sys.exit(1)
    else:
        # All clear! We'll exit with 0 to show everything's peachy.
        sys.exit(0)

# This is where the magic happens. If this script is run (not imported), kick off the main function!
if __name__ == "__main__":
    main()