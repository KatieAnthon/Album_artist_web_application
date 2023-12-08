from lib.album import Album


class AlbumRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums;')
        albums = []

        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        return albums
    
    def find(self, index):
        rows = self.connection.execute(
            'SELECT * FROM albums WHERE id=%s', [index]
            )
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # use create method
    # creates a new entry in the albums table 
    # side effects: returns None
    def create(self, new_album):
        self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES(%s, %s, %s)', [new_album.title, new_album.release_year, new_album.artist_id])
        return None

    # user delete method
    # deletes specified entry from albums table
    # side effects: returns None
    def delete(self, album_id):
        self.connection.execute('DELETE FROM albums WHERE id=%s', [album_id])
        return None