class Sorting:

    def QuickSort(self, array, start, end):
        if start >= end:
            return
        boundary = self.partition(array, start, end)
        self.QuickSort(array, start, boundary - 1)
        self.QuickSort(array, boundary + 1, end)

    def partition(self, array, start, end):
        pivot = array[end]
        boundary = start - 1

        for i in range(len(array)):
            if array[i] < pivot:
                boundary = 1 + boundary
                self.swap(array, i, boundary)

        return boundary

    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
