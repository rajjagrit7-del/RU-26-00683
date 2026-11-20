# RUNGTA INTERNATIONAL SKILLS UNIVERSITY
## School of Computer Science and Engineering
### Bachelor of Technology (Computer Science and Engineering)

---

# PROJECT REPORT: INVENTORY MANAGEMENT SYSTEM
**Problem Statement No.:** 9  
**Subject:** Python Programming  
**Student Level:** B.Tech 1st Year  
**Language:** Python 3  

---

## 1. Problem Definition & Objectives

### 1.1 Objective
The objective of this project is to build an interactive, console-based **Inventory Management System** in Python 3. The system allows a store owner or manager to manage stock effectively using fundamental programming concepts: **CRUD operations (Create, Read, Update, Delete)**, **Lists**, **Dictionaries**, and **Functions**.

### 1.2 Key Features
1. **Add Item (Create):** Adds new inventory items with unique auto-generated IDs (`I101`, `I102`, etc.), validated quantity, and price. Automatically alerts if the added item has low stock.
2. **View Items (Read):** Displays all inventory records in a well-formatted table.
3. **Update Item (Update):** Modifies the quantity or price of existing items by Item ID with input validation.
4. **Delete Item (Delete):** Removes an item by its Item ID and reports the remaining item count.
5. **Search Item:** Searches items by Item ID or Item Name.
6. **Total Stock Value:** Calculates individual stock values (`Quantity * Price`) and grand total valuation.
7. **Low Stock Report:** Identifies and reports all items where quantity is below 5.
8. **Input Validation:** Prevents negative quantities, negative prices, and non-numeric entries with clear error messages.

---

## 2. Data Structure Design

As required by the syllabus specifications:
- The complete inventory is stored in a **List of Dictionaries**:
  ```python
  inventory = [
      {"id": "I101", "name": "Pen", "quantity": 50, "price": 10},
      {"id": "I102", "name": "Notebook", "quantity": 3, "price": 40}
  ]
  ```
- **Item ID Generation:** Starting from `I101`, a global counter increments each time a valid item is added.

---

## 3. Function Architecture

| Function Name | Operation | Purpose |
| :--- | :--- | :--- |
| `generate_item_id()` | Utility | Generates sequential IDs starting from `I101` |
| `format_price(val)` | Utility | Formats prices cleanly without awkward `.0` for whole numbers |
| `add_item()` | Create | Takes user inputs, validates, adds item, checks low stock |
| `view_items()` | Read | Formats and prints items as a neat tabular view |
| `update_item()` | Update | Finds item by ID, validates new inputs, and updates fields |
| `delete_item()` | Delete | Finds item by ID, removes it, and prints remaining count |
| `search_item()` | Search | Finds item by ID or name (case-insensitive) |
| `show_total_stock_value()` | Calculation | Displays per-item values and total inventory value |
| `show_low_stock_report()` | Reporting | Lists all items with quantity < 5 |
| `main()` | Menu | Console loop to display menu and handle user choice (1-8) |

---

## 4. Test Cases & Verification

The program was tested against all 4 mandated test cases from the university problem statement:

### Test Case 1: Normal Input
- **Action:** Menu Option 1 (Add)
- **Input:** Name = `Pen`, Quantity = `50`, Price = `10`
- **Output:**
  ```text
  Item added.
  ID: I101 | Pen | Qty: 50 | Price: 10
  ```
- **Status:** PASS

### Test Case 2: Boundary / Minimum Input
- **Action:** Menu Option 1 (Add)
- **Input:** Name = `Eraser`, Quantity = `0`, Price = `5`
- **Output:**
  ```text
  Item added.
  ID: I102 | Eraser | Qty: 0 | Price: 5
  Low stock alert: Eraser (0)
  ```
- **Status:** PASS

### Test Case 3: Invalid Input
- **Action (a):** Add Pencil, Quantity = `-5`, Price = `4`
  - **Output:** `Invalid quantity. Quantity must be a non-negative whole number. Item not added.`
- **Action (b):** Menu Option 3 (Update) with ID `I999`
  - **Output:** `Item ID I999 not found.`
- **Status:** PASS

### Test Case 4: Different Valid Scenario
- **Inventory State:** `I101 Pen (50 x 10)`, `I102 Notebook (3 x 40)`
- **Action (a):** Menu Option 5 (Total stock value)
  - **Output:**
    ```text
    Pen: 500 | Notebook: 120
    Total stock value: 620
    ```
- **Action (b):** Menu Option 6 (Low stock report)
  - **Output:**
    ```text
    Low stock (below 5): I102 | Notebook | Qty: 3
    ```
- **Action (c):** Menu Option 4 (Delete) ID `I101`
  - **Output:**
    ```text
    Item 'Pen' deleted. Items left: 1
    ```
- **Status:** PASS

---

## 5. Viva / Presentation Preparation Guide

Common questions professors ask 1st-year students during viva and how to answer them:

1. **Q: Why did you choose a list of dictionaries?**  
   *A:* A dictionary represents a single item naturally using key-value pairs (`id`, `name`, `quantity`, `price`). A list is an ordered collection that allows us to easily append new items, iterate through them, update records, and delete items using index or `del`.

2. **Q: How does the unique ID generation work?**  
   *A:* We maintain a counter `next_item_id = 101`. Whenever `add_item()` is called, it prefixes `"I"` to the counter (`"I101"`), and increments the counter by 1 (`102`, `103`, etc.).

3. **Q: How do you handle invalid inputs such as negative quantity or letters?**  
   *A:* We use `try...except ValueError` blocks to catch non-numeric inputs and `if quantity < 0:` checks to ensure values are non-negative.

4. **Q: What is the criteria for low stock?**  
   *A:* Any item whose quantity is strictly less than 5 (`quantity < 5`).
