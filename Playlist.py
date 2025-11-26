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
        self.years = self.playlist_songs.get_years()
        self.temp = [0] * len(self.years)
        self._merge_sort(0,len(self.years)-1)
        

    def _merge_sort(self,left,right):
        if left >= right:
            return 
        mid = (left + right) // 2
        self._merge_sort(left,mid)
        self._merge_sort(mid+1 ,right)

        i = left
        j = mid +1
        k = left
        while i <= mid and j <= right:
            if self.years[i][0] <= self.years[j][0]:
                self.temp[k] = self.years[i]
                i += 1
            else:
                self.temp[k] = self.years[j]
                j += 1
            k += 1

        while i <= mid:
            self.temp[k] = self.years[i]
            i += 1
            k += 1
        while j <= right:
            self.temp[k] = self.years[j]
            j += 1
            k += 1
            
        for i in range(left,right+1):
            self.years[i] = self.temp[i]
    # def merge(self,years):
        
        
