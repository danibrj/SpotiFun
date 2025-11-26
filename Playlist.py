from Linkedlist import Linkedlist as Lk
class Playlist:
    def __init__(self,playlist_id,playlist_name):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.playlist_songs = Lk()
        
    #=================================ADD MUSIC================================
    def insert(self,newMusic):
        self.playlist_songs.insert(newMusic)
        print(f"{newMusic["mname"]} added to playlist successfully")
    
    #================================REMOVE MUSIC==============================
    def delete(self,music_id):
        self.playlist_songs.search_for_delete(music_id)
        
    #========================SHOW ALL PLAYLIST INFORMATION=====================
    def showAllInfo(self):
        print(f"----------Playlist << {self.playlist_name} >>----------")
        self.playlist_songs.showAll()
        
    #============================SEARCH MUSIC BY ID============================
    def search(self,music_id):
        self.playlist_songs.search_by_id(music_id)
        
        
    def merge_by_year(self):
        years = self.playlist_songs.get_years()
    
    def merge(self,years):
        
        
