# DS API for Best Beats : Spotify Song Suggester

## Search Spotify API for artist info

https://songsuggester-nyc.herokuapp.com/
https://songsuggester-nyc.herokuapp.com/artist/<input_artist>

results = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist'])

## Search Spotify API for track info
https://songsuggester-nyc.herokuapp.com
https://songsuggester-nyc.herokuapp.com/track/<input_song>

results = spotify.search(str(user_input_song), type="track", limit=1)


## Search Spotify API for albums
https://songsuggester-nyc.herokuapp.com
https://songsuggester-nyc.herokuapp.com/songsbyartist/<input_artist>

results = spotify.artist_albums(artistID)