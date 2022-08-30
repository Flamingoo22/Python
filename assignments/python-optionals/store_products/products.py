import uuid


class Product:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4()
        
    def __repr__(self):
        return f"name: {self.name}, id: {self.id}"
        
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
    
    def print_info(self):
        print(f"{self.name}")
        print(f"{self.price}")
        print(f"{self.category}")
        return self
    
