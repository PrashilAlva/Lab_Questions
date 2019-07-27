class Account:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance

    def deposit(self,deposit_amount):
        self.balance=self.balance+deposit_amount

    def withdraw(self,withdraw_amount):
        self.balance=self.balance+withdraw_amount

    def showinfo(self):
        print(f'Account Number:{self.accno}')
        print(f'Name:{self.name}')
        print(f'Balance:{self.balance}')


        