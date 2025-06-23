num = input("Please enter a number: ")
    
if num.isdigit():
    num = int(num)
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
else:
    print("Please enter a valid number.")