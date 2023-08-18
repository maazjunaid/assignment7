class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity


class ElectronicsItem(CartItem):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def calculate_item_price(self):
        return super().calculate_item_price() + (self.price * self.quantity * 0.1)


class ClothingItem(CartItem):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def calculate_item_price(self):
        return super().calculate_item_price() - (self.price * self.quantity * 0.05)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_cart(self):
        for item in self.items:
            print(f"{item.name} - Quantity: {item.quantity}, Price: ${item.calculate_item_price():.2f}")

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.calculate_item_price()
        return total_price


laptop = ElectronicsItem("Laptop", 1000, 7, 2)
shirt = ClothingItem("Shirt", 25, 5, "M")
phone = ElectronicsItem("Phone", 500, 3, 1)

cart = ShoppingCart()

cart.add_item(laptop)
cart.add_item(shirt)
cart.add_item(phone)


cart.show_cart()

total_price = cart.calculate_total_price()
print(f"Total Cart Price: ${total_price:.2f}")