'''
wapp to read list of integers from user and print on the screen
'''

num=[]
reply=input("do you want to add integers y/n ")
while reply=='y':
	ele=int(input("enter integer "))
	num.append(ele)
	reply=input("do you want to add more integers y/n ")
print(num)
for n in num:
	print(n,end=' ')
print()
for i in range(len(num)):
	print(num[i],end=' ')
print()