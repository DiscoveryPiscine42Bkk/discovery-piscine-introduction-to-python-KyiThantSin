num = input("Enter a number less than 25: ")

try:
    num = int(num)
    if num >= 25:
        print("Error")
    else:
        while num <= 25:
            print("Inside the loop, my variable is:", num)
            num += 1
except ValueError:
    print("Please enter a valid number")
