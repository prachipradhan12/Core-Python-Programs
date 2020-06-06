#wapp to find the factorial of a no
#i/p:5 o/p:1*2*3*4*5=120


num=int(input("Enter a number "))
if num < 0:
	print("B+ve")
elif num==0 or num==1:
	print("ans=",1)
else:
	fact=1
	for i in range(1,num+1,1):
		fact=fact*i
	else:
		print("ans=",fact)