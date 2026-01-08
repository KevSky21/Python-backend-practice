from efficient_inventory_class import Inventory
from efficient_item_class import Item


def menu(inventory: Inventory) -> None:
    while True:
        print("\nEnter a number to choose an action")
        print("-----------------------------------")
        choice = input(
            "1. Add Inventory\n"
            "2. Delete Inventory\n"
            "3. Edit Inventory\n"
            "4. Print Inventories\n"
            "5. Exit\n"
        )

        if choice == "1":
            name = input("Enter inventory name: ")
            inventory.add_inventory(name)

        elif choice == "2":
            name = input("Enter inventory name to delete: ")
            inventory.remove_inventory(name)

        elif choice == "3":
            inv_name = input("Enter inventory name to add to: ")
            item = create_item()
            inventory.add_item(inv_name, item)

        elif choice == "4":
            inventory.print_inventory()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


def create_item() -> Item:
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    value = float(input("Enter value: "))
    return Item(name, quantity, value)


def main():
    storage = Inventory()
    menu(storage)


if __name__ == "__main__":
    main()
