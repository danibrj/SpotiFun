class Song:
    def __init__(self,music_name ,music_id,artist_name,year,rating,contents):
        self.music_name =music_name
        self.music_id =music_id
        self.artist_name = artist_name
        self.year =year
        self.rating =rating
        self.contents =contents
    
    def __str__(self):
        return f"Music: (name: '{self.music_name}',id: {self.music_id} ,artist: '{self.artist_name}' ,year: {self.year},rating: {self.rating} ,contents: {self.contents})"
    
    def __repr__(self):
        return self.__str__()