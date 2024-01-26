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
        
        Song.add_song_to_count()
        # Song.count += 1
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)

    @classmethod
    def add_song_to_count(cls, song='song'):
        songs = []
        songs.append(song)
        Song.count += len(songs)
        # pass

    @classmethod
    def add_to_genres(cls, genre):
        if genre in Song.genres:
            Song.genre_count[genre] += 1

        else:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1

        # if genre not in Song.genres:
        #     Song.genres.append(genre)
        # # pass

    @classmethod
    def add_to_artists(cls, artist):
        if artist in Song.artists:
            Song.artist_count[artist] += 1

        else:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1

    def add_to_genre_count():
        return Song.genre_count

    def add_to_artist_count():
        return Song.artist_count