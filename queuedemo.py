#menu driven p for queue implementation

import array
queue=array.array("i",[])

while True:
	op=int(input("1>push 2>pop 3>peek 4>display 5>exit "))
	if op==1:
		ele=int(input("Enter the element "))
		queue.append(ele)
		print(ele,"is pushed into the queue")
	elif op==2:
		if len(queue)==0:
			print("Queue is empty")
		else:
			ele=queue.pop(0)
			print("popped element is",ele)
	elif op==3:
		if len(queue)==0:
			print("Queue is empty")
		else:
			ele=queue[0]
			print("peeked element is",ele)
	
	elif op==4:
		if len(queue)==0:
			print("Queue is empty")
		else:
			print(queue)
	elif op==5:
		break
	else:
		print("Invalid Option ")