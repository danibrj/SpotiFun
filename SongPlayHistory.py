from Stack import Stack
class SongPlayHistory:
    def __init__(self):
        self.history_songs = Stack()
    
    def play_song(self,song):
        print(f"song '{song.music_name}' was played")
        self.history_songs.push(song)
    
    def show_undo(self):
        self.history_songs.search_for_undo()
        