#wapp to read two int and exchange their values with third variable

n1=int(input("Enter first no "))
n2=int(input("Enter second no "))

temp=n1
n1=n2
n2=temp

print("1st no", n1)
print("2nd no", n2)
