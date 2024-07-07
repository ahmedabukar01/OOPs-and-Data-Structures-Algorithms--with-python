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

class Item:
    def __init__(self, name, price, quantity=0):
        # Validate the receiving arguments

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc(self):
        return self.price * self.quantity
        
item1 = Item("laptop", 200, 3)
item2 = Item("Phone", 50, 5)

item1.has_numpy = False

print(item2.calc())
