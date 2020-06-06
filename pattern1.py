#wapp to generate
# *
# * *
# * * *
# * * * *

num=int(input("Enter a number "))
if num < 0:
	print("B+ve")
else:
	for i in range(1,num+1):
		print(i*"*\t")
		