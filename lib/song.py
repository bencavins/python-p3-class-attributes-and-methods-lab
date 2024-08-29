class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.increment_song_count()
        Song.add_artist(artist)
        Song.add_genre(genre)
        
    
    @classmethod
    def increment_song_count(cls):
        cls.count += 1

    @classmethod
    def add_artist(cls, artist):
        """Add artist to cls.artists if it doesn't already exist"""
        if artist not in cls.artists:
            cls.artists.append(artist)
        cls.update_artist_count(artist)
    
    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        Song.update_genre_count(genre)

    @classmethod
    def update_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1  # first instance of this genre
        else:
            cls.genre_count[genre] += 1  # increment the existing value
    
    @classmethod
    def update_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1  # create new key/value pair
        else:
            cls.artist_count[artist] += 1  # increment the existing value


s1 = Song('ironic', 'alanis morrisette', 'pop')
s1 = Song('ironic', 'alanis morrisette', 'pop')
s2 = Song('sk8r boi', 'avril lavigne', 'pop')


print(Song.count)
print(Song.artists)
print(Song.artist_count)
print(Song.genres)
print(Song.genre_count)
