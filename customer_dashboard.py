import tkinter as tk
from tkinter import messagebox
import json, os

ROOMS_FILE = "rooms.json"
BOOKINGS_FILE = "bookings.json"

def load_rooms():
    with open(ROOMS_FILE) as f:
        return json.load(f)

def save_booking(booking):
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "w") as f:
            json.dump([], f)
    with open(BOOKINGS_FILE) as f:
        bookings = json.load(f)
    bookings.append(booking)
    with open(BOOKINGS_FILE, "w") as f:
        json.dump(bookings, f, indent=4)

def customer_dashboard(user):
    win = tk.Tk()
    win.title("Customer Dashboard")
    win.geometry("500x500")

    tk.Label(win, text=f"Welcome, {user['username']}", font=("Arial", 14)).pack(pady=10)

    listbox = tk.Listbox(win, width=60)
    listbox.pack(pady=10)

    def load_available_rooms():
        listbox.delete(0, tk.END)
        for r in load_rooms():
            listbox.insert(tk.END, f"Room {r['number']} - {r['type']} - KES {r['price']}")

    tk.Button(win, text="View Available Rooms", command=load_available_rooms).pack()

    def book_selected_room():
        index = listbox.curselection()
        if not index:
            return messagebox.showerror("Error", "Select a room")
        room = load_rooms()[index[0]]

        mpesa = tk.simpledialog.askstring("MPESA", "Enter MPESA number:")
        if not mpesa:
            return messagebox.showerror("Error", "MPESA number required")

        save_booking({
            "username": user["username"],
            "room": room["number"],
            "mpesa": mpesa
        })
        messagebox.showinfo("Booked", "Room booked successfully!")

    tk.Button(win, text="Book Room", command=book_selected_room, bg="orange").pack(pady=10)

    win.mainloop()
