import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip   # pip install pyperclip


def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    exclude_similar = exclude_var.get()

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|`~" if use_symbols else ""

    characters = lowercase + uppercase + digits + symbols

    if exclude_similar:
        for ch in "O0Il1":
            characters = characters.replace(ch, "")

    if not characters:
        messagebox.showerror("Error", "No characters available for password generation")
        return

    password = []

    if use_upper:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    final_password = "".join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)

    with open("passwords.txt", "a") as f:
        f.write(final_password + "\n")


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar(value=True)

# Widgets
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w")
length_slider = tk.Scale(frame, from_=6, to=32, orient="horizontal", variable=length_var)
length_slider.grid(row=0, column=1)

tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Exclude Similar (O/0, l/1)", variable=exclude_var).grid(row=4, column=0, columnspan=2, sticky="w")

password_entry = tk.Entry(root, width=30, font=("Courier", 12), justify="center")
password_entry.pack(pady=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)

root.mainloop()
