from Linkedlist import Linkedlist as Lk
class Playlist:
    def __init__(self,playlist_id,playlist_name):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.playlist_songs = Lk()
        
    #=================================ADD MUSIC================================
    def insert(self,newMusic):
        self.playlist_songs.insert(newMusic)
        print(f"{newMusic.music_name} added to playlist successfully")
    
    #================================REMOVE MUSIC==============================
    def delete(self,music_id):
        self.playlist_songs.search_for_delete(music_id)
        
    #========================SHOW ALL PLAYLIST INFORMATION=====================
    def showAllInfo(self):
        print(f"==========Playlist << name: {self.playlist_name} | id: {self.playlist_id}>>==========")
        self.playlist_songs.showAll()
        
    #============================SEARCH MUSIC BY ID============================
    def search(self,music_id):
        self.playlist_songs.search_by_id(music_id)
        
        
    def merge_by_year(self):
        self.years = self.playlist_songs.get_years() # O(n)
        # self.temp = [0] * len(self.years)
        self._counting_sort()
        self.playlist_songs.print_sorting(self.years)

    def _counting_sort(self):
        if not self.years:
            return

        min_year = min(self.years)
        max_year = max(self.years)
        
        count = [0] * (max_year - min_year + 1)
        
        for y in self.years:
            count[y - min_year] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        output = [0] * len(self.years)

        for i in range(len(self.years) - 1, -1, -1):
            year = self.years[i]
            idx = count[year - min_year] - 1
            output[idx] = year
            count[year - min_year] -= 1
        
        self.years = output