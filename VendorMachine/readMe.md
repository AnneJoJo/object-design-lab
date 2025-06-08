# 🧃 Vending Machine System (OOP + State Machine)

A minimal, object-oriented vending machine simulation implemented in Python.  
Features include product management, coin-based change distribution, and state-controlled transaction flow.

---

## 🚀 Features

- 🧱 **OOP Design** — Core modules split into Product, CoinManager, VendorMachine
- 🧭 **State Machine Control** — Built-in `MachineState` enum enforces logical transitions (IDLE → PAYMENT → DISPENSING)
- 🪙 **Optimal Change Calculation** — CoinManager returns minimal change using a greedy algorithm with inventory control
- 🧃 **Product Metadata** — Product class includes support for type, quantity, calorie/temperature logic
- 🖥️ **Command-line Interface** — Simple CLI loop for inserting money, selecting products, and receiving change

---

## 🧩 System Structure
```plaintext
VendorMachine
├── CoinManager
│ └── arrange_change()
├── Product (w/ category: drink/snack)
│ ├── is_cold()
│ └── calories()
└── MachineState (Enum)
├── IDLE
├── WAITING_FOR_PAYMENT
├── PAYMENT_RECEIVED
└── DISPENSING
├── VendorMachine
│ ├── __init__()
└── readMe.md (this file)
```


---

## 🔧 Usage

```bash
python vending_machine.py

# Example commands:
Welcome to the Vending Machine System!

Available Products:
1. Coke - $1.5 (20 left)
2. Chocolate - $2.0 (15 left)

Insert your bill: 2
Select product number: 1
Dispensing Coke. Change: ['quarter']

Make another purchase? (y/n): n
Thanks for using the vending machine.
```