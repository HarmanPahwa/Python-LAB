list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_lists = list(map(lambda x, y: x + y, list1, list2))
difference = list(map(lambda x, y: x - y, list1, list2))
print("Added lists:", added_lists)
print("Differences:", difference)
