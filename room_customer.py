# Room class
class Room:
    def __init__(self, room_number, room_type, price, status='Available'):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = status

    def display_info(self):
        print(f"Room {self.room_number} - {self.room_type} - ${self.price} - {self.status}")


# Customer class
class Customer:
    def __init__(self, name, id_number, contact):
        self.name = name
        self.id_number = id_number
        self.contact = contact

    def display_info(self):
        print(f"Customer: {self.name}, ID: {self.id_number}, Contact: {self.contact}")



room1 = Room(101, 'Single', 50)
customer1 = Customer('billy kemboi', 'ID12345', '0712345678')

room1.display_info()
customer1.display_info()
