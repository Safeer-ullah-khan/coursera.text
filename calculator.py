import math
Op=input("Enter a operator:+,-,*,/,%,^,sqrt,** ")
if Op in(["sqrt","**"]):
    if(Op=="sqrt"):
        Num=float(input("Enter a Number"))
        if(Num<0):
            print("Error:The number cannot be less than 0")
        else:
            print("The square root is equal to",math.sqrt(Num))

    elif(Op=="**"):
        Num=float(input("Enter a Number"))
        if(Num<0):
            print("Error:The number cannot be less than 0")
        else:
            print("The square is equal to",Num**2)

else:
    Num1=float(input("Enter a Number A"))
    Num2=float(input("Enter a Number B"))
    if(Op=="+"):
        print("The addition is:",Num1+Num2)
    elif(Op=="-"):
        print("The subtraction is:",Num1-Num2)
    elif(Op=="*"):
        print("The Multiplication is:",Num1*Num2)
    elif(Op=="/"):
        if(Num2==0):
            print("Number cannot be Divisible by zero:")
        else:
            print("The Divisiion is:",Num1/Num2)
    elif(Op=="%"):
        if(Num2==0):
            print("Number cannot be Remainder by zero:")
        else:
            print("The Remainder is:",Num1%Num2)
    elif(Op=="^"):
            print("The X ^ y is :",math.pow(Num1,Num2))
    else:
        print("Invalid operator")



    
