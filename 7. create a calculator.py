print("1. addition ")
print("2. subtraction ")
print("3. multiplication ")
print("4. division")

choice =int(input("enter your choice : "))
num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))

if choice == 1:
    print("sum  =",num1 + num2)
elif choice == 2:
    print("subtraction =",num1 - num2)
elif choice == 3:
    print(" multiplication =",num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("division =",num1 / num2)
    else:
        print("error division by zero")
else:
    print("invalid choice")