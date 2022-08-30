from products import Product
from store import Store

p1 = Product("Potato",2,"Vegetable")
p2 = Product("Tomato",2,"Fruit")
p3 = Product("Beef",2,"Meat")
p4 = Product("Chicken",2,"Meat")
km = Store("Kims_Conveniance")

km.add_product(p1)
km.add_product(p2)
km.add_product(p3)
km.add_product(p4)

km.inflation(.2)

km.set_clearance("Meat",0.5)

print(p4.price)

print(km.products)

km.sell_product(p4.id)

print(km.products)