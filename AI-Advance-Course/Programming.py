# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Main program
if __name__ == "__main__":
    try:
        # Take user input
        user_input = int(input("Enter a number: "))
        
        # Check if the number is even or odd
        result = check_even_odd(user_input)
        
        # Print the result
        print(f"The number {user_input} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
