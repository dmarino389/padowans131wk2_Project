class ParkingGarage:
  def __init__(self):
    self.available_tickets = list(range(1, 5))
    # self.available_parking_spaces = set(range(1, 5))
    self.current_tickets = {}
    

  
  def user_choice(self):
    while True:
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
  
  
  
  def take_ticket(self):
    if self.available_tickets:
        ticket = self.available_tickets.pop()
        # parking_spaces = self.available_parking_spaces.pop()
        self.current_tickets[ticket] = {'paid': False, 'available': False}
        print(f'Your ticket is {ticket}. Please proceed to pay your ticket.')
        
    else:
       print('Sorry, but there is not tickets')
  
  def pay_for_parking(self):
    if self.current_tickets:
      print("Your total is 5") 
      spot = int(input('(What was your ticket number?) '))
      payment = int(input('(Enter payment amount) '))
      if payment == 5:
        self.current_tickets[spot]['paid'] = True
        
        print('Payment recieved. You have 15 minutes to leave.')
        return True #if code wont work, try removing this return True
    self.spot.ammend(self.available_tickets) #-------------------------------------------------------------------->
      else:
        print('Wrong amount')
    
      return False #if code wont work, try removing this return False

  def leave_garage(self):
    spot = int(input('What was your ticket number'))
    if self.current_tickets[spot]['paid'] == True:
      self.available_tickets.append(spot)
      print('Thank you, have a nice day.')
    else:
      print('Your total is $5')
      not_paid = input('Enter payment amount')
      if self.current_tickets['paid'] == True:
        print('Thank you, have a nice day')
      self.available_parking_spaces.append(+1)
      self.available_tickets.append(+1)
  
  
 
ParkingGarage = ParkingGarage()
ParkingGarage.user_choice()

#make it go back to what it was at the beginning