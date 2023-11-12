from cryptography.fernet import Fernet
import os

try:
    # Get the current directory
    current_directory = os.getcwd()

    # Initialize an empty list to store the filenames
    txt_files = []

    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file ends with '.txt'
        if filename.endswith('.txt'):
            # Add the filename to the list
            txt_files.append(filename)

    # Print the list of .txt files
    print(txt_files)

    with open("key.key", "rb") as key:
        secretkey = key.read()

    print("\n\n")

    for file in txt_files:
        with open(file, 'rb') as thfile:
            content = thfile.read()
        constent_dencrypt = Fernet(secretkey).decrypt(content)

        with open(file, 'wb') as thfile:
            thfile.write(constent_dencrypt)
except:
    print('Cannot decrypt your files: Invalid key')





