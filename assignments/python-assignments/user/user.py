class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        if self.is_rewards_member == True:
            return print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Thank you for joining Rewards Member!")
            return self

    def spend_points(self,amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"You have {self.gold_card_points} points remain.")
            return self
        else:
            print("Insufficient amount.")
            return self

user1 = User("Q","Liu","abra@mail.com",21)

# user1.display_info()

user1.display_info().enroll().spend_points(50).display_info()

user2 = User("Dur","Ann","durrr@mail.com",31)
user3 = User("Phil","Ivy","phil@mail.com",172)

user2.enroll().spend_points(80).display_info()

user3.display_info()

