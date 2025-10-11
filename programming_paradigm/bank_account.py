class BankAccount:
    def __init__ (self, starting_balance=0):
        self.account_balance = starting_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")
    
    def  withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"withdrew: ${amount:.2f}")
            return True
        else:
            print(f"insufficient funds!")
            return False
        
    def display_balance(self,):
        print(f"current balance = ${self.account_balance:.2f}")

my_account = BankAccount()
        