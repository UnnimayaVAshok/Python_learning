#Divisionbyzero error
x = 6
#print(x/0)

try:
    print(x/0)
except ZeroDivisionError as e:
    print("Cant divide by zero")
finally:
    print("Done")
