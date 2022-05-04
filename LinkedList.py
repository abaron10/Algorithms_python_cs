# ---------------------------------------------------------------------------------------------------------
# --------------------------------------------------LINKED_LIST-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Spell checkers
# Dictionaries
# Compilers
# Code editors
# Employee number -----> hash function -----> Address in memory
# Insert  O(1)
# Lookpup O(1)
# Remove  O(1)

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        # Equivalente del toString() de Java
        def __repr__(self):
            return str(self.value)

    def addLast(self, value):
        newNode = self._Node(value)
        if self.first is None:
            self.first = self.last = newNode
            return
        self.last.next = newNode
        self.last = newNode

    def addFirst(self, value):
        newNode = self._Node(value)
        if self.first is None:
            self.first = self.last = newNode
            return
        next = self.first
        self.first = newNode
        self.first.next = next

    def indexOf(self, item):
        count = 0
        current = self.first
        while current is not None:
            if current.value == item:
                return count
            current = current.next
            count += 1
        return -1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty LinkedList")

        if self.first == self.last:
            self.first = self.last = None
            
        second = self.first.next
        self.first.next = None
        self.first = second

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty LinkedList")
        previous = self.getPrevious(self.last)

        previous.next = None
        self.last = previous

    def reverse(self):
        previous = self.first
        current = self.first.next
        #  [2 ,  3 ,  5]
        #   p -> c -> n
        while current is not None: 
            nextValue = current.next
            current.next = previous
            previous = current
            current = nextValue

        self.last = self.first
        self.last.next = None
        self.first = previous

    def size(self):
        contador = 0
        current = self.first

        if self.isEmpty():
            return 0
        while current is not None:
            current = current.next
            contador +=1
        return contador

    def contains(self, item):
        return self.indexOf(item) != -1

    def getPrevious(self, node):
        current = self.first
        while current is not None:
            if current.next == node:
                return current
            current = current.next
        return None

    def toArray(self):
        array = []
        current = self.first
        while current is not None:
            array.append(current.value)
            current = current.next
        
        return array
        
    def kthElementFromEnd(self, element):
        first = self.first
        second = self.first
        #1 -> 5 -> 9 -> 2 -> 6   n=2
        for i in range[0:element-1]:
            second = second.next
            if second is None:
                raise IndexError

        while second.next is not None:
            first = first.next
            second = second.next

        return first.value


    def printMiddle(self):
        #1 -> 5 -> 9 -> 2  n=2
        #1 -> 5 -> 9
        first = self.first
        second = self.first
        while second.next != self.last and second != self.last:
            first = first.next
            second = second.next.next
        if second == self.last:
            print(first.value)
        else:
            print(f"{first.value}  {second.value}")
        

    def isEmpty(self):
        return self.first == None

    

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.first == other.first

    def __repr__(self):
        return str(self.first)

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.first, self.last))