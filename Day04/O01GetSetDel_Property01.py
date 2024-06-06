
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print('getter called.....')
        return self.__price

    def set_price(self, val):
        print("setter called......")
        self.__price = val

    def del_price(self):
        print("deleter called.......")
        self.__price = 0

    price = property(get_price, set_price, del_price)


pepsi  = Product(50)
print(pepsi.price)
pepsi.price = 120
print(pepsi.price)
del pepsi.price
print(pepsi.price)


"""    

pepsi = Product(50)
print(pepsi.get_price())
pepsi.set_price(120)
print(pepsi.get_price())
pepsi.del_price()
print(pepsi.get_price())
"""