#Simple calculator
num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
operation = int(input("Enter 1 for addition\n2 for substraction\n3 for multiplication\n4 for division"))
if operation == 1:
    result = num1 + num2
    print("Result is : " +str(result))
elif operation == 2:
    result = num1 - num2
    print("Result is : " +str(result))
elif operation == 3:
    result = num1 * num2
    print("Result is : " +str(result))
elif operation == 4:
    try:
        result = num1/num2
        print("Result is : " +str(result))
    except ZeroDivisionError:
        print("Error")
else:
    print("Error")