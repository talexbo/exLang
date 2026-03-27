class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    return self.balance
  def withdraw(self, amount):
    self.balance -= amount
    return self.balance
  def display_balance(self):
    print(self.balance)

larry = BankAccount("Larry", "Smith" ,1, "debit", 1234, 0.)
larry.deposit(96)
larry.withdraw(25)
larry.display_balance()
