class Item:
    def __init__(self, name: str, quantity: int, value: float):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity}, Value: ${self.value:.2f})"
