from item_class import Item

class Inventory:
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inv_name:str):

            inventory_dict ={
                "name": inv_name,
                "items": {}
            }
            self.inventories.append(inventory_dict)
            print(f"Added {inv_name}")

    def remove_inventory(self, inventory_name):
        try:
            for inv in self.inventories:
                if inv["name"] == inventory_name:
                    self.inventories.remove(inv)
                print(f"Removed {inventory_name}")
                return
        except ValueError:
            print(f"The inventory {inventory_name} was not found.")


    def edit_inventory(self, inventory_name:str, item:Item):
       for names in self.inventories:
           if names["name"] == inventory_name:
            names[f"items"][item.name] = item
            return

    def get_inventory(self):
        pass

    def print_inventory(self):
        for inv in self.inventories:
            print(f"\nInventory: {inv['name']}")
            for item in inv["items"].values():
                print(f"  - {item}")



