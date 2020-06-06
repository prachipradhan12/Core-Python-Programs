'''
wapp to read tuple of integers from the user and display in descending order
'''

list_data=[]
tup_data=[]

reply=input("do you want to add integers y/n ")
while reply=='y':
	ele=input("enter integers ")
	list_data.append(ele)
	reply=input("do you want to add more integers y/n ")

tup_data=tuple(list_data)
print("Before: ",tup_data)
list_data.sort(reverse=True)
tup_data=tuple(list_data)
print("After: ",tup_data)
