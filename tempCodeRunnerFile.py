class ParkingGarage:
  def __init__(self, total_spaces):
    self.available_tickets = set(range(1, total_spaces +1))
    self.paid_tickets = set()

  def take_ticket(self):
    if not self.available_tickets:
      print('Sorry, the parking garage is full.')
      return None
    ticket = self.available_tickets.pop()
    print(f'Please take ticket {ticket}.')
    return ticket
  
  def pay_for_parking(self, ticket):
    if ticket in self.available_tickets:
      payment = input('Enter payment amount')
      if payment:
        self.paid_tickets.add(ticket)
        print('Payment recieved. You have 15 minutes to leave.')
        return True