#wapp to find the sum of first n integers
#5 1+2+3+4+5=15

num=int(input("Enter an integer "))
if num<0:
	print("B +ve")
else:
	sum=0
	i=1
	while i<=num:
		sum=sum+i
		i=i+1
print("Sum=",sum)
