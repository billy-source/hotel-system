import tkinter as tk
from tkinter import messagebox
import json, os, hashlib
from admin_dashboard import admin_dashboard
from customer_dashboard import customer_dashboard

USERS_FILE = "users.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def user_exists(username):
    return any(user["username"] == username for user in load_users())

def show_auth_screen():
    root = tk.Tk()
    root.title("Auth")
    root.geometry("400x400")

    tk.Label(root, text="Login or Sign Up", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    role_var = tk.StringVar(value="customer")
    tk.Label(root, text="Role").pack()
    tk.Radiobutton(root, text="Admin", variable=role_var, value="admin").pack()
    tk.Radiobutton(root, text="Customer", variable=role_var, value="customer").pack()

    def signup():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()

        if not username or not password:
            return messagebox.showerror("Error", "All fields required")
        if user_exists(username):
            return messagebox.showerror("Error", "Username already exists")

        users = load_users()
        users.append({
            "username": username,
            "password": hash_password(password),
            "role": role
        })
        save_users(users)
        messagebox.showinfo("Success", f"{role.capitalize()} account created")

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()

        for user in load_users():
            if user["username"] == username and user["password"] == hash_password(password) and user["role"] == role:
                root.destroy()
                if role == "admin":
                    admin_dashboard(user)
                else:
                    customer_dashboard(user)
                return
        messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, bg="blue", fg="white").pack(pady=10)
    tk.Button(root, text="Sign Up", command=signup, bg="green", fg="white").pack()

    root.mainloop()
