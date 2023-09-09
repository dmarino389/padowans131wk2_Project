
# Initialize the Parking Garage Class
# Create a class called ParkingGarage. 

class ParkingGarage: 
    def __init__(self):
        self.ParkingTickets = list(range(1,10+1))
        self.ParkingSpaces = list(range(1,10+1))
        self.CurrentTicket = {}

# takeTicket/ Check - in 
    def takeTicket(self):
        if len(self.ParkingTickets) >= 1 and len(self.ParkingTickets) <= 10:
            self.ParkingTickets.pop(0)
            self.ParkingSpaces.pop(0)

        else:
            print("There is no parking spaces")

# Implement the payForParking Method
#Garage check out
#Create a function to check if the amount owe was paid. After that,
#we need to append 1 spot back'


# Display a message to the user that their ticket has been paid and they have 15 minutes to leave.
# Update the "paid" key in the currentTicket dictionary to True.


# Testing the Parking Garage
# Create an instance of the ParkingGarage class.
############################TEST AND PRINT #########################   
def user_choice():
    while True:
        choice = int(input('****Welcome to parking garage*****\n'
                           '****Parking is $5 all day****\n'
                                '1 - Take your ticket\n'
                                '2 - Pay your ticket\n'
                                '3 - Quit\n'))
        if choice == 1:
            print('Take your ticket')
            return choice
        elif choice == 2:
            return choice
        elif choice == 3:
            print('Have a nice day')
            break
        else:
            print('Invalid choice. Please enter [1] to take a ticket, [2] to pay your ticket or [3] to quit ')


ParkingGarage = ParkingGarage()
                 
    