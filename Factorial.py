a=int(input("enter thenumber of which you want to find the factorial: "))
if a==0:
    print("the factorial of 0 is 1")
else: 
    f=1
    for i in range(1,a+1):
          f=f*i
    print("the factorial of",a,"is",f)