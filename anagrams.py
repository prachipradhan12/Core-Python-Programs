'''
wapp to read two strings from the user and check if they are anagrams
s1=listen	s2=silent
'''


s1=input("Enter String 1 ")
s2=input("Enter String 2 ")

l1=sorted(s1)
ns1=''.join(l1)
l2=sorted(s2)
ns2=''.join(l2)


if ns1==ns2:
	print("Anagram")
else:
	print("No")
