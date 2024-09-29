current_number = 1
max_number = 10 
rows = 3
for i in range(1, rows + 1):
    for j in range(1, 2 * i):
        if current_number < max_number:
            print(current_number, end=' ')
            current_number += 1
    print()