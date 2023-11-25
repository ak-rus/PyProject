class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def display(self):
        return "Processed " + self.type + " of " + str(self.amount)
    