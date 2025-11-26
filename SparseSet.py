from Artist import Artist
class SparseSet:
    def __init__(self,maxValu,capasity):
        self.sparse = [0] * (maxValu + 1)
        self.dense = [None] * capasity
        self.capasity = capasity
        self.maxValue = maxValu
        self.n = 0
    #==============================SEARCH A ARTIST=============================    
    def search(self,value):
        if self.sparse[value.artist_id] < self.n and self.dense[self.sparse[value.artist_id]] == value:
            return self.sparse[value.artist_id] 
        return -1
     
    #==============================ADD NEW ARTIST==============================
    def insert(self,value):
        if self.n >= self.capasity:
            return
        if value.artist_id > self.maxValue:
            return
        if self.search(value) != -1:
            return
        
        self.dense[self.n] = value
        
        self.sparse[value.artist_id] = self.n
        
        self.n += 1
    #==============================REMOVE A ARTIST=============================
    def delete(self,id): 
        artist = self.search_by_id(id)
        if self.search(artist) == -1 :
            print("not found!!")
            return
        
        last_element = self.dense[self.n - 1]
        value_index = self.sparse[artist.artist_id]
        self.dense[value_index] = last_element
        self.sparse[last_element.artist_id] = value_index
        self.dense[self.n - 1] = None
        self.sparse[artist.artist_id] = 0
        self.n -= 1
    #===========================CLEAR ALL INFORMATION==========================
    def clear(self):
        self.n = 0
    
    def search_by_id(self,artist_id):
        for artist in self.dense:
            if artist is not None and artist.artist_id == artist_id:
                return artist
        return None
    def search_by_id2(self,artist_id):
        for artist in self.dense:
            if artist is not None and artist.artist_id == artist_id:
                print(artist)
    def showAll(self):
        for artist in self.dense:
            if artist is not None:
                print(artist)
    
# x = Artist("danial", 1)
# x2 = Artist("ali", 2)
# y = SparseSet(100,100)
# y.insert(x)
# y.search_by_id2(1)
# print("-------")
# y.insert(x2)
# y.showAll()
# print("-------")

# y.delete(3)
# y.showAll()

