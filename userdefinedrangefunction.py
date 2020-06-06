'''
wapf myrange() to which we can pass 1 avg and 2 avg
ip=myrange(5)
   myrange(2,6)
'''
def myrange(p1=None,p2=None):
	if p1 is not None and p2 is None:
		start=1
		while start<=p1:
			print(start)
			start+=1
	elif p1 is not None and p2 is not None:
		start=p1
		while start<=p2:
			print(start)
			start+=1
myrange(5)
print()
myrange(2,6)	
			


