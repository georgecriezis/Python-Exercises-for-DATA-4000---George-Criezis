# 1. Prompt for input, strip whitespace, and convert to lowercase
product_name = input("What's the product name? ").strip().lower()

# 2. Use match-case to categorize
match product_name:
    # Logic for Electronics/Tech
    case "electronics" | "gadget":
        category = "High Margin"
    
    # Using a 'guard' (if) to check if it starts with "tech"
    case name if name.startswith("tech"):
        category = "High Margin"
        
    case "clothing" | "apparel":
        category = "Medium Margin"
        
    case "food" | "grocery":
        category = "Low Margin"
        
    # Default case
    case _:
        category = "Uncategorized - Review Needed"

# 3. Print the formatted result
print(f"Product: {product_name} | Category: {category}")