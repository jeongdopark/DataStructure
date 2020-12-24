

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            hightest = 0
            for i in range(1, self.size()):
                if(self.items[hightest] < self.items[i]):
                    hightest = i
            return hightest
    def dequeue(self):
        hightest = self.findMaxIndex()
        if hightest is not None:
            self.items.pop(hightest)
    def peek(self):
        hightest = self.findMaxIndex()
        if hightest is not None:
            return self.items[hightest]



