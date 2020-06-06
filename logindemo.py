'''
wapp to read username and password if valid op->welcome else op->try again

'''

import getpass

s1='antman'
s2='batman'

un=input("Enter username ")
pas=getpass.getpass("Enter password ")

if (un==s1 and pas==s2):
	print("welcome!!!!!!")
else:
	print("Try again")
 