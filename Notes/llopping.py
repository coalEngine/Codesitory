chars = ['A', 'B', 'C']
fruit = ['Apple', 'Banana', 'Cherry']
dict = {"name": 'Mike', 'ref': "Python", 'sys': 'Win'}

print("\nElements:\t", end='')
for element in chars:
    print(element, end='')

print("\nEnumerated:\t", end='')
for element in enumerate(chars):
    print(element, end='')

print("\nZipped:\t", end='')
for element in zip(chars, fruit):
    print(element, end='')

print("\nPaired: ")
for key, val in dict.items():
    print(key, '=', val)