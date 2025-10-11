class BankAccount:
    def __init__(self, starting_balance=0):
        self.account_balance = starting_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")  # Format like 50.0 not 50

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")  # Print once, properly formatted
            return True
        else:
            print("Insufficient funds.")  # Add period and exact casing
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
