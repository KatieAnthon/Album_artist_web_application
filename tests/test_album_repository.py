from lib.album_repository import *
from lib.album import *


def test_album_repository_works(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
    ]

def test_find_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = repo.find(1)
    assert album == Album(1, 'Doolittle', 1989, 1)


# test whether create inserts the new entry into albums

def test_create_method(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, "ABBA Gold", 1967, 5))
    album = repo.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'ABBA Gold', 1967, 5)
    ]

#test whether specified album id is removed from table

def test_delete_function(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.delete(2)
    album = repo.all()
    assert album == [
        Album(1, 'Doolittle', 1989, 1),
    ]
