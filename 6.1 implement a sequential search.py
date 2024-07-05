found = 0
list = [1,2,10,4,50,6]
n = int(input("enter the key to be search ="))
for i in range(len(list)):
    if list[i] == n:
        found = 1
if found == 1:
    print("the given number is found")
else:
    print("the given number is not found")