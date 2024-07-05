import math
a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print ("the equation has two real roots :", root1,"and" ,root2)
elif discriminant == 0:
    root = - b / (2 * a)
    print("the equation has one real root :", root)
else:
        print("does not have a real root ")
    