class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        # for attrs in __init___:
        BankAccount.all_accounts.append(self.int_rate)
        BankAccount.all_accounts.append(self.balance)
        
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        # your code here
        if amount < self.balance:
            self.balance -= amount  
            return self
        else:
            print("Insufficient Balance")
            return self
    
    def display_account_info(self):
    #     # your code here
        print(f"interest rate = {self.int_rate}")
        print(f"balance = {self.balance}")
        return self
        
    def yield_interest(self):
    #     # your code here
        if self.balance > 0:
            self.int_rate = self.balance * self.int_rate
            return self
            
    @classmethod
    def show_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)
    

user1 = BankAccount(.01, 2000)
user2 = BankAccount(.02, 210000)

# user1.deposit(2000).deposit(20).deposit(400).withdraw(5000).display_account_info()
# user2.deposit(200).deposit(120).withdraw(15000).withdraw(300).withdraw(399).withdraw(233).yield_interest().display_account_info()

BankAccount.show_all_accounts()

print(vars(BankAccount))