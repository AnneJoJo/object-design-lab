
from typing import Dict, Optional
from Product import Product
from CoinManager import CoinManager
from State import MachineState

class VendorMachine:
    def __init__(self):
        self.products: Dict[int, Product] = {
            1: Product("Coke", 1.5, 20, category="drink"),
            2: Product("Chocolate", 2.0, 15, category="snack")
        }
        self.coin_manager = CoinManager()
        self.state = MachineState.IDLE
        self.last_selected_product_id: Optional[int] = None
        self.last_bill_inserted: Optional[float] = None

    def display_products(self):
        print("\nAvailable Products:")
        for pid, product in self.products.items():
            print(f"{pid}. {product.name} - ${product.price} ({product.quantity} left)")

    def validate_payment(self, bill: float) -> bool:
        return 0 < bill <= 10

    def insert_payment(self, bill: float):
        if self.state != MachineState.WAITING_FOR_PAYMENT:
            print("Machine is not ready to accept payment.")
            return False
        if not self.validate_payment(bill):
            print("Invalid bill.")
            return False
        self.last_bill_inserted = bill
        self.state = MachineState.PAYMENT_RECEIVED
        return True

    def select_product(self, product_id: int):
        if self.state != MachineState.PAYMENT_RECEIVED:
            print("Please insert payment first.")
            return None
        product = self.products.get(product_id)
        if not product or not product.is_available():
            print("Product not available.")
            return None
        self.last_selected_product_id = product_id
        return product

    def dispense_product(self):
        if self.state != MachineState.PAYMENT_RECEIVED:
            print("Transaction not ready.")
            return
        product = self.products.get(self.last_selected_product_id)
        bill = self.last_bill_inserted
        if not product or bill is None:
            print("Invalid transaction context.")
            return
        if bill < product.price:
            print("Insufficient funds.")
            return

        change_due = bill - product.price
        try:
            change = self.coin_manager.arrange_change(change_due)
        except ValueError as e:
            print(f"Change error: {e}")
            return

        product.dispense()
        print(f"Dispensing {product.name}. Change: {change}")
        self.state = MachineState.IDLE
        self.last_bill_inserted = None
        self.last_selected_product_id = None

    def reset(self):
        self.state = MachineState.IDLE
        self.last_bill_inserted = None
        self.last_selected_product_id = None
def run():
    vm = VendorMachine()
    print("Welcome to the Vending Machine System!\n")

    while True:
        vm.display_products()
        vm.state = MachineState.WAITING_FOR_PAYMENT

        try:
            bill = float(input("Insert your bill: "))
        except ValueError:
            print("Invalid input.\n")
            continue

        if not vm.insert_payment(bill):
            continue

        try:
            product_id = int(input("Select product number: "))
        except ValueError:
            print("Invalid product selection.\n")
            continue

        if not vm.select_product(product_id):
            vm.reset()
            continue

        vm.dispense_product()

        cont = input("Make another purchase? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thanks for using the vending machine.")
            break

if __name__ == '__main__':
    run()
# This code is the main entry point for the vending machine system.