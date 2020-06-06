#wapp to generate
# * * * *
# * * *
# * * 
# * 

num=int(input("Enter a number "))
if num < 0:
	print("B+ve")
else:
	for i in range(num,0,-1):
		print(i*"*\t")
		