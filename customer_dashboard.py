import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

from main import show_main_menu

ROOMS_FILE = "rooms.json"
BOOKINGS_FILE = "bookings.json"


def load_rooms():
    if not os.path.exists(ROOMS_FILE):
        with open(ROOMS_FILE, "w") as f:
            json.dump([], f)
    with open(ROOMS_FILE, "r") as f:
        return json.load(f)


def save_bookings(bookings):
    with open(BOOKINGS_FILE, "w") as f:
        json.dump(bookings, f, indent=4)


def load_bookings():
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "w") as f:
            json.dump([], f)
    with open(BOOKINGS_FILE, "r") as f:
        return json.load(f)


def customer_dashboard(username):
    win = tk.Tk()
    win.title(f"Customer Dashboard - {username}")
    win.geometry("600x400")

    tk.Label(win, text=f"Welcome, {username}", font=("Arial", 14)).pack(pady=10)

    room_listbox = tk.Listbox(win, width=80)
    room_listbox.pack(pady=10)

    def refresh_rooms():
        room_listbox.delete(0, tk.END)
        rooms = load_rooms()
        if rooms:
            for room in rooms:
                room_listbox.insert(tk.END, f"Room No: {room['room_no']} | Type: {room['room_type']} | Price: {room['price']}")
        else:
            room_listbox.insert(tk.END, "No rooms available.")

    def book_selected_room():
        selected_index = room_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a room to book.")
            return

        rooms = load_rooms()
        selected_room = rooms[selected_index[0]]

        mpesa_number = simpledialog.askstring("MPESA Payment", "Enter your MPESA number:")
        if not mpesa_number:
            messagebox.showerror("Error", "MPESA number is required.")
            return

        bookings = load_bookings()
        bookings.append({
            "username": username,
            "room_no": selected_room['room_no'],
            "room_type": selected_room['room_type'],
            "price": selected_room['price'],
            "mpesa_number": mpesa_number
        })

        save_bookings(bookings)
        messagebox.showinfo("Success", f"Room {selected_room['room_no']} booked successfully!")

    def logout():
        win.destroy()
        show_main_menu()

    tk.Button(win, text="Refresh Rooms", command=refresh_rooms).pack(pady=5)
    tk.Button(win, text="Book Selected Room", command=book_selected_room).pack(pady=5)
    tk.Button(win, text="Logout", command=logout).pack(pady=5)

    refresh_rooms()
    win.mainloop()
