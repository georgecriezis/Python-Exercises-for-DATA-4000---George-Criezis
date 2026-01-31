def format_greeting(name, title="Customer"):
    # remove leading and trailing whitespace
    clean_name = name.strip()
    
    # Handle the empty name case
    if not clean_name:
        return "Hello, Valued Customer!"
    
    # .title() capitalizes the first letter of every word (e.g., "john doe" -> "John Doe")
    titled_name = clean_name.title()
    
    # break the string into a list based on spaces
    # take the first element [0] to get just the first name
    first_name = titled_name.split()[0]
    
    # Return the f-string formatted
    return f"Hello, {first_name} ({title})!"

def main():
    # Prompt the user for their name
    user_input = input("What's your full name? ")
    
    # Call the function and print the result
    # You can also pass a second argument here to test the custom title extension
    greeting = format_greeting(user_input)
    print(greeting)

if __name__ == "__main__":
    main()