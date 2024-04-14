class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update song count
        Song.count += 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            Song.artists.append(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            Song.genres.append(genre)

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count

    @classmethod
    def get_genre_list(cls):
        return cls.genres

    @classmethod
    def get_artist_list(cls):
        return cls.artists
