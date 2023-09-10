class ParkingGarage:
    def __init__(self):
        self.available_tickets = list(range(1, 5))
        self.available_parking_spaces = list(range(1, 5))
        self.current_tickets = {}

    def user_choice(self):
        while True:
            choice = int(input('****Welcome to parking garage*****\n'
                               '****Parking is $5 all day****\n'
                               '1 - Take your ticket\n'
                               '2 - Pay your ticket\n'
                               '3 - Quit\n'))

            if choice == 1:
                self.take_ticket()
            elif choice == 2:
                self.pay_for_parking()
            elif choice == 3:
                print('Have a nice day.')
                break
            else:
                print('Invalid choice. Please enter [1] to take a ticket, [2] to pay your ticket, or [3] to quit.')

    def take_ticket(self):
        if self.available_tickets:
            ticket = self.available_tickets.pop(0)
            parking_space = self.available_parking_spaces.pop(0)
            print(f'Please take ticket {ticket}. You can park in space {parking_space}.')
            self.current_tickets[ticket] = parking_space
        else:
            print('Sorry, but there are no tickets available.')

    def pay_for_parking(self):
        if self.current_tickets:
            ticket = int(input('Enter your ticket number: '))
            if ticket in self.current_tickets:
                parking_space = self.current_tickets.pop(ticket)
                payment = input('Enter payment amount: ')
                if payment == '5':
                    print('Payment received. You have 15 minutes to leave.')
                else:
                    print('Wrong amount. Payment not received.')
                    self.current_tickets[ticket] = parking_space
            else:
                print('Invalid ticket number.')
        else:
            print('No tickets have been taken yet.')

    def leave_garage(self):
        if self.current_tickets:
            print('You need to pay before leaving.')
        else:
            print('Thank you, have a nice day.')


parking_garage = ParkingGarage()
parking_garage.user_choice()
