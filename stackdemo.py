#menu driven p for stack implementation

import array
stack=array.array("i",[])

while True:
	op=int(input("1>push 2>pop 3>peek 4>display 5>exit "))
	if op==1:
		ele=int(input("Enter the element "))
		stack.append(ele)
		print(ele,"is pushed into the stack")
	elif op==2:
		if len(stack)==0:
			print("Stcak is empty")
		else:
			ele=stack.pop()
			print("popped element is",ele)
	elif op==3:
		if len(stack)==0:
			print("Stcak is empty")
		else:
			ele=stack[-1]
			print("peeked element is",ele)
	
	elif op==4:
		if len(stack)==0:
			print("Stcak is empty")
		else:
			print(stack)
	elif op==5:
		break
	else:
		print("Invalid Option ")