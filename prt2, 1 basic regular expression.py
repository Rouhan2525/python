import re
text = input("enter the text=")
pattern = input("enter the pattern to be search=")
match = re.search(pattern, text)
if match:
    print("match found")
else:
    print("no match found")
