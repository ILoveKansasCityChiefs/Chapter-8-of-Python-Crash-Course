def make_albums(artist_name, album_title):
    """Returning Info of Artists and Their Albums"""
    music = {'artist': artist_name, 'album': album_title}
    return music

while True:
    print("\nPlease add name of your artist and the title of one of their albums")
    print(("Enter 'q' to quit program"))

    user_artist = input("Please enter the artists name: ")
    if user_artist == 'q':
        break
    user_album = input("Please enter one of the artist's albums: ")
    if user_album =='q':
        break

    user_music = make_albums(user_artist, user_album)
    print(f"One of {user_artist}'s albums is {user_album}")
