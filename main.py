# Class

#  class Item:
#     def calculate(self,x, y):
#         print("here: ")
#         return x*y

# item1 = Item()
# item1.name = "blue birds"
# item1.price = 33
# item1.quantity = 4

# item2 = Item()
# item2.name = "red birds"
# item2.price = 20
# item2.quatity = 4

# print(item1.calculate(item1.price, item1.quantity))
import csv

from item import Item
from phone import Phone


item1 = Item("laptop", 100, 3)
item2 = Item("Phone", 50, 5)
# item1.__name = "new"
print(item1.name)
item1.has_numpy = False

print(item2.calc())
# print(Item.__dict__) # see all atributes at class level
# print(item1.__dict__) # see all atributes at instance level

print(f"old price: {item1.price}")
item1.discount()
print("latest price: ", item1.price)
Item.instance_from_csv()

samsung = Phone('a7', 20,2,1)
print("HERE",repr(item2))
print("HERE",repr(samsung))
print(samsung.calc())
