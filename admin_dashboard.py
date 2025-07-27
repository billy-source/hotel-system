import tkinter as tk
from tkinter import messagebox
import json, os

ROOMS_FILE = "rooms.json"
BOOKINGS_FILE = "bookings.json"

for file in [ROOMS_FILE, BOOKINGS_FILE]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)

def load_rooms():
    with open(ROOMS_FILE) as f:
        return json.load(f)

def save_rooms(rooms):
    with open(ROOMS_FILE, "w") as f:
        json.dump(rooms, f, indent=4)

def load_bookings():
    with open(BOOKINGS_FILE) as f:
        return json.load(f)

def admin_dashboard(user):
    win = tk.Tk()
    win.title("Admin Dashboard")
    win.geometry("600x500")

    tk.Label(win, text=f"Admin: {user['username']}", font=("Arial", 14)).pack(pady=10)

    # Add room
    tk.Label(win, text="Room Number").pack()
    room_number_entry = tk.Entry(win)
    room_number_entry.pack()

    tk.Label(win, text="Room Type").pack()
    room_type_entry = tk.Entry(win)
    room_type_entry.pack()

    tk.Label(win, text="Price").pack()
    room_price_entry = tk.Entry(win)
    room_price_entry.pack()

    def add_room():
        num = room_number_entry.get().strip()
        typ = room_type_entry.get().strip()
        price = room_price_entry.get().strip()

        if not num or not typ or not price:
            return messagebox.showerror("Error", "All fields required")

        rooms = load_rooms()
        rooms.append({"number": num, "type": typ, "price": price})
        save_rooms(rooms)
        messagebox.showinfo("Success", "Room added")

    tk.Button(win, text="Add Room", command=add_room, bg="green", fg="white").pack(pady=5)

    # View rooms
    def view_rooms():
        room_list.delete(0, tk.END)
        for r in load_rooms():
            room_list.insert(tk.END, f"Room {r['number']} - {r['type']} - KES {r['price']}")

    room_list = tk.Listbox(win, width=60)
    room_list.pack(pady=10)

    tk.Button(win, text="View Rooms", command=view_rooms).pack()

    def delete_room():
        index = room_list.curselection()
        if not index:
            return messagebox.showerror("Error", "Select a room to delete")
        rooms = load_rooms()
        del rooms[index[0]]
        save_rooms(rooms)
        view_rooms()
        messagebox.showinfo("Deleted", "Room deleted")

    tk.Button(win, text="Delete Room", command=delete_room, bg="red", fg="white").pack(pady=5)

    def view_bookings():
        bookings = load_bookings()
        book_win = tk.Toplevel(win)
        book_win.title("Bookings")
        for b in bookings:
            tk.Label(book_win, text=f"{b['username']} booked Room {b['room']} | MPESA: {b['mpesa']}").pack()

    tk.Button(win, text="View Bookings", command=view_bookings, bg="blue", fg="white").pack(pady=10)

    win.mainloop()
