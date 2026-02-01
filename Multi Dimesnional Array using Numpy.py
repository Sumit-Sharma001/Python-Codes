import numpy as n
r=int(input("enter the number of rows:"))
c=int(input("enter the number of columns:"))
n_array=n.zeros((r,c))
for a in range(r):
    for b in range(c):
        n_array[a][b]=int(input("enter the element at position ({0},{1}):".format(a,b)))
print("the array is:")
print(n_array)