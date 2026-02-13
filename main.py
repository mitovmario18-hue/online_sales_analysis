from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    p1 = Product("Laptop", 1200, 5)
    p2 = Product("Mouse", 25, 20)
    p3 = Product("Keyboard", 75, 10)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    print("Available products:")
    manager.display_products()

    print("\nTotal inventory value:", manager.total_inventory_value())


if __name__ == "__main__":
    main()