class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def get_items(self):
        return self.items


def show_menu():
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. View total price")
    print("5. Exit")


def main():
    cart = ShoppingCart()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(item, price, quantity)
            print(f"{quantity} of {item} added to cart.")

        elif choice == '2':
            item = input("Enter item name to remove: ")
            cart.remove_item(item)
            print(f"{item} removed from cart.")

        elif choice == '3':
            items = cart.get_items()
            if not items:
                print("Cart is empty.")
            else:
                for item, details in items.items():
                    print(f"{item}: {details['quantity']} @ ${details['price']} each")

        elif choice == '4':
            total = cart.get_total()
            print(f"Total price: ${total:.2f}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()