a=int(input("How many lines you want to print the star in a triangle"))
for i in range(0,a):
    for j in range(a,i,-1):
        print(j,end="")
    print()
