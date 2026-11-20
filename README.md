# Inventory Management System (Python 3)

**Course:** B.Tech Computer Science and Engineering (1st Year)  
**Problem Statement No.:** 9  
**Institution:** Rungta International Skills University  

A console-based Inventory Management System built in Python 3 using Lists, Dictionaries, and Functions following CRUD principles.

## Features
- **Add Item:** Unique ID starting from `I101`, input validation, automatic low-stock notification.
- **View All Items:** Neatly formatted table displaying ID, Name, Quantity, Price, and Total Value.
- **Update Item:** Modify quantity and price safely by Item ID.
- **Delete Item:** Remove item and display remaining item count.
- **Search Item:** Find items by ID or Name (case-insensitive).
- **Total Stock Value:** Item-wise valuation breakdown and grand total stock calculation.
- **Low Stock Report:** Automatic detection of any item with quantity below 5.

## Project Structure
```text
inventory_management_system/
│
├── inventory_system.py   # Main executable Python program
├── PROJECT_REPORT.md     # Full college project documentation
└── README.md             # GitHub repository overview
```

## How to Run
1. Make sure Python 3 is installed.
2. Open terminal/command prompt in this folder.
3. Run:
   ```bash
   python inventory_system.py
   ```

## Test Cases Covered
- **Test Case 1:** Normal Input (Adding Pen, 50 Qty, Price 10 -> ID I101)
- **Test Case 2:** Minimum/Boundary Input (Adding Eraser, 0 Qty, Price 5 -> ID I102 with Low Stock alert)
- **Test Case 3:** Invalid Input handling (Negative quantity -5, non-existent ID I999 update)
- **Test Case 4:** Multi-item scenario (Valuation calculation, Low stock report for items < 5, Deletion with remaining count)
