class SparseSet:
    def __init__(self,maxValu,capasity):
        self.sparse = [0] * (maxValu + 1)
        self.dense = [0] * capasity
        self.capasity = capasity
        self.maxValue = maxValu
        self.n = 0
    #==============================SEARCH A ARTIST=============================    
    def search(self,value):
        if self.sparse[value] < self.n and self.dense[self.sparse[value]] == value:
            return self.sparse[value] 
        return -1
     
    #==============================ADD NEW ARTIST==============================
    def insert(self,value):
        if self.n >= self.capasity:
            return
        if value > self.maxValue:
            return
        if self.search(value) != -1:
            return
        
        self.dense[self.n] = value
        
        self.sparse[value] = self.n
        
        self.n += 1
    #==============================REMOVE A ARTIST=============================
    def delete(self,value):
        if self.search(value) == -1:
            print("not found!!")
            return
        
        last_element = self.dense[self.n - 1]
        value_index = self.sparse[value]
        self.dense[value_index] = last_element
        self.sparse[last_element] = value_index
        self.dense[self.n - 1] = 0
        self.sparse[value] = 0
        self.n -= 1
    #===========================CLEAR ALL INFORMATION==========================
    def clear(self):
        self.n = 0