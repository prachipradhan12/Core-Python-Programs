'''
wapp to count occurences of each letters in the given ip string
'''



name=input("Enter a string ")

string={}
for s in name:
	ans=string.get(s,-1)
	if ans==-1:	
		string[s]=1
	else:
		string[s]=ans+1
print(string)