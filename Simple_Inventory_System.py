class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Quantity of '{self.name}' updated. New quantity: {self.quantity}")

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Total Value: ${self.calculate_total_value():.2f}\n")

    def calculate_total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"'{product.name}' has been added to the inventory.\n")

    def display_all_products(self):
        if not self.products:
            print("No products in the inventory.\n")
        else:
            for product in self.products:
                product.display_info()

    def calculate_inventory_value(self):
        total_value = sum(product.calculate_total_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}\n")
        return total_value


# Example usage
if __name__ == "__main__":
    # Create product objects
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 599.99, 25)
    product3 = Product("Headphones", 199.99, 50)

    store_inventory = Inventory()

    store_inventory.add_product(product1)
    store_inventory.add_product(product2)
    store_inventory.add_product(product3)

    print("Inventory:\n")
    store_inventory.display_all_products()

    product1.update_quantity(5)

    print("Updated Inventory:\n")
    store_inventory.display_all_products()

    store_inventory.calculate_inventory_value()
