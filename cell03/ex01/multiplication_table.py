num = input("Enter a number: ")

try:
    num = int(num)
    for i in range(10):
        print(i, "x", num, "=", i*num)
except ValueError:
    print("Please enter a valid number.")
