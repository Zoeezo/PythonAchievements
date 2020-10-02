myList = ['Hoii', True, 10, 5.7, 459, False, 4.6, 'Yikies']

strings = []
integers = []
booleans = []
floats = []

for item in myList:
    if(type(item) == str):
        strings.append(item)
    elif(type(item) == int):
        integers.append(item)
    elif(type(item) == bool):
        booleans.append(item)
    else:
        floats.append(item)

print(myList)
print()
print(strings)
print(integers)
print(booleans)
print(floats)