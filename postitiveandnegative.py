#wapp to read array of n integers from user
#and count number of positive integers , number of
#integers and number of 0's

import array
data=array.array('i',[])

n= int(input("Enter the number of elements "))

for i in range(n):
	ele=int(input("Enter the data "))
	data.append(ele)

np=0
nn=0
nz=0
for d in data:
	if( d  >  0):
		np=np+1
	elif(d < 0):
		nn=nn+1
	else:
		nz=nz+1
print("Number of positive elements ",np)
print("Number of negative elements ",nz)
print("Number of 0's ",nz)