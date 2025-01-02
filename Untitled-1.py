# Printing out a friendly heading for the vending machine
print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▄▀█ █▀▄▀█ █▄▄ █▀█ █▀▀ █▀▀ █▄░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀█ █░▀░█ █▄█ █▀▄ ██▄ ██▄ █░▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█

                                    █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
                                    █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")
"""Assigning code values to specif menu items which are divided into categories using dictionaries."""

Inventory = {
    "Crisps": {
        "C1": {"item": "Takis", "Price": 5.50, "Stock": 13},
        "C2": {"item": "Doritos", "Price": 2.50, "Stock": 11},
        "C3": {"item": "Sun Crisps", "Price": 4.00, "Stock": 3},
        "C4": {"item": "Pringles", "Price": 7.00, "Stock": 9},
        "C5": {"item": "Cheetos", "Price": 3.00, "Stock": 5},
    },
    "Chocolates": {
        "CH1": {"item": "Galaxy Flutes", "Price": 3.00, "Stock": 10},
        "CH2": {"item": "Cadbury", "Price": 1.50, "Stock": 8},
        "CH3": {"item": "Kinder Bueno", "Price": 4.50, "Stock": 3},
        "CH4": {"item": "Choki Choki", "Price": 2.00, "Stock": 11},
        "CH5": {"item": "KitKat", "Price": 1.50, "Stock": 13},
    },
    "Biscuits": {
        "B1": {"item": "CoCo Mo", "Price": 1.50, "Stock": 11},
        "B2": {"item": "Oreo", "Price": 3.00, "Stock": 9},
        "B3": {"item": "Loacker", "Price": 5.50, "Stock": 13},
        "B4": {"item": "Hide & Seek", "Price": 3.00, "Stock": 3},
        "B5": {"item": "Granola Bar", "Price": 5.00, "Stock": 12},
    },
    "Drinks": {
        "D1": {"item": "Coca Cola", "Price": 2.50, "Stock": 7},
        "D2": {"item": "Pepsi", "Price": 2.50, "Stock": 12},
        "D3": {"item": "Redbull", "Price": 8.00, "Stock": 6},
        "D4": {"item": "Orange Juice", "Price": 1.50, "Stock": 1},
        "D5": {"item": "Ice Coffee", "Price": 5.50, "Stock": 11},
    }
}

#Function to display the vending machine menu items
def display_menu():
    print("\n-*- Vending Machine Menu -*-")
    for category, items in Inventory.items():
        print(f"\nCategory: {category}")
        print(f"{'Code':<6}{'Item':<20}{'Price':<8}{'Stock':<6}")
        print("-" * 40)
        for code, details in items.items():
            print(f"{code:<6}{details['item']:<20}${details['Price']:<8.2f}{details['Stock']:<6}")
display_menu()  # Show the menu initially
#Funtion to validate if the code enetered by user is valid
def validate_code_inventory(code):
    for category, items in Inventory.items():
        if code in items:
            return True, category
    return False, None

#Function to get the user input for product code
def get_product_code():
    while True:
        code = input("Enter a product code (or type EXIT to quit): ").upper()
        if code == "EXIT":
            return None, None
        valid, category = validate_code_inventory(code)
        if valid:
            return code, category
        else:
            print("Invalid code. Please try again.")
#Function to check and track the stock 
def process_stock(code):
    for category, items in Inventory.items():
        if code in items and items[code]['Stock'] > 0:
            items[code]['Stock'] -= 1
            return items[code]
    print("Item out of stock or invalid code.")
    return None
#Function to carry out the payment process 
def process_payment(total_price):
    while True:
        try:
            amount = float(input(f"Insert payment for ${total_price:.2f}: $"))
            if amount >= total_price:
                return amount - total_price
            else:
                print("Insufficient amount. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
#Function to suggest the user to buy a product based on their previous purchase
def suggest_pairing(category):
    pairings = {
        "Crisps": "Drinks",
        "Chocolates": "Crisps",
        "Biscuits": "Drinks",
        "Drinks": "Crisps"
    }
    paired_category = pairings.get(category)
    if not paired_category:
        print("No pairings available for this item.")
        return {}

    print(f"\nSuggested pairings from {paired_category}:")
    paired_items = Inventory[paired_category]
    for code, details in paired_items.items():
        print(f"{code}: {details['item']} - ${details['Price']:.2f}")
    return paired_items
#Function to check if the paired items code is valid
def validate_pairing_code(pairings):
    while True:
        pairing_code = input("Enter the code of the pairing item: ").upper()
        if pairing_code in pairings and pairings[pairing_code]['Stock'] > 0:
            return pairing_code
        print("Invalid pairing code. Please try again.")
#Function to print the summary of the purchase
def print_receipt(items):
    print("\n--- Receipt ---")
    total = 0
    for item in items:
        print(f"{item['item']} - ${item['Price']:.2f}")
        total += item['Price']
    print(f"Total: ${total:.2f}")
    print("Thank you for using the vending machine!")
#Main function of the vending machine
def vending_machine():
    items_purchased = []  # List to store items purchased

    while True:
        code, category = get_product_code()  # Get product code from user
        if not code:  # If user types EXIT, break the loop
            break

        item = process_stock(code)  # Process the item
        if item:
            print(f"{item['item']} added to your cart for ${item['Price']:.2f}")
            total_price = item['Price']  # Set initial total price to the selected item

            pairings = suggest_pairing(category)  # Suggest pairings
            if pairings:
                use_change = input("Do you want to buy a pairing item? (y/n): ").lower()
                if use_change == 'y':
                    pairing_code = validate_pairing_code(pairings)  # Get valid pairing item code
                    pairing_item = process_stock(pairing_code)
                    if pairing_item:
                        print(f"{pairing_item['item']} added to your cart for ${pairing_item['Price']:.2f}")
                        total_price += pairing_item['Price']
                        items_purchased.append(pairing_item)

            change = process_payment(total_price)  # Process payment
            print(f"Payment accepted. Change: ${change:.2f}")
            items_purchased.append(item)  # Add selected item to purchased list
            print_receipt(items_purchased)  # Print the receipt
            print("Have a nice day!")  # Display closing message
            break  # Exit after printing receipt and message

if __name__ == "__main__":
    vending_machine()
