def search(list,n):
    for i in range(len(list)):
        if list[i] == n: 
            return True
    return False
list = [1,2,10,4,50,6]
n = int(input("enter the key to be search="))
if search(list,n):
    print("the given number is found")
else:
    print("the given number is not found")