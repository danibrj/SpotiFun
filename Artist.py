class Artist:
    def __init__(self,artist_name,artist_id):
        self.artist_name = artist_name
        self.artist_id = artist_id
        self.songs = []
    
    def insert_music(self,song):
        self.songs.append(song)
    
    
    def __str__(self):
        return f"Artist: (name : '{self.artist_name}', id : {self.artist_id}\n{self.songs})"

    def __repr__(self):
        return self.__str__()