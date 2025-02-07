class MusicManager():
    
    def __init__(self):
        self.tracks = []

    def view_tracks(self):
        return self.tracks
    
    def add(self, track):
        if type(track) != str:
            raise Exception('Error: track must be a string with more than 1 char')
        if track == '':
            raise Exception('Error: track must be a string with more than 1 char')
        self.tracks.append(track)