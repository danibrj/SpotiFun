class Song:
    def __init__(self,music_name ,music_id,year,rating,contents):
        self.music_name =music_name
        self.music_id =music_id
        self.year =year
        self.rating =rating
        self.contents =contents
    
    def __str__(self):
        return f"Music: (name: '{self.music_name}',id: {self.music_id} ,year: {self.year} ,contents: {self.contents})"
    def __repr__(self):
        return self.__str__()