'''
wapp to find factorial(recursive)

'''


def fact(n):
	if n==1:
		return 1
	
	else:
		return n*fact(n-1)
num=int(input("Enter a number "))
if num<0:
	print("b -ve")
elif num ==0 or num==1:
	print("Fact=1")
else:
	res=fact(num)
	print("fact=",res)