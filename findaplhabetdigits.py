#wapp to read a string and display the no of letters,
#digits and other characters

s1=input("Enter the string ")
lc,dc,oc= 0,0,0 

for s in s1:	
	if (s.isalpha()):
		lc=lc+1
	elif (s.isdigit()):
		dc=dc+1
	else:
		oc=oc+1
print("letters=",lc,"digit=",dc,"others=",oc)