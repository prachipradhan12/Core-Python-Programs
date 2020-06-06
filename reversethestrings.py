'''
wapp to read sentence and reverse the sentence with every word too reversed
ip= kamal classes thane
op= enaht sessalc lamak
'''

s1=input("Enter a sentence ")

s2=s1.split(' ')

new_sen=''

for d in s2:
	new_sen=d[::-1]+" "+new_sen

print("original ",s1)
print("New",new_sen)