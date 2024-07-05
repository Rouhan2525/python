try:
    num1 = int(input("enter a number :"))
    num2 = int(input("enter another number:"))
    result = num1 / num2
    print(result)
except ValueError:
    print("invalid input.please enter a valid number.")
except ZeroDivisionError:
    print("zero division error")
except Exception as e:
    print("an error occurred:", str(e))