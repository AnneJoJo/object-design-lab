
from typing import List


class CoinManager:
    """
    Handles coin arrangement and inventory for change-making.
    """
    def __init__(self):
        self.denominations = [25, 10, 5, 1]  # cents
        self.names = {1: 'penny', 5: 'nickel', 10: 'dime', 25: 'quarter'}
        self.inventory = {name: 100 for name in self.names.values()}

    def arrange_change(self, amount: float) -> List[str]:
        cents = int(round(amount * 100))
        result = []
        for coin in self.denominations:
            name = self.names[coin]
            while cents >= coin and self.inventory[name] > 0:
                cents -= coin
                result.append(name)
                self.inventory[name] -= 1
        if cents != 0:
            raise ValueError("Cannot make exact change with available coins.")
        return result

    def restock(self, name: str, count: int):
        if name in self.inventory:
            self.inventory[name] += count
