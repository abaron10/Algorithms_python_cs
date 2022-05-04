# ---------------------------------------------------------------------------------------------------------
# --------------------------------------------------HASH_TABLES-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Spell checkers
# Dictionaries
# Compilers
# Code editors
# Employee number -----> hash function -----> Address in memory
# Insert  O(1)
# Lookpup O(1)
# Remove  O(1)
from LinkedList import LinkedList
class HashTable:

    def __init__(self):
        self.array = [None for number in range(0,5)]
    
    # Chaining
    # The problem with this implementation is the amount of memory required to store the linked list
    # that handles the collision , also some values get lost becouse LinkedLists store the last values
    def addChaining(self,key,value):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is None:
            linkedList = LinkedList()
            linkedList.addFirst(value)
            self.array[hashedKey] = linkedList
        else:
            self.array[hashedKey].addLast(value)

    def getChaining(self,key):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is None:
            raise ValueError
        array = self.array[hashedKey].toArray()
        return array.pop()


    # Open Addressing -> Linear Probing
    # The problem with this implementation are the big clusters that are made due to linear assignments.
    # Linear Probing: hash(key) + 1
    def addLinear(self,key,value):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is not None:
            while True:
                hashedKey = hashedKey + 1
                if self.array[hashedKey] is None:
                    self.array[hashedKey] = value
                    break
        else:
            self.array[hashedKey] = value

    def getLinear(self,key):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is None:
            raise ValueError
        return self.array[hashedKey]

    # Open Addressing -> Quadratic Probing
    # The problem with this implementation are the big clusters that are made due to linear assignments.
    # Linear Probing: hash(key) + 1

    def addQuadratic(self,key,value):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is not None:
            while True:
                hashedKey = hashedKey + 1
                if self.array[hashedKey] is None:
                    self.array[hashedKey] = value
                    break
        else:
            self.array[hashedKey] = value

    def getQuadratic(self,key):
        hashedKey = self.hashing(key)
        if self.array[hashedKey] is None:
            raise ValueError
        return self.array[hashedKey]

    def hashing(self,key):
        return key % len(self.array) 
        


