# from assignments.pet_ninja.dojo_pet import Pet
from dojo_pet import Pet

class Advanced_Pet(Pet):
    def __init__(self, name, type, tricks, skill,owner=None):
        super().__init__(name, type, tricks, owner)
        self.skill = skill
        
    def use_skill(self):
        print(f"{self.name} use {self.skill} \n It is not effective")

Psyduck = Advanced_Pet("Psyduck","Water", "Tail Swing", "Water Gun")

Psyduck.use_skill()