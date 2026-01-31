a=int (input("enter first number a: "))
b=int (input("enter second number b: "))
print("choose the option from below list: \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.modulus \n 6.exponentiation \n 7.floor division \n")
option = int(input("enter your option: "))
if option == 1:
    print("the addition of a and b is: ", a + b)
elif option == 2:
    print("the subtraction of a and b is: ", a - b)
elif option == 3:
    print("the multiplication of a and b is: ", a * b)
elif option == 4:
    print("the division of a and b is: ", a / b)
elif option == 5:
    print("the modulus of a and b is: ", a % b)
elif option == 6:
    print("the exponentiation of a and b is: ", a ** b)
elif option ==  7:
    print("the floor division of a and b is: ", a // b)
else:
    print("invalid option selected")
