def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # Return original price if discount is less than 20%

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"Final price after discount: ${final_price:.2f}")