from room_customer import * 
from datetime import datetime

class Booking:
    def __init__(self, booking_id, customer, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        self.check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
        self.total_days = (self.check_out_date - self.check_in_date).days
        self.total_cost = self.total_days * room.price_per_night

    def confirm_booking(self):
        if self.room.status == "Available":
            self.room.book_room()
            self.customer.assign_room(self.room)
            print(f"\n✅ Booking Confirmed!")
            print(f"Booking ID: {self.booking_id}")
            print(f"{self.customer.name} booked Room {self.room.room_number} from {self.check_in_date.date()} to {self.check_out_date.date()}")
            print(f"Total Days: {self.total_days}, Total Cost: ${self.total_cost}")
        else:
            print(f"❌ Room {self.room.room_number} is not available.")
