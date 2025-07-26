# auth.py
import tkinter as tk
from tkinter import messagebox
from utils import load_json, save_json

USERS_FILE = "users.json"

def init_users():
    if not load_json(USERS_FILE):
        admin = {
            "username": "admin",
            "password": "admin123",
            "role": "admin"
        }
        save_json(USERS_FILE, [admin])

def save_user(user):
    users = load_json(USERS_FILE)
    users.append(user)
    save_json(USERS_FILE, users)

def find_user(username, password):
    users = load_json(USERS_FILE)
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None

def user_exists(username):
    users = load_json(USERS_FILE)
    return any(user["username"] == username for user in users)

def login_screen(on_success):
    window = tk.Tk()
    window.title("Hotel System - Login")
    window.geometry("300x250")

    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        user = find_user(username, password)
        if user:
            messagebox.showinfo("Success", f"Welcome {user['role'].capitalize()}")
            window.destroy()
            on_success(user)
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def handle_signup():
        username = entry_username.get()
        password = entry_password.get()
        role = role_var.get()

        if not username or not password:
            messagebox.showwarning("Incomplete", "Enter all fields")
            return
        if user_exists(username):
            messagebox.showwarning("Exists", "Username already exists")
            return

        user = {"username": username, "password": password, "role": role}
        save_user(user)
        messagebox.showinfo("Signup Successful", "You can now login")

    tk.Label(window, text="Username").pack(pady=5)
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack(pady=5)
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Label(window, text="Role").pack(pady=5)
    role_var = tk.StringVar(value="customer")
    tk.OptionMenu(window, role_var, "admin", "customer").pack()

    tk.Button(window, text="Login", command=handle_login).pack(pady=5)
    tk.Button(window, text="Signup", command=handle_signup).pack()

    window.mainloop()
