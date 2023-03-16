class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance=balance
    def getbalance(self):
        print("your balance is:")
        return self.balance
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("after deposited balance is:")
        return self.balance
    def withdrawal(self,amount):
        self.amount = amount
        self.balance= self.balance-self.amount
        print("after withdrawal balance is:")
        return self.balance

class SavingAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate 
    def InterestAmount(self):
        print("interest amount is : ")
        return((self.interestRate*self.balance)//100)
    def display(self):
        return f"{self.title} has balance{self.balance} in account and interest is :{self.interestRate}"


obj= SavingAccount("Ashish",2000,5)
print(obj.display())
print(obj.InterestAmount())              

print(obj.getbalance())
print(obj.deposit(500))
print(obj.withdrawal(500))