class Song:
    def __init__(self,song, artist):
        self.artist = artist
        self.song = song
        self.tags = []
    def add_tags(self, *args):
        self.tags.extend(args)

song1 = Song('Ti ne odin', 'DDT')
song1.add_tags('Russian', 'Rock')

song2 = Song('Get lucky', 'Daft Punk')
song2.add_tags('French', 'Electronic')

print(song2.tags)
print(song2.tags is not song1.tags)