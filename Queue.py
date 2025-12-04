class Queue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        self.arr.append(value)
        self.rear += 1
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return None

        value = self.arr.pop(0)
        self.size -= 1
        self.rear -= 1
        return value
    
    def peak(self):
        if self.size == 0:
            return None
        return self.arr[self.front]
    
    def delete(self,value):
        for _ in range(self.size):
            if value == self.peak():
                self.dequeue()
            else:
                temp = self.dequeue()
                self.enqueue(temp)
    
    def delete_sogns_of_one_artist(self,artist_name):
        for data in list(self.arr):
            if data.artist_name == artist_name:
                self.delete(data)
            
    def found(self,music_name):# O(n)
        for data in self.arr:
            if data.music_name == music_name:
                print(data) 
    
    def get_music_by_id(self,music_id):#O(n)
        for data in self.arr:
            if data.music_id == music_id:
                return data
        return None
    
    def delete_all_info(self):
        self.arr = []
        self.front = 0
        self.rear = -1
        self.size = 0
                
    def get_max(self):
        max = -999
        for data in self.arr:
            if data.rating > max:
                max = data.rating
        
        for data in self.arr:
            if data.rating == max:   
                return data     
                
    def get_min(self):
        min = 999
        for data in self.arr:
            if data.rating < min:
                min = data.rating
        
        for data in self.arr:
            if data.rating == min:   
                return data 
            
            
    # def prints(self):
    #     if self.size == 0:
    #         print("Queue is empty")
    #         return

    #     for i in range(self.front, self.rear + 1):
    #         print(self.arr[i], end=" ")
    #     print()
    
    def __str__(self):
        items = ""
        for data in self.arr:
            items += (str(data)) + " | "
        return items

# x = Queue()
# x.enqueue(1)
# x.enqueue(2)
# x.enqueue(3)
# x.enqueue(4)
# print(x.peak())
# print("--------")
# x.delete(1)
# print(x.peak())

# x.prints()
