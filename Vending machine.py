print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▄▀█ █▀▄▀█ █▄▄ █▀█ █▀▀ █▀▀ █▄░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀█ █░▀░█ █▄█ █▀▄ ██▄ ██▄ █░▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█

                                    █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
                                    █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""") 

# Defining a Dictionary for inventory
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

# Function to display the menu
def display_menu():
    print("\n-*- Vending Machine Menu -*-")
    for category, items in Inventory.items():
        print(f"\nCategory: {category}")
        print(f"{'Code':<6}{'Item':<20}{'Price':<8}{'Stock':<6}")
        print("-" * 40)
        for code, details in items.items():
            print(f"{code:<6}{details['item']:<20}${details['Price']:<8.2f}{details['Stock']:<6}")

# Function to validate code
def Code_validation(code):
    for category, items in Inventory.items():
        if code in items:
            return True, category
    return False, None

# Function to get a valid code from the user
def Inventory_code():
    while True:
        code = input("Enter a product code (or type EXIT to quit): ").upper()
        if code == "EXIT":
            return code, None
        is_valid, category = Code_validation(code)
        if is_valid:
            return code, category
        else:
            print("Invalid code, Please enter a valid code.")

# Function for payment and change making
def user_payment(Price):
    print(f"\nPayment Amount: ${Price:.2f}")
    while True:
        try:
            amount = float(input("Insert the payment amount: $"))
            if amount >= Price:
                change = amount - Price
                print(f"\nPayment accepted, Here is your change: ${change:.2f}")
                return change
            else:
                print("\nInsufficient payment, Try again.")
        except ValueError:
            print("\nInvalid Payment, Enter a valid amount.")

# Function for stock management and deduction
def stock_Inventory(code):
    for category, items in Inventory.items():
        if code in items:
            if items[code]["Stock"] > 0:
                items[code]["Stock"] -= 1
                return items[code]
            else:
                print("\nSorry, item is out of stock :-(")
                return None
    print("\nInvalid code, Try again.")
    return None

# Function for suggested pairings
def suggested_pairing(items, code):
    if code in items["Crisps"]:
        paired_category = "Drinks"
    elif code in items["Chocolates"]:
        paired_category = "Crisps"
    elif code in items["Biscuits"]:
        paired_category = "Drinks"
    elif code in items["Drinks"]:
        paired_category = "Crisps"
    else:
        return []  # No pairings available

    pairing_items = []
    for pair_code, details in items[paired_category].items():
        pairing_items.append((pair_code, details['item'], details['Price']))
    
    return pairing_items

# Function to print a receipt
def print_receipt(Items_purchased):
    print("\n--- Receipt ---")
    total = 0
    for item in Items_purchased:
        print(f"{item['item']} - ${item['Price']:.2f}")
        total += item["Price"]
    print(f"\nTotal: ${total:.2f}")
    print("Thank you for using the vending machine!")

# Main function
def main_function():
    display_menu()
    Items_purchased = []
    remaining_balance = 0
    bought_pairing = False

    while True:
        code, category = Inventory_code()
        if code == "EXIT":
            break
        item = stock_Inventory(code)
        if item:
            if remaining_balance > 0 and not bought_pairing:
                print(f"You have ${remaining_balance:.2f} remaining from your previous purchase.")
                buy_pair = input(f"Do you want to buy a pairing with the remaining balance? (y/n): ").lower()
                if buy_pair == 'y':
                    pairings = suggested_pairing(Inventory, category)
                    if not pairings:
                        print("No pairings available for this item.")
                    else:
                        print(f"You can choose from the following pairing items:")
                        for pair_code, item_name, price in pairings:
                            print(f"{pair_code}: {item_name} - ${price:.2f}")
                        
                        pair_code = input("Enter the code of the item you want to buy from the pairing options: ").upper()
                        pair_item = stock_Inventory(pair_code)
                        if pair_item:
                            if remaining_balance >= pair_item["Price"]:
                                remaining_balance -= pair_item["Price"]
                                Items_purchased.append(pair_item)
                                bought_pairing = True
                            else:
                                print(f"You don't have enough balance to purchase {pair_item['item']}.")
                        else:
                            print("Invalid code for pairing item.")
                else:
                    bought_pairing = True  # No pairing purchase, allow normal flow

            if remaining_balance == 0 or bought_pairing:
                change = user_payment(item["Price"])
                remaining_balance += change
                Items_purchased.append(item)
                bought_pairing = False
                pairings = suggested_pairing(Inventory, category)
                if pairings:
                    print(f"You might also enjoy these pairing items:")
                    for pair_code, item_name, price in pairings:
                        print(f"{pair_code}: {item_name} - ${price:.2f}")
                else:
                    print("No pairings available for this item.")

        else:
            print("Invalid code, please try again.")

    if Items_purchased:
        print_receipt(Items_purchased)

if __name__ == "__main__":
    main_function()
