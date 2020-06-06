'''
wamdp to maintain the runs scored by the players
1.add
2.view
3.update
4.delete
5.exit
'''

data={ }

while True:
	op=int(input("1.add 2.view 3.update 4.delete 5.exit "))
	if op==1:
		name=input("Enter player name ")
		if data.get(name,-1)==-1:	
			runs=int(input("enter runs scored "))
			data[name]=runs
			print(name," added")
		else:
			print(name, "already exist")
	elif op==2:
		for n in data:
			print("name ",n,"runs",data[n])
	elif op==3:
		name=input("Enter player name to update ")
		if data.get(name,-1)==-1:	
			print("Player doesn't exist")			
		else:
			runs=int(input("enter updated scored "))
			data[name]=runs
			print(runs," updated")
	elif op==4:
		name=input("Enter player name to delete ")
		if data.get(name,-1)==-1:	
			print("Player doesn't exist")			
		else:
			data.pop(name)
			print(name," deleted")
		
	elif op==5:
		break
	else:
		print("Invalid option")