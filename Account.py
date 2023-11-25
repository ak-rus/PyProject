from Transaction import Transaction
class Account:
    def __init__(self, ownerName, accountNumber, balance, transactions):
        self.ownerName = ownerName
        self.acccountNumber = accountNumber
        self.balance = balance
        self.transactions = transactions
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Not enough balance")
        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount))
    
    def balance(self):
        return "Current Balance: " + str(self.balance)
    