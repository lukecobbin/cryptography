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

# open the key file
with open("thekey.key", "rb") as key:
	secretkey = key.read()

# loop through files and decrypt
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)		

#  print confirmation
print("Files decrypted")
