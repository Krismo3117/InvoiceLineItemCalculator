def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid price format. Please enter a valid price.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity format. Please enter a valid quantity.")

def calculate_total(quantity, price):
    return quantity * price

def display_invoice_line_item(quantity, price, total):
    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Total: ${total:.2f}")
    print("=" * 20)

print("The Invoice Line Item Calculator")

while True:
    price = get_price()
    quantity = get_quantity()
    total = calculate_total(quantity, price)

    display_invoice_line_item(quantity, price, total)

    another_item = input("Enter another line item? (y/n): ")
    if another_item.lower() != 'y':
        break

