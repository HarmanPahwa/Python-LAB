rows = 5
for i in range(rows, 0, -1):
    for j in range(rows, i - 1, -1):
        print(j, end=' ')
    
    for j in range(i):
        print(i, end=' ')
    
    for j in range(i + 1, rows + 1):
        print(j, end=' ')
    
    print()
