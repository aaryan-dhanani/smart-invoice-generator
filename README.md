# Smart Invoice Generator System

## Project Overview
A complete Python-based invoice system that allows users to create professional invoices with item details, automatic calculations, and discount code functionality.

## How It Works (Explanation)
The system operates through a menu-driven interface where users can create invoices by entering item names, quantities, and prices. The program automatically calculates line totals (quantity × price), applies optional discount codes, adds 18% GST tax, and generates a professionally formatted invoice. All invoices are stored in memory with unique invoice numbers for easy retrieval and viewing. The core logic uses dictionaries to store item data and performs sequential calculations: subtotal → discount → tax → final total.

## Core Features (Required)
✅ **Item Name Input** - Accept multiple item names  
✅ **Quantity Input** - Accept quantity for each item  
✅ **Price Input** - Accept price per item  
✅ **Total Calculation** - Automatic calculation (quantity × price)  
✅ **Formatted Invoice** - Professional invoice display with all details  

## Custom Feature (Required)
🎯 **DISCOUNT CODE SYSTEM**
- Pre-defined discount codes (SAVE10, SAVE20, FIRST50, STUDENT15)
- Percentage-based discounts (10%, 20%, 50%, 15%)
- Automatic validation and application
- Displays discount amount on invoice
- Codes stored in a dictionary for easy management

## Additional Features (Bonus)
- Invoice numbering system
- Date and time stamp
- Customer name field
- Invoice history storage
- GST (18%) tax calculation
- View previous invoices
- Clean, formatted output

## Technical Details
- **Language:** Python 3
- **Data Structures:** Lists, Dictionaries
- **Key Concepts:** Functions, Loops, Input Validation, String Formatting
- **Lines of Code:** ~280 lines

## How to Run
```bash
python invoice_system.py
```

## Sample Output
```
======================================================================
                           INVOICE
======================================================================
Invoice Number: #1001
Date: 01-02-2026 05:03:35
Customer: Rahul Kumar
======================================================================

Item                           Qty      Price        Total       
----------------------------------------------------------------------
Python Programming Book        2        ₹450.00      ₹900.00     
Wireless Mouse                 1        ₹350.00      ₹350.00     
USB Cable (Type-C)             3        ₹120.00      ₹360.00     
----------------------------------------------------------------------
Subtotal:                                                   ₹1610.00
Discount (STUDENT15):                                       -₹241.50
GST (18%):                                                  ₹246.33
======================================================================
TOTAL AMOUNT:                                               ₹1614.83
======================================================================
```

## Author
Aaryan

## Hackathon
BitBuilders Fun Code Race
