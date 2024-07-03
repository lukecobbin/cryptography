# cryptography
Encrypt and Decrypt files.
This repository contains two python scripts. One is for encrypting all the files in a driectory (encrypt.py) 
and the other is for decrypting those files (decrypt.py)

They are fairly basic, mostly to demonstrate simple encrytion and decryption but they could be modified to do more.

Caesar Cipher
caesar.py is python code for decrypting caesar ciphers.
It takes arguments from the caommand line and shows all 26 version of the caesar cipher
Example: python3 caesar.py JxyiYiXemJeKiuYj

PowerShell Obfuscation
env_hid.py is a python script for obfuscating PowerShell.
It uses environment variables in windows and maps characters to positions.
e.g. The envoironment variable PUBLIC is: C:\Users\Public
so for the character "U" it would be $env:PUBLIC[3]
This idea is taken from a John Hammon youtube tutorial.
