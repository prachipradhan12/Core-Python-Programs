#wapp to read the n marks form user and find the following
#1) avg marks 2) highest marks 3)lowest marks
#4) count nos >=70  5) count nos <=40



import array

marks= array.array('i',[])

num=int(input("Enter number of students "))
for i in range(num):
	m=int(input("Enter marks "))
	marks.append(m)

sum=0
for m in marks:
	sum=sum+m
avg=sum/num
print("Average ",avg)

high=low=marks[0]
for m in marks:
	if  m>high:
		high=m
	if m<low:
		low=m
print("Highest marks ",high)
print("Lowest marks ",low)
count=0
count1=0
for m in marks:
	if m >=70:
		count+=1
	if m<=40:
		count1+=1
print(">=70",count)
print("<=30",count1)






	