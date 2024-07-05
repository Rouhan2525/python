import re
pattern = r'^[A-Za-z] + {2}$'
data = 'Abc12'
if re.match(pattern, data):
    print("valid data")
else:
    print("invalid data")