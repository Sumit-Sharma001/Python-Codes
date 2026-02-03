a=int(input("How maay lines you want to print the star in a triangle"))
for i in range(0,a):
    for j in range(a,i,-1):
        print("*",end="")
    print()