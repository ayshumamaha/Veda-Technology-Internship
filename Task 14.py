# Shopping Bill Generator
# VEDA Technology - Python Programming Track, Level 1, Task 15

def calculate_bill(items, discount_percent, tax_percent):
    subtotal = sum(item["quantity"] * item["price"] for item in items)
    discount = subtotal * discount_percent / 100
    taxable_amount = subtotal - discount
    tax = taxable_amount * tax_percent / 100
    total = taxable_amount + tax
    return subtotal, discount, tax, total


def main():
    print("=" * 42)
    print("           SHOPPING BILL")
    print("=" * 42)
    items = []

    while True:
        name = input("\nEnter product name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Product name cannot be empty.")
            continue
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (₹): "))
            if quantity <= 0 or price < 0:
                print("Quantity must be positive and price cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole-number quantity and valid price.")
            continue
        items.append({"name": name, "quantity": quantity, "price": price})

    if not items:
        print("\nNo products entered. Bill cancelled.")
        return

    try:
        discount_percent = float(input("\nDiscount percentage (0 if none): "))
        tax_percent = float(input("Tax percentage (0 if none): "))
        if not 0 <= discount_percent <= 100 or tax_percent < 0:
            raise ValueError
    except ValueError:
        print("Invalid discount or tax percentage.")
        return

    subtotal, discount, tax, total = calculate_bill(items, discount_percent, tax_percent)

    print("\n" + "=" * 58)
    print("                     ITEMIZED BILL")
    print("=" * 58)
    print(f"{'Product':<24}{'Qty':>6}{'Price':>12}{'Amount':>14}")
    print("-" * 58)
    for item in items:
        amount = item["quantity"] * item["price"]
        print(f"{item['name'][:23]:<24}{item['quantity']:>6}"
              f"{item['price']:>12.2f}{amount:>14.2f}")

    print("-" * 58)
    print(f"{'Subtotal:':>42} ₹{subtotal:>12.2f}")
    print(f"{f'Discount ({discount_percent:g}%):':>42} ₹{discount:>12.2f}")
    print(f"{f'Tax ({tax_percent:g}%):':>42} ₹{tax:>12.2f}")
    print("=" * 58)
    print(f"{'FINAL AMOUNT:':>42} ₹{total:>12.2f}")
    print("=" * 58)


if __name__ == "__main__":
    main()
