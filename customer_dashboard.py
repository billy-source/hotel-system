import tkinter as tk
import json
import os

ROOMS_FILE = "rooms.json"

def load_rooms():
    if not os.path.exists(ROOMS_FILE):
        return []
    with open(ROOMS_FILE, "r") as f:
        return json.load(f)

def customer_dashboard(customer_user):
    win = tk.Tk()
    win.title("Customer Dashboard")
    win.geometry("500x500")

    tk.Label(win, text=f"Welcome, {customer_user['username']}", font=("Arial", 14)).pack(pady=10)
    tk.Label(win, text="Available Rooms", font=("Arial", 12)).pack(pady=5)

    listbox = tk.Listbox(win, width=60, height=20)
    listbox.pack(pady=10)

    def show_rooms():
        rooms = load_rooms()
        listbox.delete(0, tk.END)
        if not rooms:
            listbox.insert(tk.END, "No rooms available.")
        else:
            for i, r in enumerate(rooms):
                listbox.insert(tk.END, f"{i + 1}. {r['type']} - KES {r['price']}")

    show_rooms()

    win.mainloop()
