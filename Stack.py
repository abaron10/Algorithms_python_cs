
# ---------------------------------------------------------------------------------------------------------
# --------------------------------------------------STACKS-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Implement the undo features
# Build compilers
# Evaluate expresions
# LIFO

class Stack:

    def __init__(self):
        self.array = []

    def add(self, value):
        if value is None:
            raise ValueError
        self.array.append(value)

    def remove(self):
        return self.array.pop() if len(self.array) > 0 else None

    def peek(self):
        return self.array[len(self.array) -1] if len(self.array) > 0 else None

