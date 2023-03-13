dividend = int(input("What is the Dividend?: "))
divisor = int(input("What is the Divisor?: "))

remaider = dividend % divisor
fakeDivisor = divisor
quo = 0
while fakeDivisor < dividend:
    quo += 1
    fakeDivisor = fakeDivisor * quo
quo-=1

print("\t", quo," r ", remaider)
print("\t ________")
print("\t5|", dividend)
print("\t  ", divisor*quo)
print("\t   ___")
print("\t   ", dividend-(divisor*quo))