
# Initialize the Parking Garage Class
# Create a class called ParkingGarage. 

class ParkingGarage: 
<<<<<<< HEAD
    def __init__(self, parkingSpaces, tickets, currentTicket, cost):
     self.parkingSpaces = parkingSpaces
     self.tickets = tickets
     self.currentTicket = currentTicket
     self.cost = cost
    
=======
    def __init__(self):
        self.ParkingTickets = list(range(1,10+1))
        self.ParkingSpaces = list(range(1,10+1))
        self.CurrentTicket = {}
>>>>>>> 602191850068cef91f4b5b34c186b21e867727c6

# takeTicket/ Check - in 
    def takeTicket(self):
        if len(self.ParkingTickets) >= 1 and len(self.ParkingTickets) <= 10:
            self.ParkingTickets.pop(0)
            self.ParkingSpaces.pop(0)

        else:
            print("There is no parking spaces")

<<<<<<< HEAD

                 
       
while True: 
  print(f'You owe 5 dollars')
  choice_pay = input('(Enter your payment amount) ')
  if choice_pay ==5:
     print('Thank you for your purchase')
     break
  else:
     print('Insufficient ammount, please start over')
     




     
       
       

 # I need a function to remove a parking spot
    



# Initialize class attributes tickets, parkingSpaces, and currentTicket in the constructor.
# Initialize Class Attributes
# In the constructor, initialize the tickets attribute as an empty list to keep track of available tickets.
# Initialize the parkingSpaces attribute as a list to represent the available parking spaces.
# Initialize the currentTicket attribute as a dictionary to represent the current parking ticket.
# Implement the takeTicket Method
# Create a method called takeTicket that decreases the amount of tickets available by 1.
# Decrease the amount of parkingSpaces available by 1.
# Assign the ticket to the current user in the currentTicket attribute.
=======
>>>>>>> 602191850068cef91f4b5b34c186b21e867727c6
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
                 
    