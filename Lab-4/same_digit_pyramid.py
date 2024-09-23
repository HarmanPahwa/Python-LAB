n = int(input("enter no. of rows : "))

for i in range (n,0,-1):
    print(' '*(n-i),end ='')
    for j in range(i):
        print(n,end = ' ')
    print()