# room_customer.py

# Room class to represent hotel rooms
class Room:
    def __init__(self, room_number, room_type, price_per_night, status="Available"):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.status = status  # Can be: Available, Booked, Maintenance

    def book_room(self):
        if self.status == "Available":
            self.status = "Booked"
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is not available for booking.")

    def make_available(self):
        self.status = "Available"
        print(f"Room {self.room_number} is now available.")

    def mark_maintenance(self):
        self.status = "Maintenance"
        print(f"Room {self.room_number} is under maintenance.")

    def display_info(self):
        print(f"Room No: {self.room_number} | Type: {self.room_type} | Price: ${self.price_per_night}/night | Status: {self.status}")


# Customer class to represent hotel guests
class Customer:
    def __init__(self, name, id_number, contact_number):
        self.name = name
        self.id_number = id_number
        self.contact_number = contact_number
        self.room = None  # This will store the Room object assigned to the customer

    def assign_room(self, room: Room):
        if room.status == "Available":
            room.book_room()
            self.room = room
            print(f"{self.name} has been assigned to Room {room.room_number}.")
        else:
            print(f"Room {room.room_number} is not available for {self.name}.")

    def check_out(self):
        if self.room:
            print(f"{self.name} is checking out from Room {self.room.room_number}.")
            self.room.make_available()
            self.room = None
        else:
            print(f"{self.name} has no room assigned.")

    def display_info(self):
        room_info = f"Assigned Room: {self.room.room_number}" if self.room else "No room assigned"
        print(f"Customer: {self.name} | ID: {self.id_number} | Contact: {self.contact_number} | {room_info}")



def main():

    room1 = Room(101, "Single", 50)
    room2 = Room(102, "Double", 80)

    # Create a customer
    customer1 = Customer("Billy kemboi", "ID12345", "0712345678")

    
    print("Initial Room Status:")
    room1.display_info()
    room2.display_info()

    print("\nCustomer Info Before Booking:")
    customer1.display_info()

    # Assign room
    print("\nBooking Room...")
    customer1.assign_room(room1)

    # Display info after booking
    print("\nCustomer Info After Booking:")
    customer1.display_info()

    print("\nRoom Status After Booking:")
    room1.display_info()

    
    print("\nCustomer Checking Out...")
    customer1.check_out()

    
    print("\nFinal Room Status:")
    room1.display_info()

    print("\nCustomer Info After Check-Out:")
    customer1.display_info()



if __name__ == "__main__":
    main()
