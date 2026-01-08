from inventory_class import Inventory
from item_class import Item


def menu(inventory: Inventory) -> None:
    inv_choice = ""

    while inv_choice != "5":
        print(f"Enter a number to choose an action")
        print(f"-----------------------------------")
        inv_choice = input("1. Add an Inventory | 2. Delete an Inventory | 3. Edit an Inventory | 4. Print an Inventory | 5. Exit\n")
        if inv_choice == "1":
            inventory_name = input("Enter your inventory name: ")
            inventory.add_inventory(inventory_name)
        elif inv_choice == "2":
            inventory.remove_inventory(input("Enter Inventory Name: "))
        elif inv_choice == "3":
            inventory_name = input("Enter your inventory name to add to: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            value = float(input("Enter value of item: "))
            item = Item(name, quantity, value)
            inventory.edit_inventory(inventory_name, item)

        elif inv_choice == "4":
            inventory.print_inventory()
        elif inv_choice == "5":
            print("Exiting")
        else:
            print("Invalid choice")

def main():
    my_storage = Inventory()
    menu(my_storage)



if __name__ == "__main__":
    main()
