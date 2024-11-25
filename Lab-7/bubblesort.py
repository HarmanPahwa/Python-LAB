class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def get_sorted_data(self):
        return self.data


# Example Usage
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort(data)
bubble_sort.sort()
print("Bubble Sort:", bubble_sort.get_sorted_data())
