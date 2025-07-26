# utils.py
import json
import os
from tkinter import simpledialog, messagebox

def load_json(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def prompt_mpesa_number():
    number = simpledialog.askstring("Payment", "Enter your MPESA number:")
    if not number or not number.isdigit() or len(number) != 10:
        messagebox.showerror("Invalid", "Enter a valid 10-digit MPESA number")
        return None
    return number

def notify_admin(message):
    print("[ADMIN ALERT]:", message)
    messagebox.showinfo("Admin Notification", message)
