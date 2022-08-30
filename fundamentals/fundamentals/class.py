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


# It's important to know that class methods have no access to the instance attribute or any attribute that starts with self.

# Static methods are functions defined within the class with a decorator @staticmethod.  They have no access on instance or class attributes, so if we need any existing values, they need to be passed in as arguments.

# constructor function is called when class set

x = 6 + "5"