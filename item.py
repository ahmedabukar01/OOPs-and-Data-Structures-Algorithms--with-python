import csv
class Item:
    pay_rate = 0.8 # class attribute
    def __init__(self, name: str, price: float, quantity=0):
        # Validate the receiving arguments
        assert price >= 0, "Price should not less than 1"
        assert quantity >=0, f"Quantity {quantity} cannot be 0 or negetive numbers"

        # assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self): 
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
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
    def __repr__(self):
        return f"({self.__class__.__name__} {self.name} {self.price} {self.quantity})"
    
    # this is called abstraction. "its a oops principle, it's way to make private methods that are not being used in other places."
    def __prepare_body(self):
        pass
    def __connect(self):
        pass

    def send_email(self):
        self.__prepare_body()
        self.__connect()


   