from dashboard_admin import *
from  dashboard_customer import *


import tkinter as tk
from tkinter import messagebox
from db_config import get_db

db = get_db()
users_col = db["users"]


def signup_window():
    def register_user():
        username = entry_username.get()
        password = entry_password.get()
        role = role_var.get()

        if users_col.find_one({"username": username}):
            messagebox.showerror("Error", "Username already exists.")
            return

        users_col.insert_one({
            "username": username,
            "password": password,
            "role": role
        })

        messagebox.showinfo("Success", f"{role.capitalize()} registered successfully.")
        window.destroy()

    window = tk.Tk()
    window.title("Sign Up")
    window.geometry("300x300")

    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Label(window, text="Role").pack()
    role_var = tk.StringVar(value="customer")
    tk.Radiobutton(window, text="Customer", variable=role_var, value="customer").pack()
    tk.Radiobutton(window, text="Admin", variable=role_var, value="admin").pack()

    tk.Button(window, text="Sign Up", command=register_user, bg="green", fg="white").pack(pady=10)
    window.mainloop()


def login_window():
    def login_user():
        username = entry_username.get()
        password = entry_password.get()

        user = users_col.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo("Success", f"Welcome {user['role'].capitalize()}!")
            window.destroy()

            if user["role"] == "admin":
                from dashboard_admin import open_admin_dashboard
                open_admin_dashboard()
            else:
                from dashboard_customer import open_customer_dashboard
                open_customer_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    window = tk.Tk()
    window.title("Login")
    window.geometry("300x250")

    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Button(window, text="Login", command=login_user, bg="blue", fg="white").pack(pady=10)
    tk.Button(window, text="Create Account", command=lambda:[window.destroy(), signup_window()]).pack()

    window.mainloop()
