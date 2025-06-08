from typing import Dict, List, Optional

from CoinManager import CoinManager

class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str = "general"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def is_available(self) -> bool:
        return self.quantity > 0

    def dispense(self):
        if self.quantity <= 0:
            raise ValueError("Product out of stock.")
        self.quantity -= 1

    def is_cold(self) -> bool:
        return self.category == "drink"

    def calories(self) -> Optional[int]:
        if self.category == "snack":
            return 200
        return None



