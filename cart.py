class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Product '{product.name}' added to cart.")

    def calculate_total(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
            return

        for product in self.cart_items:
            print(f"{product.name} - Price: {product.price}, Quantity: {product.quantity}")