class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

savings_acct = SavingsAccount("Anup", 5000, 5)


print(savings_acct.title)
print(savings_acct.balance)
print(savings_acct.interestRate)