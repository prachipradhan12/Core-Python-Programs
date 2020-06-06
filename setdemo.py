'''
wapp to read two set of student names
1.android batch students
2.java batch students
Display the following:
1.all names
2.common names
'''

abatch=set()
jbatch=set()

reply=input("do you want to add android student names y/n ")
while reply=='y':
	ele=input("enter names ")
	abatch.add(ele)
	reply=input("do you want to add more android student names y/n ")


reply=input("do you want to add java student names y/n ")
while reply=='y':
	ele=input("enter names ")
	jbatch.add(ele)
	reply=input("do you want to add more java student names y/n ")
r1= abatch|jbatch
print("All students :",r1)
r2= abatch&jbatch
print("common students :",r2)



