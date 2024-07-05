# multiplication_table.py

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through numbers 1 to 10
for i in range(1, 11):
    # Calculate the product of the user’s number and the iterator
    product = number * i
    # Print each line of the multiplication table
    print(f"{number} * {i} = {product}")

