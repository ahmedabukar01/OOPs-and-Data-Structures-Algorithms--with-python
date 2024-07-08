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
class Item:
    pay_rate = 0.8 # class attribute
    def __init__(self, name: str, price: float, quantity=0):
        # Validate the receiving arguments
        assert price >= 0, "Price should not less than 1"
        assert quantity >=0, f"Quantity {quantity} cannot be 0 or negetive numbers"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc(self):
        return self.price * self.quantity
    def discount(self):
        self.price = self.price * Item.pay_rate
    
    @classmethod
    def instance_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items: 
            print("item: ",item)
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # count out floats that are point zero. ex: 10.0, 5.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

item1 = Item("laptop", 100, 3)
item2 = Item("Phone", 50, 5)

item1.has_numpy = False

print(item2.calc())
print(Item.__dict__) # see all atributes at class level
print(item1.__dict__) # see all atributes at instance level

print(f"old price: {item1.price}")
item1.discount()
print("latest price: ", item1.price)
Item.instance_from_csv()

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name,price,quantity)

        assert broken_phones >0, f"broken phones {broken_phones} is not greater than or equal to zero!"

        self.broken_phones = broken_phones

samsung = Phone('a7', 20,2,1)
print(samsung.calc())