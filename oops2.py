class bank_account: #class and class name
    def __init__(self): 
        self.balance = 0
        print("Welcome to Deposit and Withdraw Machine...")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited= "))
        self.balance += amount
        print("\nAmount Deposited: ",amount)

    def withdraw(self):
        amount = float(input("\nEnter amount of withdrawing= "))
        if self.balance >= amount :
            self.balance -= amount
            print("\nwithdraw: ",amount)
        else:
            print("\nInsufficient Blanace")
    
    def display(self):
        print("\n Net Available Balance= ",self.balance)

s = bank_account()

s.deposit()
s.withdraw()
s.display()