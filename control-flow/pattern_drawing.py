# pattern_drawing.py

try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Please enter a valid integer.")
    exit()

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # move to next line after each row
    row += 1
