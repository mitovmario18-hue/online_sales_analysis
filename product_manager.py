from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added.")

    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' removed successfully.")
                return
        print(f"Product '{name}' not found.")