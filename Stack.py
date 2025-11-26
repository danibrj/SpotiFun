class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    
    def push(self,value):
        if self.n == 100:
            print("is full")
            return
        
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.n +=1
    
    
    # def pop()