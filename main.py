from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    p1 = Product("Gaming Laptop", 1500, 1)
    p2 = Product("Wireless Mouse", 30, 2)
    p3 = Product("Mechanical Keyboard", 90, 1)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)


if __name__ == "__main__":
    main()