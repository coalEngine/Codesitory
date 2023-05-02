 
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
a = int(input("Number?: "))
b = int(input("Number?: "))
print("The GCF is : ", end="")
print(hcfnaive(a, b))