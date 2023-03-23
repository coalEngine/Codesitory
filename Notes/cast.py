a = input("Enter a number: ")
b = input("Enter another number: ")

sum = a + b
print("Data Type sum :", sum, type(sum))
sum = int(a) + int(b)
print("Data Type sum :", sum, type(sum))
sum = float(a) + float(b)
print("Data Type sum :", sum, type(sum))
sum = chr(int(sum))
print("Data type sum :", sum, type(sum))