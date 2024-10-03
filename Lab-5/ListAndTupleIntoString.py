int_list = [1, 2, 3]
int_tuple = (4, 5, 6)
combined = list(map(str, int_list + list(int_tuple)))
print(combined)
