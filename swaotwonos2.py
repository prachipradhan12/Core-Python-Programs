#wapp to read two int and exchange their values without third variable

n1=int(input("Enter first no "))
n2=int(input("Enter second no "))

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("After swapping")
print("1st no", n1)
print("2nd no", n2)
