# ===================================================================
# BITBUILDERS FUN CODE RACE - INVOICE SYSTEM
# ===================================================================
# Project: Smart Invoice Generator
# Language: Python
# Author: [Your Name]
# Description: A complete invoice system with discount code feature
# ===================================================================

import datetime

# Store for invoice history
invoice_history = []
invoice_counter = 1001  # Starting invoice number

# Custom Feature: Discount codes dictionary
DISCOUNT_CODES = {
    "SAVE10": 10,      # 10% discount
    "SAVE20": 20,      # 20% discount
    "FIRST50": 50,     # 50% discount for first-time customers
    "STUDENT15": 15    # 15% discount for students
}

def display_header():
    """Display the main menu header"""
    print("\n" + "="*60)
    print("          SMART INVOICE GENERATOR SYSTEM")
    print("="*60)

def create_invoice():
    """Main function to create a new invoice"""
    global invoice_counter
    
    print("\n--- CREATE NEW INVOICE ---")
    
    # Customer details
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        customer_name = "Walk-in Customer"
    
    # Items list
    items = []
    
    print("\nEnter item details (press Enter on item name when done):")
    
    while True:
        print(f"\n--- Item #{len(items) + 1} ---")
        item_name = input("Item name: ").strip()
        
        # Exit condition
        if not item_name:
            if len(items) == 0:
                print("⚠ You must add at least one item!")
                continue
            else:
                break
        
        # Get quantity
        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("⚠ Quantity must be positive!")
                    continue
                break
            except ValueError:
                print("⚠ Please enter a valid number!")
        
        # Get price per item
        while True:
            try:
                price = float(input("Price per item (₹): "))
                if price <= 0:
                    print("⚠ Price must be positive!")
                    continue
                break
            except ValueError:
                print("⚠ Please enter a valid price!")
        
        # Calculate line total
        line_total = quantity * price
        
        # Add item to list
        items.append({
            "name": item_name,
            "quantity": quantity,
            "price": price,
            "total": line_total
        })
        
        print(f"✓ Added: {item_name} x{quantity} = ₹{line_total:.2f}")
    
    # Calculate subtotal
    subtotal = sum(item["total"] for item in items)
    
    # CUSTOM FEATURE: Apply discount code
    discount_amount = 0
    discount_code = ""
    
    print("\n--- DISCOUNT CODE (Optional) ---")
    print("Available codes: SAVE10, SAVE20, FIRST50, STUDENT15")
    code_input = input("Enter discount code (or press Enter to skip): ").strip().upper()
    
    if code_input in DISCOUNT_CODES:
        discount_percent = DISCOUNT_CODES[code_input]
        discount_amount = subtotal * (discount_percent / 100)
        discount_code = code_input
        print(f"✓ Discount applied: {discount_percent}% off!")
    elif code_input:
        print("⚠ Invalid discount code. Proceeding without discount.")
    
    # Calculate tax (18% GST)
    tax_rate = 18
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * (tax_rate / 100)
    
    # Calculate final total
    final_total = taxable_amount + tax_amount
    
    # Generate invoice
    invoice_data = {
        "invoice_number": invoice_counter,
        "customer_name": customer_name,
        "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "items": items,
        "subtotal": subtotal,
        "discount_code": discount_code,
        "discount_amount": discount_amount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "final_total": final_total
    }
    
    # Save to history
    invoice_history.append(invoice_data)
    
    # Display invoice
    display_invoice(invoice_data)
    
    # Increment invoice counter
    invoice_counter += 1
    
    return invoice_data

def display_invoice(invoice_data):
    """Display a formatted invoice"""
    print("\n" + "="*70)
    print("                           INVOICE")
    print("="*70)
    print(f"Invoice Number: #{invoice_data['invoice_number']}")
    print(f"Date: {invoice_data['date']}")
    print(f"Customer: {invoice_data['customer_name']}")
    print("="*70)
    
    # Table header
    print(f"\n{'Item':<30} {'Qty':<8} {'Price':<12} {'Total':<12}")
    print("-"*70)
    
    # Items
    for item in invoice_data['items']:
        print(f"{item['name']:<30} {item['quantity']:<8} "
              f"₹{item['price']:<11.2f} ₹{item['total']:<11.2f}")
    
    print("-"*70)
    
    # Subtotal
    print(f"{'Subtotal:':<59} ₹{invoice_data['subtotal']:.2f}")
    
    # Discount (if applied)
    if invoice_data['discount_amount'] > 0:
        print(f"{'Discount (' + invoice_data['discount_code'] + '):':<59} "
              f"-₹{invoice_data['discount_amount']:.2f}")
    
    # Tax
    print(f"{'GST (' + str(invoice_data['tax_rate']) + '%):':<59} "
          f"₹{invoice_data['tax_amount']:.2f}")
    
    print("="*70)
    
    # Final total
    print(f"{'TOTAL AMOUNT:':<59} ₹{invoice_data['final_total']:.2f}")
    print("="*70)
    
    print("\n           Thank you for your business!")
    print("="*70)

def view_invoice_history():
    """View all previous invoices"""
    if len(invoice_history) == 0:
        print("\n⚠ No invoices found in history.")
        return
    
    print("\n--- INVOICE HISTORY ---")
    print(f"\n{'Invoice #':<12} {'Date':<20} {'Customer':<25} {'Amount':<12}")
    print("-"*75)
    
    for inv in invoice_history:
        print(f"#{inv['invoice_number']:<11} {inv['date']:<20} "
              f"{inv['customer_name']:<25} ₹{inv['final_total']:<11.2f}")
    
    # Option to view full invoice
    print("\n" + "-"*75)
    view_detail = input("Enter invoice number to view details (or press Enter): ").strip()
    
    if view_detail:
        try:
            inv_num = int(view_detail)
            for inv in invoice_history:
                if inv['invoice_number'] == inv_num:
                    display_invoice(inv)
                    return
            print("⚠ Invoice not found!")
        except ValueError:
            print("⚠ Invalid invoice number!")

def show_discount_codes():
    """Display available discount codes"""
    print("\n--- AVAILABLE DISCOUNT CODES ---")
    print("-"*50)
    for code, percent in DISCOUNT_CODES.items():
        print(f"{code:<15} - {percent}% off")
    print("-"*50)

def main():
    """Main program loop"""
    print("\n🎉 Welcome to Smart Invoice Generator System!")
    
    while True:
        display_header()
        print("1. Create New Invoice")
        print("2. View Invoice History")
        print("3. View Discount Codes")
        print("4. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            create_invoice()
        
        elif choice == "2":
            view_invoice_history()
        
        elif choice == "3":
            show_discount_codes()
        
        elif choice == "4":
            print("\n" + "="*60)
            print("  Thank you for using Smart Invoice Generator!")
            print("  Have a great day! 👋")
            print("="*60 + "\n")
            break
        
        else:
            print("\n⚠ Invalid choice! Please select 1-4.")
        
        # Pause before next iteration
        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
