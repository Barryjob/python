def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    
    :param price: The original price of the item.
    :param discount_percent: The discount percentage to be applied.
    :return: The final price after discount or the original price.
    """
    
    # Check if the discount percent is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Example usage:
original_price = 100
discount = 25
final_price = calculate_discount(original_price, discount)
print(f"Final price after discount: ${final_price:.2f}")  # Output: Final price after discount: $75.00


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    
    :param price: The original price of the item.
    :param discount_percent: The discount percentage to be applied.
    :return: The final price after discount or the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Enhanced user input with validation
while True:
    try:
        original_price = float(input("Enter the original price of the item: $"))
        if original_price < 0:
            print("The price cannot be negative. Please enter a valid price.")
            continue
        
        discount = float(input("Enter the discount percentage: "))
        if discount < 0:
            print("The discount percentage cannot be negative. Please enter a valid percentage.")
            continue
        
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Calculate the final price
final_price = calculate_discount(original_price, discount)

# Print the result
if final_price != original_price:
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price remains: ${original_price:.2f}")