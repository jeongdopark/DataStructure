

class DNode:
    def __init__(self,elem, prev = None, next = None):
        self.data = elem
        self.prve = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def clear(self):
        self.front = self.rear = None
    def size(self):
        if self.isEmpty():
            return None
        else:
            count = 0
            n = self.front
            while n != None:
                n = n.next
                count += 1
            return count
    
    def addFront(self, item):
        node = DNode(item, None, self.front)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.next
            if self.rear == None:
                self.front = None
            else:
                self.rear.prev = None
            return data