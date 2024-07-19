import pandas as pd
from functions import get_card_details

df = pd.read_csv('hotels.csv', dtype={'id': str})  # load the id column as string values
df_cards = (pd.read_csv('cards.csv', dtype=str)  # load all columns as string values
            .to_dict(orient="records"))  # each row is loaded as a dictionary
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """ Change the hotel availability from 'yes' to 'no' value. """
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)
        # updates file and prevents another column index being created

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        # find the row where the id is user input, then return the value from that rows 'available' column
        if availability == "yes":
            return True
        else:
            return False


class HotelSpa(Hotel):
    def book_spa_package(self):
        pass


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


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}      
        """
        return content



class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, name, cvc):
        card_details = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": name}
        if card_details in df_cards:
            print("Card is in the list")
            return True
        else:
            print("Card is not in the list")
            return False


# Inherits everything from the CreditCard class including the init and validate methods
# Checks if the users given password corresponds to the credit card number they provided
class SecureCreditCard(CreditCard):
    def authenticate(self, user_password):
        p = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if p == user_password:
            return True
        else:
            return False


print(df)

while True:
    try:
        hotel_id = input('Enter the id of the hotel: ')
        hotel = Hotel(hotel_id)

        if hotel.available():  # receives True or False

            # VALIDATE CREDIT CARD
            cc = get_card_details()  # gets from functions.py
            credit_card = SecureCreditCard(cc['card_no'])
            if credit_card.validate(cc['expiration'], cc['name'], cc['cvc']):
                password = input("Please enter your credit card authenticator password: ")
                if credit_card.authenticate(user_password=password):

                    # BOOK HOTEL
                    hotel.book()
                    name = input("Enter your name: ")
                    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
                    # we are sending a str instance and a hotel instance to the ReservationTicket class
                    print(reservation_ticket.generate())

                    # SPA PACKAGE
                    user_spa = input('Would you like to book a spa package y/n: ?')
                    if user_spa == 'y':
                        spa_reservation_ticket = SpaReservationTicket(customer_name=name, hotel_object=hotel)
                        print(spa_reservation_ticket.generate())
                        break
                    else:
                        print(f'Thank you {name}, enjoy your stay.')
                        break

                else:
                    print('Password does not match with credit card number.')

            else:
                print("There was a problem with the payment")

        else:
            print("Hotel is not available.")
            break

    except ValueError:
        print('Invalid id. Try again.')
