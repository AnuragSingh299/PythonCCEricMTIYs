def make_album(artist_name, title_name, no_of_tracks=None):
    album = {'artist': artist_name, 'title': title_name}
    if no_of_tracks:
        album['no_of_tracks'] = no_of_tracks
    return album

print(make_album('pink floyd', 'animals'))
print(make_album('alt-j', 'relaxer'))
print(make_album('queen', 'across the world', 10))
