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
        
    def enroll(self):
        if self.is_rewards_member == True:
            return print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return print("Thank you for joining Rewards Member!")

    def spend_points(self,amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            return print(f"You have {self.gold_card_points} points remain.")
        else:
            return print("Insufficient amount.")
            

user1 = User("Q","Liu","abra@mail.com",21)

# user1.display_info()

user1.enroll()

user2 = User("Dur","Ann","durrr@mail.com",31)
user3 = User("Phil","Ivy","phil@mail.com",172)

user1.spend_points(50)

user2.enroll()

user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

