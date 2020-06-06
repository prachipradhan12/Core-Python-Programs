#wapp to find the sum of digits
#ip 354 op 12 

num=int(input("Enter an integer "))
if num<0:
	print("B +ve")
else:
	sum=0
	while num>0:
		dig=num%10
		sum=sum+dig
		num=num//10
print("Sum=",sum)
