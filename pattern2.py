#wapp to generate
# A
# B B
# C C C
# D D D D

num=int(input("Enter a number "))
if num < 0:
	print("B+ve")
else:
	ch=65
	for i in range(1,num+1):
		print(i * (chr(ch)+"\t"))
		ch=ch+1
		