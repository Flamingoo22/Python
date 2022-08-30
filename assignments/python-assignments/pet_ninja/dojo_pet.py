class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = [treats]
        self.pet_food = [pet_food]
        self.pet = pet
        
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self,food):
        if food in self.pet_food:
            self.pet.eat(food)
        else:
            print(f"You don't have {food}")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    
    
class Pet:
    health = 100
    energy = 10
    def __init__(self, name, type, tricks,owner=None):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.owner = owner

        
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self,food):
        if self.owner == None:
            print(f"{self.name} needs an owner")
        elif food in self.owner.pet_food:
            self.owner.pet_food.remove(food)
            self.energy += 5
            self.health += 10
            print(f"{self.name} loves eating {food}")
        else:
            print(f"{self.owner.last_name} is broke.")
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print("Awwwww")
        return self
    

Goofy = Pet("Goofy","dog","Lick")

Fan = Ninja("Fan", "Q","Dog food", "Dog snack", Goofy)

Goofy.owner = Fan

Goofy.noise

Fan.bathe().feed("Dog snack")

Goofy.eat("Pineapple")

Jane = Pet("Jane", "cat", "Scratch")

Jane.eat("Fish")