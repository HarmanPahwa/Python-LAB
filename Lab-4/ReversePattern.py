current_number = 1
rows = 4 

for i in range(1, rows + 1):
    last_number = current_number + i - 1
    for j in range(last_number, current_number - 1, -1):
        print(j, end=' ')
    current_number += i
    print()
