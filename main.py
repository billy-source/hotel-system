import tkinter as tk
from auth import *


def show_main_menu():
    win = tk.Tk()
    win.title("Hotel Management System")
    win.geometry("400x300")

    tk.Label(win, text="Welcome to Hotel Management System", font=("Arial", 14)).pack(pady=20)

    tk.Button(win, text="Login", command=lambda: [win.destroy(), login()], width=20).pack(pady=10)
    tk.Button(win, text="Sign Up", command=lambda: [win.destroy(), signup()], width=20).pack(pady=10)

    win.mainloop()


if __name__ == "__main__":
    show_main_menu()
