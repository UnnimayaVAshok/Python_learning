#use of nested if
Degree = input("Enter your degree")
cgpa = float(input("Enter your cgpa"))
if Degree.lower() == 'cs' :
    if cgpa >= 6.00 :
        print("Eligible")
else :
    print("Not eligible")

#use of in
if Degree in('CS','IT','BCA') :
    print("Eligible")
else :
    print("Not eligible")

#use of and/or
name = input("Enter your name")
age = int(input("Enter your age"))
if name.lower() == 'arya' and age >= 20 :
    print("You got it")
elif name.lower() == 'unni' or age == 25:
    print("You can try it again")
else :
    print("Better luck next time")