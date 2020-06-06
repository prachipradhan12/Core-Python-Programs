'''
ip=a,2,b,4,c,3
op=a a
   b b b b
   c c c
'''
s1="a,2,b,4,c,3"
s2=s1.split(',')

for i in range(0,len(s2),2):
	what=s2[i]
	how=int(s2[i+1])
	print((what+"\t")*how)
