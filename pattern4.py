#wapp to generate
# a a a a
# b b b
# c c
# d 

num=int(input("Enter a number "))
if num < 0:
	print("B+ve")
else:
	ch=97
	for i in range(num,0,-1):
		print(i * (chr(ch)+"\t")) # + performs  concatenation & * performs repeatition
		ch=ch+1
		