import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})   # load the id column as string values

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()


    def book(self):
        """ Change the hotel availability from 'yes' to 'no' value. """
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)
        # updates file and prevents another column index being created
        print("I am the book function")

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        # find the row where the id is user input, then return the value from that rows 'available' column
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}      
        """
        return content


print(df)

while True:
    try:
        hotel_id = input('Enter the id of the hotel: ')
        hotel = Hotel(hotel_id)
        if hotel.available():
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            # we are sending a str instance and a hotel instance to the ReservationTicket class
            print(reservation_ticket.generate())
        else:
            print("Hotel is not available.")
            break
    except ValueError:
        print('Invalid id. Try again.')
