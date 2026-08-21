def make_albums(artist_name, album_title):
    """Returning Info of Artists and Their Albums"""
    music = {'artist': artist_name, 'album': album_title}
    return music

kendrick = make_albums('Kendrick Lamar', 'DAMN')
print(kendrick)

drake = make_albums('Drake', 'Ice Man')
print(drake)

nle_choppa = make_albums('NLE Choppa', 'Top Shotta')
print(nle_choppa)
