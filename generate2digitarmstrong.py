'''
using function generate all 3 digit ARMSTRONG number
'''

def check(num):
	org_num=num
	sum=0
	while num>0:
		digit=num%10
		sum=sum+digit**3  #if 4 digit armstrong is required then **4 n so on
		num=num//10
	if(sum==org_num):
		return True
	else:
		return False
for i in range(100,1000):
	if check(i):
		print("Armstrong no :",i)
		