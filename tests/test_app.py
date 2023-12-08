from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    

    
    div_tags = page.locator("p")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Albums")
    #expect(response).to_be_ok()
    expect(div_tags).to_contain_text([
        "Doolittle"
    ])
    expect(div_tags).to_contain_text([
        'Surfer Rosa'
    ])

    expect(div_tags).to_contain_text([
        'Released: 1988'
    ])

    expect(div_tags).to_contain_text([
        'Released: 1988'
    ])

def test_get_albums_for_1_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")

    p_tags = page.locator("p")
    expect(p_tags).to_have_text([
        "Release year: 1989",
        "Artist: Pixies"
        ])
    

"""
When i call  GET /albums a links for each album listed
hyperlinks that click through to correspondin albums id 
"""
def test_albums_hyperlinks(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")


    page.click("text='Doolittle'")
    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Album: Doolittle")


""" When i call GET/artists artists are listed"""

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    h1_tag = page.locator("h1")
    p_tag = page.locator("p")

    expect(h1_tag).to_contain_text("Artists")

    expect(p_tag).to_contain_text(['Pixies','ABBA','Taylor Swift','Nina Simone'])




""" When i call GET /artists/<id> I see a single artist and the artists details"""


def test_artists_information(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    p_tags = page.locator("p")
    expect(p_tags).to_contain_text(["Artist: Pixies"])
    expect(p_tags).to_contain_text(["Genre: Rock"])

""" From the artists page i can click through to the specific artist details"""

def test_artist_hyperlink(page,test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text='1'")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Pixies")








    
    


    



