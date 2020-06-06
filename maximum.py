#wapp to read int and find the max


a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
c=int(input("Enter 3rd no "))

if (a>b):
        max=a 
else:
	max=b
if (c>max):
	max=c
print("Maximum=",max)