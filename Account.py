class Account:
    def __init__(self):
        self.accountNumber=0
        self.accountType=None
        self.accountHOlderName=None
        self.Balance=0


    def setDetails(self,ACNumber,AcType,AcHolderName,Balance):
        self.accountNumber=ACNumber
        self.accountType=AcType
        self.accountHolderName=AcHolderName
        self.Balance=Balance

    def getDetails(self):
        print("Account Number: ",self.accountNumber)
        print("Account Holder Name: ",self.accountHolderName)
        print("Account Type: ",self.accountType)
        print("Account Balance: ",self.Balance)

    def BalanceA(self):
        print("Account Balance is: ")
        return self.Balance

    def withdraw(self,amount):
        self.Balance=self.Balance-amount
        print("Withdraw sucessfully: ")
        return self.Balance

    def diposit(self,amount):
        self.Balance=self.Balance+amount
        print("Diposit Sucessfully:")
        return self.Balance
    def transfer(self,amount,user1):
        if self.Balance<amount:
            print("Not sufficient Balance please try again")
        else:
            user1.Balance=user1.Balance+amount
            self.Balance=self.Balance-amount
            print("Transfer Amount sucessfully")
            




user1=Account()
user1.setDetails(101,"saving","Mohammad Patel",2000)
user1.getDetails()
"""print(object.diposit(50000))
print(object.withdraw(25000))
print(object.BalanceA())"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
user2=Account()
user2.setDetails(102,"Business","Mehmud Patel",220000)

user2.getDetails()
print(".............................................................................")
user2.transfer(25000,user1)
print("After Transfer:")
print("User1 Balance:",user1.Balance)
print("User2 Balance",user2.Balance)
