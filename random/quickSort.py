class QuickSort:
    def sort(self, array):
        self.quickSort(array, 0, len(array) - 1)
        return array

    def calculatePivotIndex(self, array, min, max):
        pivot = (array[min]+array[max]) / 2 
        i = min
        j = max
        while(True):
            while (array[i] < pivot):
              i += 1
            while (array[j] > pivot):
              j -= 1

            if (i >= j):
              return j
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

# тут написать проверу - бежим в стороны он pivot, ищем и мменяем элементы больше меньеш пивота, пока индексы не сойдутся в пивот

    def quickSort(self, array, left, right):
        if (left < right):
            pivotIndex = self.calculatePivotIndex(array, left, right)
            self.quickSort(array, left, pivotIndex)
            self.quickSort(array, pivotIndex + 1, right)


print(QuickSort().sort([0, 4, 2, 4, 8, 6, 3, 2, 1]))
print(QuickSort().sort([1,4,2,5,78,9,3,54,25,645,2,1,2,6,9]))
# print(QuickSort().sort([1,4,2]))
# print(QuickSort().sort([1,4,2]))
# print(QuickSort().sort([1,4,2]))
# print(QuickSort().sort([1]))