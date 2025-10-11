class BankAccount:
    def __init__(self, starting_balance=0):
        self.account_balance = starting_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.1f}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.1f}"
