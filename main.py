import tkinter as tk
from auth import show_auth_screen

def main_menu():
    root = tk.Tk()
    root.title("Hotel Management System")
    root.geometry("400x300")

    tk.Label(root, text="Welcome to Hotel Management System", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Login / Sign Up", command=lambda: [root.destroy(), show_auth_screen()], width=20).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
