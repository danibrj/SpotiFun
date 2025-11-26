from Playlist import Playlist as PL
from SparseSet import SparseSet as SpSet
from Artist import Artist
from Song import Song
# from Stack import Stack
class Spotifun:
    def __init__(self):
        # self.sparse = {} # for id's index
        # self.dense = [] # for ids
        self.SSet = SpSet(100,100)
        self.artist_name = {} # for id's name
        self.songs = {}
        self.playlists = {}
        
    #==============================ADD NEW ARTIST==============================
    def adds(self,artist_id,artist_name):
        # if self.contains(artist_id):
        #     print("this id already exist.")
        #     return
        
        # if artist_id > 100:
        #     print("id is out of correct range.")
        #     return
        artist = Artist(artist_name,artist_id)
        
        self.SSet.insert(artist)
        # self.sparse[artist_id] = len(self.dense)
        # self.dense.append(artist_id)
        # self.artist_name[artist_id] = artist_name
        
    #==============================REMOVE  ARTIST==============================
    def dels(self,artist_id):
        # if not self.contains(artist_id):
        #     print("not found any artist with this id") 
        #     return
        
        # index = self.sparse[artist_id]
        # last_id = self.dense[-1]
        
        # self.dense[index] = last_id
        # self.sparse[last_id] = index
        # # delete id
        # self.dense.pop()
        # #delete id index
        # self.sparse.pop(artist_id,None)
        self.SSet.delete(artist_id)
        #delete id name
        # self.artist_name.pop(artist_id,None)
    #==============================ADD NEW  MUSIC==============================    
    def addms(self,music_name ,artist_name,year,rating,contents):
        # self.songs[len(self.songs)+1]= { "mname":music_name ,"aname":artist_name,"year":year,"rating":rating,"contents":contents}
        
        self.SSet.add_music_to_a_artist(music_name ,artist_name,year,rating,contents)
        
    #===============================FIND A MUSIC===============================
    def findms(self,music_name):
        self.SSet.all_songs.found(music_name)
        
        
        # self.search_on_songs(music_name,"mname")
        
    #==============================FIND  A ARTIST==============================
    def finds(self,artist_id):
        letter = "="*60
        print(f"{letter}details{letter}")
        self.SSet.search_by_id2(artist_id)
        print(f"{letter}======={letter}")
        
    #============================WORD COUNT IN MUSIC===========================
    def countw(self,artist_id,music_id,word):
        
        artist = self.SSet.search_by_id(artist_id)
        mus = None
        for music in artist.songs:
            if music.music_id == music_id:
                mus = music
        texts = mus.contents
        count = 0
        for i in range(1,len(texts)+1):
            string = texts[i]
            strs = string.strip().split()
            for i in range(len(strs)):
                if strs[i] == word:
                    count += 1
        print(count)
        
        # artist_name = self.artist_name[artist_id]
        # music_info = None
        # for i in range(1,len(self.songs)+1):
        #     if i == music_id and self.songs[i]["aname"] == artist_name:
        #         music_info = self.songs[i]
        # x = music_info["contents"]
        # count = 0
        # for i in range(1,len(x)+1):
        #     string = x[i]
        #     strs = string.strip().split()
        #     for i in range(len(strs)):
        #         if strs[i] == word:
        #             count += 1
        # print(count)
        
    #=============================ADD NEW PLAYLIST=============================
    def addp(self,playlist_id,playlist_name):
        new_playlist = PL(playlist_id,playlist_name)
        
        self.playlists[len(self.playlists)+1] = new_playlist
    
    #===========================ADD NUSIC TO PLAYLIST==========================
    def addmp(self,music_id,playlist_id):
        x = 0
        for i in range(1,len(self.songs)+1):
            if i == music_id:
                x = 1
                break
        if x == 0:
            print("not found")
            
        music = self.songs[music_id]
        
        for i in range(1,len(self.playlists)+1):
            if self.playlists[i].playlist_id == playlist_id:
                self.playlists[i].insert(music)
      
    #=============================FIND A PLAYLIST==============================      
    def searchp(self,playlist_id):
        for i in range(1,len(self.playlists)+1):
            if self.playlists[i].playlist_id == playlist_id:
                self.playlists[i].showAllInfo()
                break
            
            
    #======================SEARCH A WORD ON SONG'S TEXT========================
    def searchw(self,artist_id,music_id,word):
        artist = self.SSet.search_by_id(artist_id)
        mus = None
        for music in artist.songs:
            if music.music_id == music_id:
                mus = music
        texts = mus.contents
        
        # artist = self.artist_name[artist_id]
        # target_music = {}
        # for i in range(1,len(self.songs)+1):
        #     if self.songs[i]["aname"] == artist and i == music_id :
        #         target_music = self.songs[i]
        # music_contents = target_music["contents"]
        count = 0
        for i in range(1,len(texts)+1):
            words = texts[i].strip().split()
            for i in range(len(words)):
                if words[i] != word:
                    count += 1
                else:
                    print(count + 1)
                    return 
        
    #=========================SEARCH MUSIC IN PLAYLIST=========================
    def searchmp(self,playlist_id,music_id):
        for i in range(1,len(self.playlists)+1):
            if self.playlists[i].playlist_id == playlist_id:
                self.playlists[i].search(music_id)
    
    #========================REMOVE MUSIC FROM PLAYLIST========================    
    def delmp(self,playlist_id,music_id):
        for i in range(1,len(self.playlists)+1):
            if self.playlists[i].playlist_id == playlist_id:
                self.playlists[i].delete(music_id)
                
    #=======================PRINT ALL ARTISTS INFORMATION======================
    def prints(self):
        print("_______________All Artists Details_______________")
        for i in range(self.SSet.n):
            name = self.artist_name[self.SSet.dense[i]]
            print(f"-------id: {self.SSet.dense[i]}------")
            print(f"{self.SSet.dense[i]} : {name}")
            print("musics:")
            self.search_on_songs(name,"aname")
            print("--------------------")
        print("_______________________END_______________________")
        
    #===========================CLEAR ALL INFORMATION==========================
    def cls(self):
        self.SSet.clear()
        # self.sparse.clear()
        # self.dense.clear()
        self.artist_name.clear()
        self.songs.clear()
        
        
    #===========================A AUXILIARY FUNCTION===========================
    def search_on_songs(self,input,idx):
        is_exist = False
        for i in range(1,len(self.songs)+1):
            if self.songs[i][idx] == input:
                is_exist = True
                print(self.songs[i])
        if(not is_exist):
            print(f"music for < {input} > not found")
            
    def showp(self,playlist_id):
        for i in range(1,len(self.playlists)+1):
            if self.playlists[i].playlist_id == playlist_id:
                self.playlists[i].merge_by_year()
    # # a auxiliary function       
    # def contains(self,artist_id):
    #     if artist_id not in self.sparse:
    #         return False
    #     index = self.sparse[artist_id]
    #     return self.dense[index] == artist_id
        
        
    

# x = Spotifun()
# x.adds(1,"danial")
# print(x.sparse)
# print(x.dense)
# print(x.artist_name)
# print(x.songs)
# x.adds(3,"ali")
# print(x.sparse)
# print(x.dense)
# print(x.artist_name)
# print(x.songs)
# x.adds(2,"dariush")
# print(x.sparse)
# print(x.dense)
# print(x.artist_name)
# print(x.songs)
# x.adds(4,"amir")
# print(x.sparse)
# print(x.dense)
# print(x.artist_name)
# print(x.songs)
# x.dels(3)
# print(x.sparse)
# print(x.dense)
# print(x.artist_name)
# print(x.songs)
# x.addms("ay eshgh","dariush",2015,3,"eshgh","yar","to ke")
# x.addms("ay eshgh","amir",2022,3,"eshgh","fd","grrt")
# x.finds(2)
# print(x.songs)
# print("-------")
# x.prints()
# print(x.artist_name)
# print(x.SSet.dense)
# print(x.SSet.sparse)
# x.cls()
# print("-------")
# print(x.SSet.dense)
# print(x.SSet.sparse)
# x.prints()
# x.finds(4)
# print(x.artist_name)


