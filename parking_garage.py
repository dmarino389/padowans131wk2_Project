class ParkingGarage:
    def __init__(self):
        self.available_tickets = list(range(1, 5))
        self.current_tickets = {}
    
    def user_choice(self):
        while True:
            try:
                choice = int(input('****Welcome to parking garage*****\n'
                                   '****Parking is $5 all day****\n'
                                   '1 - Take your ticket\n'
                                   '2 - Pay your ticket\n'
                                   '3 - Leave The Garage\n'))
                
                if choice == 1:
                    self.take_ticket()
                elif choice == 2:
                    self.pay_for_parking()
                elif choice == 3:
                    print('Have a nice day.')
                    break
                else:
                    print('Invalid choice. Please enter [1] to take a ticket, [2] to pay your ticket, or [3] to quit.')
            except ValueError:
                print('Invalid input. Please enter a valid choice (1, 2, or 3).')

  
    def take_ticket(self):
        if self.available_tickets:
            ticket = self.available_tickets.pop()
            self.current_tickets[ticket] = {'paid': False}
            print(f'Your ticket is {ticket}. Please proceed to pay your ticket.')
        else:
            print('Sorry, but there are no available tickets.')
  
    def pay_for_parking(self):
        if self.current_tickets:
            spot = int(input('(What was your ticket number?) '))
            if spot in self.current_tickets and not self.current_tickets[spot]['paid']:
                payment = int(input('(Enter payment amount) '))
                if payment == 5:
                    self.current_tickets[spot]['paid'] = True
                    print('Payment received. You have 15 minutes to leave.')
                    # Return the ticket to the list of available tickets
                    self.available_tickets.append(spot)
                else:
                    print('Wrong amount. Payment failed.')
            else:
                print('Ticket not found or already paid.')
        else:
            print('No tickets issued yet.')
    
    def leave_garage(self):
        spot = int(input('What was your ticket number? '))
        if spot in self.current_tickets and self.current_tickets[spot]['paid']:
            del self.current_tickets[spot]
            print('Thank you, have a nice day.')
        else:
            print('Ticket not found or not paid.')
 
ParkingGarage = ParkingGarage()
ParkingGarage.user_choice()
