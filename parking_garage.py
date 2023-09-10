
# Initialize the Parking Garage Class
# Create a class called ParkingGarage. 

class ParkingGarage: 
    def __init__(self, parkingSpaces, tickets, currentTicket, cost):
     self.parkingSpaces = parkingSpaces
     self.tickets = tickets
     self.currentTicket = currentTicket
     self.cost = cost
    


while True:
    choice = input('Do you want to take a ticket? (1 = Y / 2 = N) ')
    if choice == "1":
        print('Take your ticket')
        break  # Exit the loop when the user chooses 1
    elif choice == "2":
        print('Have a nice day')
        quit()
    else:
        print('Invalid choice. Please enter 1 to take a ticket or 2 to exit.')


                 
       
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
# Implement the payForParking Method
# Create a method called payForParking that displays an input prompt to the user to enter the payment amount and stores it in a variable.
# If the payment variable is not empty (meaning the ticket has been paid):
# Display a message to the user that their ticket has been paid and they have 15 minutes to leave.
# Update the "paid" key in the currentTicket dictionary to True.
# Implement the leaveGarage Method
# Create a method called leaveGarage.
# If the ticket has been paid (the "paid" key in the currentTicket dictionary is True):
# Display a message: "Thank you, have a nice day."
# If the ticket has not been paid:
# Display an input prompt for payment.
# Once paid, display a message: "Thank you, have a nice day!"
# Update the parkingSpaces list to increase by 1 (add a parking space back).
# Update the tickets list to increase by 1 (add the ticket back).
# Testing the Parking Garage
# Create an instance of the ParkingGarage class.
# Use the methods takeTicket, payForParking, and leaveGarage to simulate the parking garage operations.
# Test various scenarios to ensure the class behaves as expected.
# Git and GitHub Collaboration
# Set up a GitHub repository for the project.
# Collaborate with team members using Git for version control.
# Commit and push changes to the repository regularly.
# Create a README file to document each team member's contributions.
# Each team member should work on different parts of the class methods, and you can switch roles (driver/navigator) during development to ensure everyone contributes to the project. Make sure to follow best practices for collaborating on a shared codebase using Git and GitHub.



 