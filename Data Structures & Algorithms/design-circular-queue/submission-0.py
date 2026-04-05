class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k)]
        self.k = k
        self.curcap = 0
        self.head = 0
        self.tail = k-1

    def enQueue(self, value: int) -> bool:
        if self.curcap < self.k:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            self.curcap += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.curcap == 0:
            return False
        self.queue[self.head] = -1
        self.head = (self.head + 1) % self.k
        self.curcap -= 1
        return True
        
        
    def Front(self) -> int:
        return self.queue[self.head]
        

    def Rear(self) -> int:
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return False if self.curcap > 0 else True
        

    def isFull(self) -> bool:
        return True if self.curcap == self.k else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



