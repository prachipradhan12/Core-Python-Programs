'''
wapp to read sentence and sort every word in sentence
ip=kamal classes thane
op=aaklm acelsss aehnt
'''

s1=input("Enter sentence 1 ")

data=s1.split(' ')

def ana(s):
	l=sorted(s)
	r=''.join(l)
	return r
new_sen=""

for d in data:
	new_sen=new_sen+" "+ana(d)

print("original ",s1)
print("New",new_sen)



