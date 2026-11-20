# ==============================================================================
# PROJECT: INVENTORY MANAGEMENT SYSTEM
# COURSE: Bachelor of Technology (Computer Science and Engineering) - 1st Year
# CONCEPTS USED: Lists, Dictionaries, Functions, Loops, CRUD Operations
# ==============================================================================

# Global list to store all inventory items
# Each item will be stored as a dictionary:
# {'id': 'I101', 'name': 'Pen', 'quantity': 50, 'price': 10}
inventory = []

# Global counter for generating unique item IDs starting from 101 (e.g., I101, I102)
next_item_id = 101


def generate_item_id():
    """Generates a unique item ID starting from I101."""
    global next_item_id
    item_id = f"I{next_item_id}"
    next_item_id += 1
    return item_id


def format_price(value):
    """Helper function to format price cleanly (e.g., 10 instead of 10.0 if whole number)."""
    if isinstance(value, (int, float)):
        if value == int(value):
            return int(value)
        return round(value, 2)
    return value


# ------------------------------------------------------------------------------
# 1. ADD ITEM (Create)
# ------------------------------------------------------------------------------
def add_item():
    """Adds a new item to the inventory with quantity and price validation."""
    name = input("Enter item name: ").strip()
    if not name:
        print("Item name cannot be empty. Item not added.")
        return

    # Validate Quantity (must be a non-negative whole number)
    qty_input = input("Enter quantity: ").strip()
    try:
        quantity = int(qty_input)
        if quantity < 0:
            print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
            return
    except ValueError:
        print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
        return

    # Validate Price (must be a positive/non-negative number)
    price_input = input("Enter price: ").strip()
    try:
        price = float(price_input)
        if price < 0:
            print("Invalid price. Price must be a non-negative number. Item not added.")
            return
    except ValueError:
        print("Invalid price. Please enter a valid number. Item not added.")
        return

    # Generate unique ID and create dictionary
    item_id = generate_item_id()
    display_price = format_price(price)

    new_item = {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": display_price
    }

    # Add dictionary to inventory list
    inventory.append(new_item)

    print("Item added.")
    print(f"ID: {item_id} | {name} | Qty: {quantity} | Price: {display_price}")

    # Check for low stock alert upon adding (quantity < 5)
    if quantity < 5:
        print(f"Low stock alert: {name} ({quantity})")


# ------------------------------------------------------------------------------
# 2. VIEW ITEMS (Read / Table Format)
# ------------------------------------------------------------------------------
def view_items():
    """Displays all items in the inventory in a neat table format."""
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<8} | {'Name':<20} | {'Quantity':<10} | {'Price':<10} | {'Total Value':<10}")
    print("-" * 70)
    for item in inventory:
        total_val = format_price(item["quantity"] * item["price"])
        print(f"{item['id']:<8} | {item['name']:<20} | {item['quantity']:<10} | {item['price']:<10} | {total_val:<10}")
    print("=" * 65)


# ------------------------------------------------------------------------------
# 3. UPDATE ITEM (Update)
# ------------------------------------------------------------------------------
def update_item():
    """Updates the quantity or price of an existing item by ID."""
    search_id = input("Enter Item ID to update: ").strip()

    # Search for item in inventory
    target_item = None
    for item in inventory:
        if item["id"].upper() == search_id.upper():
            target_item = item
            break

    if target_item is None:
        print(f"Item ID {search_id} not found.")
        return

    print(f"Current details: ID: {target_item['id']} | {target_item['name']} | Qty: {target_item['quantity']} | Price: {target_item['price']}")

    # Update Quantity
    new_qty_input = input("Enter new quantity (leave blank to keep current): ").strip()
    if new_qty_input != "":
        try:
            new_qty = int(new_qty_input)
            if new_qty < 0:
                print("Invalid quantity. Quantity must be a non-negative whole number. Update cancelled.")
                return
            target_item["quantity"] = new_qty
        except ValueError:
            print("Invalid quantity. Quantity must be a non-negative whole number. Update cancelled.")
            return

    # Update Price
    new_price_input = input("Enter new price (leave blank to keep current): ").strip()
    if new_price_input != "":
        try:
            new_price = float(new_price_input)
            if new_price < 0:
                print("Invalid price. Price must be a non-negative number. Update cancelled.")
                return
            target_item["price"] = format_price(new_price)
        except ValueError:
            print("Invalid price. Please enter a valid number. Update cancelled.")
            return

    print("Item updated successfully.")
    print(f"ID: {target_item['id']} | {target_item['name']} | Qty: {target_item['quantity']} | Price: {target_item['price']}")

    if target_item["quantity"] < 5:
        print(f"Low stock alert: {target_item['name']} ({target_item['quantity']})")


# ------------------------------------------------------------------------------
# 4. DELETE ITEM (Delete)
# ------------------------------------------------------------------------------
def delete_item():
    """Deletes an item from inventory by its ID."""
    search_id = input("Enter Item ID to delete: ").strip()

    for i in range(len(inventory)):
        if inventory[i]["id"].upper() == search_id.upper():
            deleted_name = inventory[i]["name"]
            del inventory[i]
            print(f"Item '{deleted_name}' deleted. Items left: {len(inventory)}")
            return

    print(f"Item ID {search_id} not found.")


# ------------------------------------------------------------------------------
# 5. TOTAL STOCK VALUE
# ------------------------------------------------------------------------------
def show_total_stock_value():
    """Calculates each item's stock value and overall total stock value."""
    if not inventory:
        print("Inventory is empty. Total stock value: 0")
        return

    breakdown = []
    grand_total = 0

    for item in inventory:
        val = item["quantity"] * item["price"]
        grand_total += val
        breakdown.append(f"{item['name']}: {format_price(val)}")

    # Print individual item values separated by '|' as shown in test case 4(a)
    print(" | ".join(breakdown))
    print(f"Total stock value: {format_price(grand_total)}")


# ------------------------------------------------------------------------------
# 6. LOW STOCK REPORT
# ------------------------------------------------------------------------------
def show_low_stock_report():
    """Lists all items having quantity below 5."""
    low_stock_items = []
    for item in inventory:
        if item["quantity"] < 5:
            low_stock_items.append(f"{item['id']} | {item['name']} | Qty: {item['quantity']}")

    if not low_stock_items:
        print("All items have sufficient stock (5 or more).")
    else:
        # Expected format: Low stock (below 5): I102 | Notebook | Qty: 3
        print(f"Low stock (below 5): {', '.join(low_stock_items)}")


# ------------------------------------------------------------------------------
# 7. SEARCH ITEM
# ------------------------------------------------------------------------------
def search_item():
    """Searches for an item by its ID or Name."""
    query = input("Enter Item ID or Name to search: ").strip().lower()
    if not query:
        print("Search term cannot be empty.")
        return

    matches = []
    for item in inventory:
        if query == item["id"].lower() or query in item["name"].lower():
            matches.append(item)

    if not matches:
        print("No matching items found.")
    else:
        print(f"Found {len(matches)} item(s):")
        for item in matches:
            print(f"ID: {item['id']} | {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")


# ------------------------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------------------------
def main():
    """Main menu loop to interact with the inventory system."""
    while True:
        print("\n==============================")
        print("  INVENTORY MANAGEMENT SYSTEM ")
        print("==============================")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Total Stock Value")
        print("6. Low Stock Report")
        print("7. Search Item")
        print("8. Exit")
        print("==============================")

        choice = input("Enter option (1-8): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            show_total_stock_value()
        elif choice == "6":
            show_low_stock_report()
        elif choice == "7":
            search_item()
        elif choice == "8":
            print("Exiting Inventory Management System. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
