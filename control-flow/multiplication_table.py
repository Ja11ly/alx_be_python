# multiplication_table.py

try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
