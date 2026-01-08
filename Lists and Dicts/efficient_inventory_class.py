from item_class import Item


class Inventory:
    def __init__(self):
        self.inventories = []

    def add_inventory(self, name: str) -> None:
        self.inventories.append({
            "name": name,
            "items": {}
        })
        print(f"Added inventory '{name}'")

    def remove_inventory(self, name: str) -> None:
        for inv in self.inventories:
            if inv["name"] == name:
                self.inventories.remove(inv)
                print(f"Removed inventory '{name}'")
                return
        print(f"Inventory '{name}' not found.")

    def add_item(self, inventory_name: str, item: Item) -> None:
        for inv in self.inventories:
            if inv["name"] == inventory_name:
                inv["items"][item.name] = item
                print(f"Added {item.name} to {inventory_name}")
                return
        print(f"Inventory '{inventory_name}' not found.")

    def print_inventory(self) -> None:
        if not self.inventories:
            print("No inventories available.")
            return

        for inv in self.inventories:
            print(f"\nInventory: {inv['name']}")
            if not inv["items"]:
                print("  (empty)")
            for item in inv["items"].values():
                print(f"  - {item}")
