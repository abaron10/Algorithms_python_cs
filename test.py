



class PriorityQueue:

    def __init__(self):
        self.arr = []
    
    def __str__(self):
        return f"{self.arr}"

    def add(self,number):

        #[4,2]

        if len(self.arr) == 0:
            self.arr.append(number)
        else:
            self.arr.append(0)
            curr = len(self.arr) -1
            self.arr[curr] = number
            while self.arr[curr-1] > number and curr-1 > -1:
            #[4,2]
                temp = self.arr[curr-1]
                self.arr[curr-1] = number
                self.arr[curr] = temp
                curr-=1
            
        return self.arr

p = PriorityQueue()
p.add(4)
p.add(2)
p.add(1)
p.add(8)
p.add(5)
p.add(0)
p.add(53)
p.add(12)

print(p)