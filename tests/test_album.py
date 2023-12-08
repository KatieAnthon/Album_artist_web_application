from lib.album import *


def test_album_class_works():
    album = Album(1,"Doolittle",1989,1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1


def test_equality():
    album1 = Album(1,"Doolittle",1989,1)
    album2 = Album(1,"Doolittle",1989,1)

    assert album1 == album2

def test_repr_():
    album = Album(2, "The Weekend", 1999, 2)
    assert str(album) == "Album(2, The Weekend, 1999, 2)"

