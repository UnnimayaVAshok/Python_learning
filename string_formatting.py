"""
Practicing basics in python and different string formatting methods:
1. String concatenation
2. format() method
3. f-strings
"""
#Printing output
print("Hello World")
#name = "Unnimaya V Ashok"
#print(name)
#print("Hello",name)

first_name = "Unnimaya"
middle_name = "V"
last_name = "Ashok"

#String concatenation example
print("Hello" + first_name + middle_name + last_name)
#print("Hello" + ""+ first_name + "" + middle_name + "" + last_name)
#print("Hello" + " "+ first_name + " " + middle_name + " " + last_name)
#print("Hello",first_name,middle_name,last_name)

#Taking input
output = input("Enter your name")

#format() method example
output = "Hai {} ".format(output)
#output = "Hai {0} {1} {2}".format(first_name,middle_name,last_name)
#output = "Hai {2} {1} {0}".format(first_name,middle_name,last_name)
print(output)

#f-string example
output = f'Hai {first_name} {middle_name} {last_name}'
#output = f'Hai {middle_name} {last_name} {first_name}'
print(output.capitalize())
print(output.lower())
