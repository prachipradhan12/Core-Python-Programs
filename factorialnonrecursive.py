'''
wapp to find factorial(non recursive)

'''


def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	else:
		return f
num=int(input("Enter a number "))
if num<0:
	print("b -ve")
elif num ==0 or num==1:
	print("Fact=1")
else:
	res=fact(num)
	print("fact=",res)