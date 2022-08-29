class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self.int_rate)
        BankAccount.all_accounts.append(self.balance)
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount  
            return self
        else:
            print("Insufficient Balance")
            return self
    
    def display_account_info(self):
        print(f"interest rate = {self.int_rate}")
        print(f"balance = {self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.int_rate = self.balance * self.int_rate
            return self
            
    @classmethod
    def show_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)
            return cls



class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = {}
    
    def make_bank_account(self,account_number):
        if f"account_{account_number}" not in self.account:
            self.account[f"account_{account_number}"]=(BankAccount(0.01,0))
            return self
        else:
            print("Account already exist")
    
    def make_deposit(self,account_number,amount):
        if amount > 0:
            self.account[f"account_{account_number}"].balance += amount
            return self
    
    def make_withdrawal(self,account_number,amount):
        if amount < self.account[f"account_{account_number}"].balance:
            self.account[f"account_{account_number}"].balance -= amount
            return self
        else:
            print("Insufficient Balance")
            return self
        
    def make_transfer(self,transfer_from, transfer_to, amount):
        if amount < self.account[f"account_{transfer_from}"].balance:
            self.account[f"account_{transfer_from}"].balance -= amount
            self.account[f"account_{transfer_to}"].balance += amount
            return self
        else:
            print("Insufficient Balance")
            return self
        
    def display_user_balance(self):
        for acc in range(1,len(self.account)+1):
            accounts = self.account[f"account_{acc}"].balance
            print(f"Account {acc} has balance of ${accounts}.")
        return self

user1 = User("Jon", "Cena")

# user1.make_deposit(1000)

# user1.account.display_account_info()

user1.make_bank_account(1)
user1.make_bank_account(1)
user1.make_bank_account(2)


user1.make_deposit(1,3000).make_deposit(2,2000).make_transfer(2,1,210).display_user_balance()