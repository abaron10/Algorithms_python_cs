# ---------------------------------------------------------------------------------------------------------
# --------------------------------------------------PRIORITY_QUEUE-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Implement the undo features
# Build compilers
# Evaluate expresions
# LIFO

class PriorityQueue:
    def __init__(self):
        self.array = []


    #[2,2]
#
    def add(self, value):
        prev = len(self.array) -1
        if prev < 0 or self.array[prev] < value:
            self.array.append(value)
            return self.array
        self.array.append(0)
        while (value < self.array[prev] and prev > -1):
            self.array[prev + 1] = self.array[prev]
            self.array[prev] = value
            prev -= 1
        return self.array

  





