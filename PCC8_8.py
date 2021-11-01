def make_album(artist_name, title_name):
    album = {'artist': artist_name, 'title': title_name}
    return album

while True:
    print("\nEnter artist name and title of the album:")
    print("\nEnter q to quit")

    artist_n = input("Enter artist name:")
    if artist_n == 'q':
        break

    album_t = input("Enter album name:")
    if album_t == 'q':
        break

    album_detail = make_album(artist_n, album_t)
    print(f"Album details: {album_detail}")
    
    
    
    
