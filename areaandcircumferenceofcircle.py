#wapp to read readius of circle and find the area and circumference of circle.


n1=float(input("Enter the radius "))

area=3.14*n1*n1
#area=3.14*n1**2

cir=2*3.14*n1

print("Area =",round(area,2))
print("Circumference=",round(cir,3))

print("Area=%.2f" %area)
print("Circumference=%.3f" %cir)