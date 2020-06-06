'''
wapp to read list of marks and find the highest and the lowest marks
'''

marks=[]
reply=input("do you want to add marks y/n ")
while reply=='y':
	ele=int(input("enter marks "))
	marks.append(ele)
	reply=input("do you want to add more integers y/n ")

marks.sort()
lowest=marks[0]
highest=marks[-1]
print("Highest=",highest)
print("Lowest=",lowest)