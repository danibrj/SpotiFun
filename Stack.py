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
    
    def get_music_by_id(self,music_id):
        current = self.top
        while current:
            if current.value.music_id == music_id:
                return current.value
            current = current.next
        return None
    
    def found(self,music_name):
        current = self.top
        while current:
            if current.value.music_name == music_name:
                print(current.value)
            current = current.next
    
    def prints(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next
    # def pop()

# x = Stack()
# x.push(1)
# x.prints()
# print("---")
# x.push(2)
# x.prints()