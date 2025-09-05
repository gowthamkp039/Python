print("Simple Calculator Program")
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
program=True
while program==True:
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.Exit")
    try:
        a=int(input("Enter 1/2/3/4 to perfrom arithmetic operatins or enter 5 to exit the program:"))
        if a==1:
            b=int(input("Enter a Value 1 to perform addition:"))
            c=int(input("Enter a Value 2 to perform addition:"))
            print(f"Sum of two numbers {b,c} is {addition(b,c)}")
        elif a==2:
            b=int(input("Enter a Value 1 to perform subtraction:"))
            c=int(input("Enter a Value 2 to perform subtraction:"))
            print(f"Difference of two numbers {b,c} is {subtraction(b,c)}")
        elif a==3:
            b=int(input("Enter a Value 1 to perform multiplication:"))
            c=int(input("Enter a Value 2 to perform multiplication:"))
            print(f"Multiple of two numbers {b,c} is {multiply(b,c)}")
        elif a==4:
            b=int(input("Enter a Value 1 to perform division:"))
            c=int(input("Enter a Value 2 to perform division:"))
            if c==0:
                print("Can't divide the value by zero")
            else:
                print(f"Division of two numbers {b,c} is {division(b,c)}")
        elif a==5:
            program=False
        else:
            print("Invalid Input")
    except ValueError as e:
        print(e)
    
