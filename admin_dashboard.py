# admin_dashboard.py
import tkinter as tk
from tkinter import messagebox
from utils import load_rooms, save_rooms, load_bookings
import main

rooms_file = "rooms.json"


def admin_dashboard(username):
    def add_room():
        room = room_entry.get()
        if not room:
            messagebox.showerror("Error", "Room name is required")
            return
        rooms = load_rooms()
        rooms.append({"name": room})
        save_rooms(rooms)
        room_entry.delete(0, tk.END)
        update_rooms_listbox()

    def delete_room():
        selected = rooms_listbox.curselection()
        if selected:
            index = selected[0]
            rooms = load_rooms()
            del rooms[index]
            save_rooms(rooms)
            update_rooms_listbox()
        else:
            messagebox.showwarning("Warning", "No room selected")

    def update_rooms_listbox():
        rooms_listbox.delete(0, tk.END)
        rooms = load_rooms()
        for room in rooms:
            rooms_listbox.insert(tk.END, room["name"])

    def view_bookings():
        bookings = load_bookings()
        if not bookings:
            messagebox.showinfo("Info", "No bookings found")
            return
        bookings_str = "\n".join([f"{b['customer']} booked {b['room']} for {b['days']} day(s), MPESA: {b['mpesa']}" for b in bookings])
        messagebox.showinfo("Bookings", bookings_str)

    win = tk.Tk()
    win.title("Admin Dashboard")
    win.geometry("400x400")

    tk.Label(win, text=f"Welcome Admin: {username}", font=("Arial", 12)).pack(pady=10)

    room_entry = tk.Entry(win)
    room_entry.pack(pady=5)
    tk.Button(win, text="Add Room", command=add_room).pack(pady=5)
    tk.Button(win, text="Delete Selected Room", command=delete_room).pack(pady=5)
    tk.Button(win, text="View All Bookings", command=view_bookings).pack(pady=5)

    rooms_listbox = tk.Listbox(win, width=50)
    rooms_listbox.pack(pady=10)

    tk.Button(win, text="Logout", command=lambda: [win.destroy(), main.show_main_menu()]).pack(pady=10)

    update_rooms_listbox()
    win.mainloop()
