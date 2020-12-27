

class Node:
    def __init__(self, elem, link = None):
        self.data = elem        
        self.link = link
    
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def push(self, item):
        n = Node(item, self.head)
        self.head = n
    def pop(self):
        if not self.isEmpty():
            n = self.head
            self.head = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.head.data
    def size(self):
        if self.isEmpty():
            return None
        else:
            count = 0
            n = self.head
            while not n == None:
                n = n.link
                count += 1
            return count
    def getNode(self, pos):
        if pos < 0:
            return None
        else:
            node = self.head
            while pos > 0 and node != None:
                node = node.link
                pos -= 1
            return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            else:
                node = node.link
        return None

    def insert(self, pos, elem):
        beforelink = self.getNode(pos-1)
        if beforelink == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, beforelink)
            beforelink.link = node
    def delete(self, pos):
        beforelink = self.getNode(pos-1)
        if beforelink == None:
            if self.head is not None:
                self.head = self.head.link
        elif beforelink != None:
            beforelink.link = beforelink.link.link
            



