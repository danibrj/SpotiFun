class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0
    #=================================ADD VALUE================================
    def insert(self,input):
        newNode = Node(input)
        self.n += 1
        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode
        
        
    #================================REMOVE VALUE==============================   
    def search_for_delete(self,music_id):
        if music_id > self.n:
            print("ERROR")
            return
        current = self.head
        for _ in range(music_id - 1):
            current = current.next
        self.delete(current.value)
        
    def delete(self,input):
        current = self.head
        prev = None
        
        while current:
            if current.value == input:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.n -= 1
                print("removed successfully")
                return
            prev = current
            current = current.next
        print("not found")
        return 
    
    #================================SEARCH VALUE==============================
    def search(self,input):
        current = self.head
        while current:
            if current.value == input:
                return True
            current = current.next
        return False    
    
    #===============================SHOW ALL VALUE=============================    
    def showAll(self):
        current = self.head
        count = 1
        while current:
            print(f"{count} : {current.value}")
            current = current.next
            count += 1
            
    #=============================SEARCH VALUE BY ID===========================
    def search_by_id(self,music_id):
        if music_id > self.n:
            print("ERROR")
            return
        current = self.head
        count = 1
        while current:
            if music_id == count:
                print(current.value)
                break
            current = current.next
            count += 1
        
    def get_years(self):
        years = [0] * self.n
        current = self.head
        for i in range(self.n):
            years[i] = current.value["year"]
            if i != self.n - 1:
                current = current.next
        return years
            
# x = Linkedlist()
# x.insert(2)
# x.showAll()
# print(x.leng)