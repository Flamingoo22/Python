class Shoe:
    def __init__(self):
        self.brand = "Adidas"
        self.type = "tennis shoe"
        self.price = 45.99
        self.in_stock = True
    
    def rebrand(self, new_brand):
        self.brand = new_brand
    
    def sold_out(self):
        self.in_stock = False
        
    def on_sale(self,percent):
        self.price = self.price* (1-percent)
        