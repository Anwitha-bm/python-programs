def division (x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Error!")
    else:
        print("The answer is :",result)
    finally:
        print('testing try...except...finally')
x= int(input("Enter the value of x :"))
y= int(input("Enter the value of y :"))
division(x,y)