class BankAccount:
    def __init__(self, starting_balance=0):
        self.account_balance = float(starting_balance)

    def deposit(self, amount):
        amount = float(amount)
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
