def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example Usage
data = [10, 20, 30, 40, 50]
print("Linear Search:", linear_search(data, 30))
