#wapp to read marks and display grades

m=int(input("Enter the marks "))

if m>=70:
	print("Grade=Distinction")
elif m>=60 and m<=70:
	print("Grade=First class")
elif m>=50 and m<=60:
	print("Grade=Second class")
elif m>=40 and m<=50:
	print("Grade=Pass class")
else:
	print("Grade=Fail")