import array

data=array.array('i',[])
n=int(input("Enter number of elements "))
for i in range(n):
	ele=int(input("Enter the data "))
	data.append(ele)
while True:
	op=int(input("1 data, 2 data in asc ,3 data in desc ,4 exit"))
	if op==1:
		for d in data:
			print(d,end='')
		print()
	elif op==2:
  		adata=sorted(data)
		for i in adata:
			print(i,end='')
		print()
	elif op==3:
		ddata=sorted(data,reverse=True)
		for i in ddata:
			print(i,end='')
		print()
	elif op==4:
		break:
	else:
		print("Invalid option:")