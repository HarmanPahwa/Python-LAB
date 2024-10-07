class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposite: {amount}, current balance: {self.balance}")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficent balance")
            
        else:
            self.balance -= amount
            print(f"withdraw: {amount}, current balance: {self.balance}")
            
    def check_balance(self):
        print(f"account balance: {self.balance}")
        
account = BankAccount("abc")
account.deposit(2000)
account.withdraw(5000)
account.check_balance