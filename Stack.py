class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
        self.count = 0
    
    def push(self,value):
        if self.n == 100:
            print("is full")
            return
        
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.n +=1
    
    def get_music_by_id(self,music_id):#O(n)
        current = self.top
        while current:
            if current.value.music_id == music_id:
                return current.value
            current = current.next
        return None
    
    def found(self,music_name):# O(n)
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
        
    def search_for_undo(self):
        if self.count == self.n:
            self.count = 0
        current = self.top
        
        for _ in range(self.count):
            current= current.next
        
        self.count += 1
        return current.value
    # def pop()
    def get_max(self):
        current = self.top
        max = -999
        while current:
            if current.value.rating > max:
                max = current.value.rating
            current = current.next
            
        current = self.top
        while current:
            if current.value.rating == max:
                return current.value
            current = current.next
    
    def get_min(self):
        current = self.top
        min = 999
        while current:
            if current.value.rating < min:
                min = current.value.rating
            current = current.next
        
        current = self.top    
        while current:
            if current.value.rating == min:
                return current.value
            current = current.next
    
    def __str__(self):
        items = [None] * self.n
        current = self.top
        i = 0
        while current:
            items[i] = (str(current.value))
            current = current.next
            i += 1
        return " | ".join(items)

# x = Stack()
# x.push(1)
# x.prints()
# print("---")
# x.push(2)
# x.prints()