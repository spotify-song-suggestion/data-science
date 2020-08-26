# DS API for Best Beats : Spotify Song Suggester

## Search Spotify API for artist info

<li>https://songsuggester-nyc.herokuapp.com/
<li>https://songsuggester-nyc.herokuapp.com/artist/<input_artist>

<li>results = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist'])

## Search Spotify API for track info
<li>https://songsuggester-nyc.herokuapp.com
<li>https://songsuggester-nyc.herokuapp.com/track/<input_song>

<li>results = spotify.search(str(user_input_song), type="track", limit=1)


## Search Spotify API for albums

<li>https://songsuggester-nyc.herokuapp.com
<li>https://songsuggester-nyc.herokuapp.com/songsbyartist/<input_artist>

<li>results = spotify.artist_albums(artistID)