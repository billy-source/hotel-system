import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import db_config
rooms = []
bookings = []


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = "Available"

    def __str__(self):
        return f"{self.room_number} | {self.room_type} | ${self.price} | {self.status}"


class Booking:
    def __init__(self, customer_name, room_number, check_in, check_out, total_cost):
        self.customer_name = customer_name
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out
        self.total_cost = total_cost

    def __str__(self):
        return f"{self.customer_name} | Room {self.room_number} | {self.check_in} to {self.check_out} | ${self.total_cost}"



def add_room():
    try:
        num = int(entry_room_number.get())
        rtype = entry_room_type.get()
        price = float(entry_price.get())

        new_room = Room(num, rtype, price)
        rooms.append(new_room)

        messagebox.showinfo("Success", f"Room {num} added.")
        entry_room_number.delete(0, tk.END)
        entry_room_type.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Invalid input.")


def view_rooms():
    window = tk.Toplevel(root)
    window.title("All Rooms")
    for room in rooms:
        tk.Label(window, text=str(room)).pack(anchor="w")


def view_bookings():
    window = tk.Toplevel(root)
    window.title("All Bookings")
    if bookings:
        for b in bookings:
            tk.Label(window, text=str(b)).pack(anchor="w")
    else:
        tk.Label(window, text="No bookings yet.").pack()



def show_admin_dashboard():
    global root, entry_room_number, entry_room_type, entry_price

    root = tk.Tk()
    root.title("Admin Dashboard")
    root.geometry("400x400")

    tk.Label(root, text="Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Add Room").pack()
    entry_room_number = tk.Entry(root)
    entry_room_number.insert(0, "Room Number")
    entry_room_number.pack()

    entry_room_type = tk.Entry(root)
    entry_room_type.insert(0, "Room Type (Single/Double)")
    entry_room_type.pack()

    entry_price = tk.Entry(root)
    entry_price.insert(0, "Price")
    entry_price.pack()

    tk.Button(root, text="Add Room", command=add_room, bg="blue", fg="white").pack(pady=5)
    tk.Button(root, text="View All Rooms", command=view_rooms).pack()
    tk.Button(root, text="View Bookings", command=view_bookings).pack()
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()



def login():
    user = entry_username.get()
    password = entry_password.get()

    if user == "admin" and password == "admin123":
        login_window.destroy()
        show_admin_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Admin Login", font=("Arial", 14)).pack(pady=10)

tk.Label(login_window, text="Username").pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

tk.Label(login_window, text="Password").pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

tk.Button(login_window, text="Login", command=login, bg="green", fg="white").pack(pady=10)

login_window.mainloop()
