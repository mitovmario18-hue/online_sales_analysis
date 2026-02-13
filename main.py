from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    # dostupni proizvodi
    p1 = Product("Laptop", 1200, 2)
    p2 = Product("Mouse", 25, 3)
    p3 = Product("Keyboard", 75, 1)
    p4 = Product("Monitor", 300, 1)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)

    # korpa
    cart = Cart()

    # dodaj 3 proizvoda iz liste dostupnih proizvoda (iz managera)
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

    print("\nCart content:")
    cart.display_cart()

    print("\nTotal to pay:")
    print(cart.calculate_total())


if __name__ == "__main__":
    main()