n = int(input("enter no. of rows : "))
rows = n
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()