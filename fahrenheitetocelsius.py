#wapp to convert fahrenheite ro celsius

fah=float(input("Enter temp in fahrenheit"))

cel=(fah-32)*5/9

print("Fah=",fah)
print("Cel=",cel)

print("Fah=",round(fah,2))
print("Cel=",round(cel,3))

print("Fah=%.2f" %fah)
print("Cel=%.3f" %cel)

print("Fah=%.2f Cel=%.3f" %(fah,cel))



