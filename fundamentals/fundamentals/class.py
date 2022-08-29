class Shoe:
    def __init__(self, brand, type, price, in_stock):
        self.brand = brand
        self.type = type
        self.price = price
        self.in_stock = in_stock
    
    def rebrand(self, new_brand):
        self.brand = new_brand
    
    def sold_out(self):
        self.in_stock = False
        
    def on_sale(self,percent):
        self.price = self.price* (1-percent)
        
        
        
Adidas = Shoe("Adidas", "sport_shoe", 70, True) 

print(Adidas.type)

Adidas.on_sale(.3)

print(Adidas.price)

Adidas.on_sale(.2)

print(Adidas.price)