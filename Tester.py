from Account import Account
from Bank import Bank


def test():
    bankName = "BOA"
    bank = Bank(bankName)

    account1 = Account("Simon", 19,     0, [])
    account2 = Account("Bati",  16,  3000, [])
    account3 = Account("Saron", 23,  1000, [])
    account4 = Account("James", 30, 50000, [])
    
   
    bank.addAccount(account1)
    bank.addAccount(account2)
    bank.addAccount(account3)
    bank.addAccount(account4)

    while True:
        accNum = int(input("Enter account number "))

        if accNum == -1:
            break

        for acc in bank.accounts:
            if acc.acccountNumber == accNum:
                type = input("What would you like to do today? Enter deposit or Withdraw ").lower()

                if type == "deposit":
                    quatity = int(input("how much would you like to deposit today? "))
                    acc.deposit(quatity)
                    print(acc.transactions[-1].display())
                    break

                elif type == "withdraw":
                    quatity = int(input("how much would you like to withdraw today? "))
                    acc.withdraw(quatity)
                    print(acc.transactions[-1].display())
                    break
                else:   
                    print("Action not recognized, input again")
                    continue

    for account in bank.accounts:
        print(account.ownerName + " has a balace of " + str(account.balance))
         
test()