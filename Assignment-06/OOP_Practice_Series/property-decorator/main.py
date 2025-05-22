class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting the price")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting the price")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price")
        del self._price


# Usage example:
p = Product(100)

print(p.price)     # Get the price

p.price = 150      # Update the price
print(p.price)

p.price = -50      # Try to set invalid price

del p.price        # Delete the price

