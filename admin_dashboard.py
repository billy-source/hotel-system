import tkinter as tk
from tkinter import messagebox
import json
import os

ROOMS_FILE = "rooms.json"

def load_rooms():
    if not os.path.exists(ROOMS_FILE):
        with open(ROOMS_FILE, "w") as f:
            json.dump([], f)
    with open(ROOMS_FILE, "r") as f:
        return json.load(f)

def save_rooms(rooms):
    with open(ROOMS_FILE, "w") as f:
        json.dump(rooms, f, indent=4)

def admin_dashboard(admin_user):
    win = tk.Tk()
    win.title("Admin Dashboard")
    win.geometry("500x550")

    tk.Label(win, text=f"Welcome Admin: {admin_user['username']}", font=("Arial", 14)).pack(pady=10)

    tk.Label(win, text="Room Type").pack()
    room_type_entry = tk.Entry(win)
    room_type_entry.pack()

    tk.Label(win, text="Room Price (KES)").pack()
    room_price_entry = tk.Entry(win)
    room_price_entry.pack()

    def add_room():
        room_type = room_type_entry.get().strip()
        price = room_price_entry.get().strip()

        if not room_type or not price:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return

        rooms = load_rooms()
        rooms.append({"type": room_type, "price": price})
        save_rooms(rooms)
        messagebox.showinfo("Success", "Room added successfully.")
        room_type_entry.delete(0, tk.END)
        room_price_entry.delete(0, tk.END)
        refresh_rooms()

    def delete_selected_room():
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a room to delete.")
            return
        index = selection[0]
        rooms = load_rooms()
        del rooms[index]
        save_rooms(rooms)
        messagebox.showinfo("Deleted", "Room deleted successfully.")
        refresh_rooms()

    def refresh_rooms():
        listbox.delete(0, tk.END)
        rooms = load_rooms()
        if not rooms:
            listbox.insert(tk.END, "No rooms available.")
        else:
            for i, room in enumerate(rooms):
                listbox.insert(tk.END, f"{i + 1}. {room['type']} - KES {room['price']}")

    tk.Button(win, text="Add Room", command=add_room, bg="green", fg="white").pack(pady=5)
    tk.Button(win, text="Delete Selected Room", command=delete_selected_room, bg="red", fg="white").pack(pady=5)

    listbox = tk.Listbox(win, width=60, height=15)
    listbox.pack(pady=10)

    refresh_rooms()

    win.mainloop()
