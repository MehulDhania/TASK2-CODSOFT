import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():

    length = int(lenght.get())
    if length < 1:
        messagebox.showerror("Password length should be greater then 1.")
        return
    letter=string.ascii_letters
    digit=string.digits
    symbol=string.punctuation
    characters = letter + digit + symbol
    password = ''.join(random.choice(characters) for _ in range(length))

    entry.delete(0, tk.END) 
    entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

lb = tk.Label(root, text="Enter Password Length:")
lb.pack(pady=10)

lenght = tk.Entry(root)
lenght.pack(pady=5)

button = tk.Button(root, text="Generate Password", command=generate_password)
button.pack(pady=10)

lb2 = tk.Label(root, text="Generated Password:")
lb2.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
root.mainloop()
