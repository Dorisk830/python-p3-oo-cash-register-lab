#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize CashRegister defaulting to 0.
        self.discount = discount
        self.total = 0
        self.items = []
        self.recent_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add item to the register
        self.total += price * quantity
        # Add the item to the list
        self.items.extend([item] * quantity)
        # keep recent transactions made.
        self.recent_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        # Apply a discount
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last transaction by subtracting cost from the total.
        if not self.recent_transactions:
            return "There are no transactions to void."
        last_transaction = self.recent_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove the items from the items list based on the last transaction's quantity.
        self.items = self.items[:-last_transaction["quantity"]]
