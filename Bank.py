class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = [] 
    
    def addAccount(self, account):
        if account and account not in self.accounts:
            self.accounts.append(account)
    
    
    
