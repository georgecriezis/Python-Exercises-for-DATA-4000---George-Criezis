# Ask what my annual income is (float)
income = float(input("What's your annual income? "))


# Define a function get_tax_bracket (income) that takes income  (float) and returns the bracket as str
def get_tax_bracket(income):
    if income < 50000:
        bracket =  "Low (10%)"
        rate = 0.10
    elif 50000 <= income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    elif income >= 100000:
        bracket = "High (30%)"
        rate = 0.30
    elif income < 0:
        return "Invalid income"
    
    return bracket, rate

# Call the function and print the result
bracket, rate = get_tax_bracket(income)
print(f"Your tax bracket is: {bracket}. Estimated tax: {rate*100}%.")