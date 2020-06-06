#wapp to read a year and find if its a leap year

year=int(input("Enter year "))


b1= (year%100!=0)and(year % 4==0)  #every 4 yrs
b2= (year%100==0) and (year%400==0)  #every 400 yrs
 
if b1 or b2:
	print("Leap year")
else:
	print("Not a leap year")
