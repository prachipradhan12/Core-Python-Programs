'''
wadpp for billing generation
'''

menu={'idli':20,'burger':50,'Margritta':400,'pasta':350}
amount=0.0
while True:
	op=int(input("1. add 2. amount and 3.exit "))
	if op==1:
		food=input("Enter name of food item ")
		price=menu.get(food,-1)
		if price ==-1:
			print("Check food item name ")
		else:
			qty=int(input("Enter quantity "))
			amount=amount+price*qty
			

	elif op==2:
		print("amount =",amount)
	elif op==3:
		break
	else:
		print("Invalid option ")