# auth.py
import tkinter as tk
from tkinter import messagebox
import json
import hashlib
from admin_dashboard import admin_dashboard
from customer_dashboard import customer_dashboard

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def signup():
    win = tk.Tk()
    win.title("Sign Up")
    win.geometry("300x300")

    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    tk.Label(win, text="Role (admin/customer)").pack()
    role_entry = tk.Entry(win)
    role_entry.pack()

    def register():
        username = username_entry.get()
        password = password_entry.get()
        role = role_entry.get().lower()

        if role not in ["admin", "customer"]:
            messagebox.showerror("Error", "Role must be admin or customer")
            return

        users = load_users()

        for user in users:
            if user["username"] == username:
                messagebox.showerror("Error", "Username already exists")
                return

        users.append({
            "username": username,
            "password": hash_password(password),
            "role": role
        })
        save_users(users)
        messagebox.showinfo("Success", "Account created successfully")
        win.destroy()

    tk.Button(win, text="Register", command=register).pack(pady=10)
    tk.Button(win, text="Back", command=lambda: [win.destroy(), import_main()]).pack()

    win.mainloop()

def login():
    win = tk.Tk()
    win.title("Login")
    win.geometry("300x250")

    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def authenticate():
        username = username_entry.get()
        password = password_entry.get()
        hashed = hash_password(password)
        users = load_users()

        for user in users:
            if user["username"] == username and user["password"] == hashed:
                win.destroy()
                if user["role"] == "admin":
                    admin_dashboard(username)
                else:
                    customer_dashboard(username)
                return

        messagebox.showerror("Error", "Invalid credentials")

    tk.Button(win, text="Login", command=authenticate).pack(pady=10)
    tk.Button(win, text="Back", command=lambda: [win.destroy(), import_main()]).pack()

    win.mainloop()

def import_main():
    import main
    main.show_main_menu()
