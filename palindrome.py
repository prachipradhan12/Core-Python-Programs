'''
wapp to read a string t check if its palindrome
'''

s1=input("Enter the string ")
s1=s1.lower() # if u want case sensitive
r1=s1[::-1]
if s1==r1:
	print("Palindrome")
else:
	print("nope ")	