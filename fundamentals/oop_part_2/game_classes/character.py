class Character:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.level = 1
        self.defense = 5
        
    def attack(self, target):
        print("attacking")
        target.defend(self.strength)
        return self
    
    def defend(self,damage):
        actual_damage = damage - self.defense
        self.health -= actual_damage
        return self
    
    def heal(self):
        self.health += 10
        
    def print_info(self):
        print(f"health:{self.health} strength:{self.health} level: {self.level} defense: {self.defense}")
        return self