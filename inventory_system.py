# Inventory Management System (PS No. 9)
# Each item is a dictionary: {"id": "I101", "name": "Pen", "quantity": 50, "price": 10}
# All items are stored together in a list called "inventory".

inventory = []          # list that stores all the items
next_number = 101       # used to create IDs like I101, I102, ...
LOW_STOCK_LIMIT = 5     # low stock means quantity below 5

def show_item(item):
    # Print one item in a single line
    print(f"ID: {item['id']} | {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")

def find_item(item_id):
    # Look for an item by its ID. Return the item, or None if not found
    for item in inventory:
        if item["id"] == item_id.upper():
            return item
    return None

def check_quantity(text):
    # Quantity must be a whole number that is 0 or more
    if text.isdigit():              # "-5", "abc" and "2.5" are not digits only
        return int(text)
    print("Invalid quantity. Quantity must be a non-negative whole number.")
    return None

def check_price(text):
    # Price must be a number that is 0 or more
    try:
        price = float(text)
    except ValueError:              # happens when the user types letters
        price = -1
    if price < 0:
        print("Invalid price. Price must be a non-negative number.")
        return None
    if price.is_integer():          # show 10 instead of 10.0
        price = int(price)
    return price

def add_item():
    global next_number
    name = input("Name: ").strip()
    quantity_text = input("Quantity: ").strip()
    price_text = input("Price: ").strip()
    quantity = check_quantity(quantity_text)
    price = check_price(price_text)
    if name == "" or quantity is None or price is None:
        print("Item not added.")
        return
    item = {"id": "I" + str(next_number), "name": name, "quantity": quantity, "price": price}
    next_number = next_number + 1       # next item gets a new unique ID
    inventory.append(item)
    print("Item added.")
    show_item(item)
    if quantity < LOW_STOCK_LIMIT:
        print(f"Low stock alert: {name} ({quantity})")

def view_items():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print(f"{'ID':<8}{'Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 48)
    for item in inventory:
        print(f"{item['id']:<8}{item['name']:<20}{item['quantity']:<10}{item['price']:<10}")

def update_item():
    item_id = input("Enter item ID: ").strip()
    item = find_item(item_id)
    if item is None:
        print(f"Item ID {item_id.upper()} not found.")
        return
    quantity = check_quantity(input("New quantity: ").strip())
    price = check_price(input("New price: ").strip())
    if quantity is None or price is None:
        print("Item not updated.")
        return
    item["quantity"] = quantity
    item["price"] = price
    print("Item updated.")
    show_item(item)

def search_item():
    word = input("Enter item ID or name to search: ").strip().lower()
    found = False
    for item in inventory:
        if word in item["id"].lower() or word in item["name"].lower():
            show_item(item)
            found = True
    if not found:
        print("No matching item found.")

def delete_item():
    item_id = input("Enter item ID: ").strip()
    item = find_item(item_id)
    if item is None:
        print(f"Item ID {item_id.upper()} not found.")
        return
    inventory.remove(item)
    print(f"Item '{item['name']}' deleted. Items left: {len(inventory)}")

def total_stock_value():
    total = 0
    parts = []
    for item in inventory:
        value = item["quantity"] * item["price"]    # quantity x price
        total = total + value
        parts.append(f"{item['name']}: {value}")
    print(" | ".join(parts))
    print("Total stock value:", total)

def low_stock_report():
    found = False
    for item in inventory:
        if item["quantity"] < LOW_STOCK_LIMIT:
            print(f"Low stock (below {LOW_STOCK_LIMIT}): {item['id']} | {item['name']} | Qty: {item['quantity']}")
            found = True
    if not found:
        print("No low stock items.")

def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add item")
        print("2. View all items")
        print("3. Update item")
        print("4. Delete item")
        print("5. Total stock value")
        print("6. Low stock report")
        print("7. Search item")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            total_stock_value()
        elif choice == "6":
            low_stock_report()
        elif choice == "7":
            search_item()
        elif choice == "8":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

main()
