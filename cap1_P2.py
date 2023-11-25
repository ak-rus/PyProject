from datetime import datetime

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((datetime.now(), 'Deposit', amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append((datetime.now(), 'Withdrawal', amount))
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class CheckingAccount(Account):
    pass

class CreditAccount(Account):
    def __init__(self, account_number, credit_limit=0):
        super().__init__(account_number)
        self.credit_limit = credit_limit

    def charge(self, amount):
        if self.balance + amount <= self.credit_limit:
            self.balance += amount
            self.transactions.append((datetime.now(), 'Charge', amount))
        else:
            print("Credit limit exceeded")

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_type, account_number, initial_balance=0):
        if account_type == "checking":
            self.accounts[account_number] = CheckingAccount(account_number, initial_balance)
        elif account_type == "credit":
            self.accounts[account_number] = CreditAccount(account_number, initial_balance)
        else:
            print("Invalid account type")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_all_accounts(self):
        return self.accounts

# Example Usage
if __name__ == "__main__":
    # Create a customer
    john = Customer("John Doe")

    # Create accounts for the customer
    john.create_account("checking", "C123", 1000)
    john.create_account("credit", "CR456", 5000)

    # Make transactions
    john.get_account("C123").deposit(500)
    john.get_account("CR456").charge(1000)
    john.get_account("C123").withdraw(200)

    # Display transactions for a specific account
    for account_num, account in john.get_all_accounts().items():
        print(f"Transactions for account {account_num}:")
        for transaction in account.get_transactions():
            print(transaction)
