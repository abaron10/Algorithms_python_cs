class Sorting:

    #Select a random pivot
    

    #b i 
    #  3  6  1  10  13  15  22
    #---left------|pivot|--right--
    #left must be smaller than the pivot and right must be higher than the pivot
    #b = boundary end of left partition strats at -1
    #i = index = 0
    #start from the begining an then compare with the pivot , if is small we increase the pivot
    #and perform a swap


    def QuickSort(self, array, start, end):
        if start >= end:
            return
        boundary = self.partition(array, start, end)
        self.QuickSort(array, start, boundary - 1)
        self.QuickSort(array, boundary + 1, end)

    def partition(self, numbers, high, low):
        pivot = numbers[high]
	    item = low - 1

        for i in range(low, high):
            if numbers[i] <= pivot:
                item = item + 1
                (numbers[item], numbers[i]) = (numbers[i], numbers[item])

        (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])

        return item + 1
        
    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp



