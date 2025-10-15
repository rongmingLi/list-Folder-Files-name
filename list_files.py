import os

import datetime

def save_all_files(directory, output_file):
    """
    Lists all files in a given directory and its subdirectories and saves them to a file.
    If the output file already exists, a timestamp is appended to the filename.
    """
    base_name, extension = os.path.splitext(output_file)
    counter = 1
    final_output_file = output_file
    while os.path.exists(final_output_file):
        final_output_file = f"{base_name}_{counter}{extension}"
        counter += 1

    with open(final_output_file, 'w') as f:
        f.write(f"Listing files in: {directory}\n\n")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(f"{file_path}\n")
    return final_output_file

if __name__ == "__main__":
    # Allow the user to manually input the directory path
    directory_to_list = input("Enter the directory path to list files (press Enter for current directory): ")
    if not directory_to_list:
        directory_to_list = os.getcwd() # Use current directory if no input

    output_filename = "file_list.txt"
    final_output_filename = save_all_files(directory_to_list, output_filename)
    print(f"File list saved to {final_output_filename}")