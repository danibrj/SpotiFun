from Song import Song
from Artist import Artist
from Stack import Stack
from Queue import Queue
class SparseSet:
    def __init__(self,maxValue,capasity):
        self.sparse = [-1] * (maxValue + 1)
        self.dense = [None] * capasity
        self.capasity = capasity
        self.maxValue = maxValue
        self.n = 0
        self.all_songs = Queue()
    # def find_music_by_name(self,music_name):
    
    #==============================SEARCH A ARTIST=============================    
    def search(self,value):
        if self.sparse[value.artist_id] < self.n and self.dense[self.sparse[value.artist_id]] == value:
            return self.sparse[value.artist_id] 
        return -1
     
    #==============================ADD NEW ARTIST==============================O(1)
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
    #==============================REMOVE A ARTIST=============================O(1)
    def delete(self,id): 
        artist = self.search_by_id(id)
        if artist is None:
            print("not found!!")
            return
        if self.search(artist) == -1 :
            print("not found!!")
            return
        
        last_element = self.dense[self.n - 1]
        value_index = self.sparse[artist.artist_id]
        self.dense[value_index] = last_element
        self.sparse[last_element.artist_id] = value_index
        self.dense[self.n - 1] = None
        self.sparse[artist.artist_id] = -1
        self.n -= 1
        artist.songs.delete_all_info()
        self.all_songs.delete_sogns_of_one_artist(artist.artist_name)
        
    #===========================CLEAR ALL INFORMATION==========================
    def clear(self):
        self.sparse = [-1] * (self.maxValue + 1)
        self.dense = [None] * self.capasity
        self.n = 0    
    
    def search_by_id(self,artist_id):#O(1)
        # for artist in self.dense:
        #     if artist is not None and artist.artist_id == artist_id:
        #         return artist
        # return None
        index = self.sparse[artist_id]
        return self.dense[index]
    
    def search_by_id2(self,artist_id):#O(1)
        # for artist in self.dense:
        #     if artist is not None and artist.artist_id == artist_id:
        #         print(artist)
        #         return 
        # return None
        index = self.sparse[artist_id]
        artist = self.dense[index]
        print(artist)
        return 
                
    def showAll(self):
        for artist in self.dense:
            if artist is not None:
                print(artist)
    
    def add_music_to_all_songs(self,music_name ,artist_name,year,rating,contents):
        song = Song(music_name,self.all_songs.size +1,artist_name,year,rating,contents)
        self.all_songs.enqueue(song)
        self.add_music_to_a_artist(artist_name,song)
                   
    def add_music_to_a_artist(self,artist_name,song):
        
        
        
        for artist in self.dense:
            if artist is not None and artist.artist_name == artist_name:
                # song = Song(music_name,len(artist.songs)+1,artist_name,year,rating,contents)
                # song = self.all_songs[]
                artist.insert_music(song)
                # self.all_songs.push(song)
                
    def print_max(self):
        music = self.all_songs.get_max()
        print("best music is : ")
        print(music)
    
    def print_min(self):
        music = self.all_songs.get_min()
        print("worst music is : ")
        print(music)
    
x = Artist("danial", 1)
x2 = Artist("ali", 2)
x3 = Artist("df", 3)

y = SparseSet(100,100)
y.insert(x)
# y.search_by_id2(1)
print("-------")
y.insert(x2)
y.insert(x3)
y.showAll()
print("-------")
# y.search_by_id2(2)
y.add_music_to_all_songs("a","danial",2015,5,{1:"adsd sa"})
y.add_music_to_all_songs("b","ali",2014,8,{1:"adfsdf777777ddf sa"})
y.add_music_to_all_songs("c","df",2013,5,{1:"adfsdfddf sa"})
y.add_music_to_all_songs("d","danial",2013,5,{1:"adfsdfddf sa"})

y.search_by_id2(1)
print("-------")
# # y.delete(2)
# y.showAll()
# print("------")
# y.search_by_id2(2)

print(y.all_songs)
print("---------")
y.delete(1)
print(y.dense)
print(y.sparse)
print("**************")
# y.search_by_id2(1)
print(y.all_songs)



