class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0
    #=================================ADD VALUE================================O(1)
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
        # if music_id > self.n:
        #     print("ERROR")
        #     return
        current = self.head
        while current:
            if current.value.music_id == music_id:
                self.delete(current.value)
                break
            current = current.next
        
        
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
        while current:
            print(current.value)
            current = current.next
            
            
    #=============================SEARCH VALUE BY ID===========================
    def search_by_id(self,music_id):
        # if music_id > self.n:
        #     print("ERROR")
        #     return
        current = self.head
        while current:
            if current.value.music_id == music_id:
                print(current.value)
                break
            current = current.next
            
        
    def get_years(self):
        years = [0] * self.n
        current = self.head
        for i in range(self.n):
            years[i] = current.value.year
            if i != self.n - 1:
                current = current.next
        return years
    
    def print_sorting(self,years):
        # current = self.head
        # for i in range(self.n):
        #     current = self.head
        #     for _ in range(self.n):
        #         if years[i] == current.value.year:
        #             print(current.value)
        #             break
        #         current = current.next
        
        current = self.head
        values = {}
        while current:
            values[current.value.year] = current.value
            current = current.next
        
        for year in years:
            print(values[year])
            
# x = Linkedlist()
# x.insert(2)
# x.insert(3)
# x.insert(24)

# x.showAll()
# # print(x.leng)