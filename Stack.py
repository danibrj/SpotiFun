class Stack:
    def __init__(self):
        self.values = []
        self.n = 0
        self.count = self.n - 1
    
    def push(self,value):
        if self.n == 100:
            print("is full")
            return
        self.values.append(value)
        self.n +=1
        
    def peak(self):
        if self.n == 0:
            raise IndexError("stack is empty")
        return self.values[-1]
    
    def delete(self,value):
        if self.n == 0:
            raise IndexError("stack is empty")
        temp_stack = []
        while self.peak() != value:
            temp_stack.append(self.values.pop())
            self.n -= 1
            
        self.values.pop()
        self.n -= 1
        
        while temp_stack:
            self.push(temp_stack.pop())
            
        
    def delete_sogns_of_one_artist(self,artist_name):
        for data in list(self.values):
            if data.artist_name == artist_name:
                self.delete(data)

    def delete_all_info(self):
        self.values = []
        self.n = 0
                
    def get_music_by_id(self,music_id):#O(n)
        for data in self.values:
            if data.music_id == music_id:
                return data
        return None
    
    def found(self,music_name):# O(n)
        for data in self.values:
            if data.music_name == music_name:
                print(data) 
    
    def prints(self):
        for data in self.values:
            print(data)
        
    def search_for_undo(self):
        if self.n == 0:
            return
        
        if self.count == -1:
            self.count = self.n - 1
        
        print(self.values[self.count])
        
        self.count -= 1
        

    def get_max(self):
        max = -999
        for data in self.values:
            if data.rating > max:
                max = data.rating
        
        for data in self.values:
            if data.rating == max:   
                return data     
                
    def get_min(self):
        min = 999
        for data in self.values:
            if data.rating < min:
                min = data.rating
        
        for data in self.values:
            if data.rating == min:   
                return data 
    
    def __str__(self):
        items = ""
        for data in self.values:
            items += (str(data)) + " | "
        return items

# x = Stack()
# x.push(1)
# x.push(2)
# x.push(3)
# x.push(4)
# print("---")
# x.delete(5)
# x.prints()
# # x.delete_all_info()
# print("---")
# x.prints()
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
#         self.n = 0
#         self.count = 0
    
#     def push(self,value):
#         if self.n == 100:
#             print("is full")
#             return
        
#         newNode = Node(value)
#         newNode.next = self.top
#         self.top = newNode
#         self.n +=1
    
#     def delete(self,value):
#         current = self.top
#         if value == self.top.value:
#             self.top = current.next
#             return
        
#         prev = None
#         while current:
#             if current.value == value:
#                 if current == self.top:
#                     self.top = current.next
#                 else:
#                     prev.next = current.next
#                 self.n -= 1
#             else:
#                 prev = current
#             current = current.next
            
#     def delete_all_info(self):
#         self.top = None
    
#     def delete_sogns_of_one_artist(self,artist_name):
#         current = self.top
#         prev = None
#         while current:
#             if current.value.artist_name == artist_name:
#                 if current == self.top:
#                     self.top = current.next
#                 else:
#                     prev.next = current.next
#                 self.n -= 1
#             else:
#                 prev = current
#             current = current.next
            
#     def get_music_by_id(self,music_id):#O(n)
#         current = self.top
#         while current:
#             if current.value.music_id == music_id:
#                 return current.value
#             current = current.next
#         return None
    
#     def found(self,music_name):# O(n)
#         current = self.top
#         while current:
#             if current.value.music_name == music_name:
#                 print(current.value)
#             current = current.next
    
#     def prints(self):
#         current = self.top
#         while current:
#             print(current.value)
#             current = current.next
        
#     def search_for_undo(self):
#         if self.count == self.n:
#             self.count = 0
#         current = self.top
#         if current is None:
#             return
        
#         for _ in range(self.count):
#             current= current.next
        
#         self.count += 1
#         return current.value
#     # def pop()
#     def get_max(self):
#         current = self.top
#         max = -999
#         while current:
#             if current.value.rating > max:
#                 max = current.value.rating
#             current = current.next
            
#         current = self.top
#         while current:
#             if current.value.rating == max:
#                 return current.value
#             current = current.next
    
#     def get_min(self):
#         current = self.top
#         min = 999
#         while current:
#             if current.value.rating < min:
#                 min = current.value.rating
#             current = current.next
        
#         current = self.top    
#         while current:
#             if current.value.rating == min:
#                 return current.value
#             current = current.next
    
#     def __str__(self):
#         items = ""
#         current = self.top
#         while current:
#             items += (str(current.value)) + " | "
#             current = current.next
#         return items