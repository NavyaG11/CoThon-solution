import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = 12  # You can adjust the password length here
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)

# Set up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Password variable
password_var = tk.StringVar()

# Create GUI elements
title_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

password_entry = tk.Entry(root, textvariable=password_var, font=("Helvetica", 12), width=30, justify='center')
password_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"), bg="blue", fg="white")
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: root.clipboard_append(password_var.get()), font=("Helvetica", 12), bg="green", fg="white")
copy_button.pack(pady=10)

# Run the GUI
root.mainloop()
