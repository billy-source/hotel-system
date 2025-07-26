from auth import login_screen, init_users
from admin_dashboard import admin_dashboard
from customer_dashboard import customer_dashboard

def launch_dashboard(user):
    if user["role"] == "admin":
        admin_dashboard(user)
    elif user["role"] == "customer":
        customer_dashboard(user)

if __name__ == "__main__":
    init_users()
    login_screen(launch_dashboard)

