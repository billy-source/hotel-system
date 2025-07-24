import tkinter as tk
from tkinter import messagebox, simpledialog


class Billing:
    def __init__(self, booking):
        self.booking = booking
        self.amount = booking.total_cost

    def process_payment(self):
        # Show total bill
        messagebox.showinfo("Billing", f"Total amount: KES {self.amount}\nProceed to pay via M-Pesa")

        # Ask for PIN (masked)
        pin = simpledialog.askstring("M-Pesa Payment", "Enter M-Pesa PIN:", show="*")

        if not pin:
            messagebox.showerror("Payment Failed", "Payment cancelled. M-Pesa PIN required.")
            return False
        else:
            # Simulate success
            messagebox.showinfo("Payment Successful", f"Payment of KES {self.amount} received via M-Pesa.")
            return True
