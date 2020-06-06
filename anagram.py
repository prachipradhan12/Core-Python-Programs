'''
wapp to read two strings from the user and check if they are anagrams
s1=listen	s2=silent
with function()
'''
def ana(s):
	l=sorted(s)
	r=''.join(l)
	return r


s1=input("Enter String 1 ")
s2=input("Enter String 2 ")
a=ana(s1)
b=ana(s2)

if a==b:
	print("Anagram")
else:
	print("No")
