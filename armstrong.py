'''
wapf that takes as input integer and returns True if the number is Armstrong number else returns false
'''

def check(num):
	org_num=num
	sum=0
	while num>0:
		digit=num%10
		sum=sum+digit**3
		num=num//10
	if(sum==org_num):
		return True
	else:
		return False

n=int(input("Enter a number "))

if n<0:
	print("b +ve")
else:
	if check(n):
		print("Yeshhhh")
	else:
		print("No")
