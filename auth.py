import tkinter as tk
from tkinter import messagebox
from json_db import save_user, find_user, username_exists
import dashboard_admin
import dashboard_customer

def open_login_window():
    window = tk.Tk()
    window.title("Login")
    window.geometry("300x250")

    def login_user():
        username = entry_username.get()
        password = entry_password.get()
        user = find_user(username, password)

        if user:
            messagebox.showinfo("Success", f"Welcome {user['role']}!")
            window.destroy()
            if user["role"] == "admin":
                dashboard_admin.open_admin_dashboard()
            else:
                dashboard_customer.open_customer_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def signup_user():
        username = entry_username.get()
        password = entry_password.get()
        role = var_role.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password required.")
            return
        if username_exists(username):
            messagebox.showerror("Error", "Username already exists.")
            return

        user = {"username": username, "password": password, "role": role}
        save_user(user)
        messagebox.showinfo("Success", "Account created successfully!")

    tk.Label(window, text="Username").pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    var_role = tk.StringVar(value="customer")
    tk.Radiobutton(window, text="Customer", variable=var_role, value="customer").pack()
    tk.Radiobutton(window, text="Admin", variable=var_role, value="admin").pack()

    tk.Button(window, text="Login", command=login_user).pack(pady=5)
    tk.Button(window, text="Sign Up", command=signup_user).pack()

    window.mainloop()
