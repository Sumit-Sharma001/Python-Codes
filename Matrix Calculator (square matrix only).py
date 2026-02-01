import numpy as n
print("This Matrix Calculator works only for Square Matrices")
r=int(input("enter the number of rows:"))
c=int(input("enter the number of columns:"))
n_array1=n.zeros((r,c),dtype=int)
for a in range(r):
    for b in range(c):
        n_array1[a][b]=int(input("enter the element at position ({0},{1}):".format(a,b)))
print("the array1 is:")
print(n_array1)
n_array2=n.zeros((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        n_array2[i][j]=int(input("enter the element at position ({0},{1}):".format(i,j)))
print("the array2 is:")
print(n_array2)
print("choose the option from below list: \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division ")
op=int(input("enter the option number:"))
if op==1:
    print("the addition of two arrays is:")
    print(n_array1+n_array2)
elif op==2:
    print("choose the way of subtraction: \n 1.Matrix-1 - Matrix-2 \n 2.Matrix-2 - Matrix-1")
    o=int(input("enter the option number:"))
    if o==1:
        print("the subtraction of two arrays is:")
        print(n_array1-n_array2)
    elif o==2:
        print("the subtraction of two arrays is:")
        print(n_array2-n_array1)
elif op==3:
    print("the multiplication of two arrays is:")
    print(n_array1@n_array2)
elif op==4:
     print("choose the way of Division: \n 1.Matrix-1 / Matrix-2 \n 2.Matrix-2 / Matrix-1")
     o=int(input("enter the option number:"))
     if o==1:
        print("the division of two arrays is:")
        print(n_array1/n_array2)
     elif o==2:
        print("the division of two arrays is:")
        print(n_array2/n_array1)

