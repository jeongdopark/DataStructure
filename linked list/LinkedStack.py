# top이 뭔지 모르고 봤다가 이해를 못 했었음, stack은 후입 선출이므로 가장 위에 있는 데이터가 가장 먼저 반환된다 
# 그러므로 가장 위에 있는 데이터를 가르키는 변수가 필요하다.

class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link
    
class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def clear(self):
        self.top = None
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data   
    def size(self):
        if self.isEmpty():
            return None
        else:
            count = 0
            n = self.top
            while not n == None:
                n = n.link
                count += 1
            return count