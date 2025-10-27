"""
Inventory System Module
"""

import json
from datetime import datetime


stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add quantity of an item to the stock and log the operation.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to add.
        logs (list): List to append operation log.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        return
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a quantity of an item from the stock.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """
    Get the quantity of a specific item.
    Args:
        item (str): Name of the item.
    Returns:
        int: Quantity of the item.
    """
    return stock_data.get(item, 0)


def load_data(filename="inventory.json"):
    """
    Load stock data from a JSON file.
    Args:
        filename (str): Path to the JSON file.
    """
    global stock_data
    try:
        with open(filename, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}
    except json.JSONDecodeError:
        stock_data = {}


def save_data(filename="inventory.json"):
    """
    Save stock data to a JSON file.
    Args:
        filename (str): Path to the JSON file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def print_data():
    """
    Print all items and their quantities.
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Return a list of items with quantity below threshold.
    Args:
        threshold (int): Threshold value.
    Returns:
        list: Items below the threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Demonstration of inventory system features.
    """
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)
    add_item(123, "ten", logs)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('eval used')
    for log_entry in logs:
        print(log_entry)


if __name__ == "__main__":
    main()
