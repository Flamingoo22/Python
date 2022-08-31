from game_classes.character import Character

class Pokemon(Character):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.health = 80
        self.strength = 110
        self.type = type
        
    def print_info(self):
        super().print_info()
        print(self.type)
        return self

bulbasaur = Pokemon("grass")