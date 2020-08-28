# DS API for Best Beats : Spotify Song Suggester


## Search Spotify Suggester - Playlist Generator

<li>Use DS API - https://songsuggester-nyc.herokuapp.com/
<li>Access in Browser - https://songsuggester-nyc.herokuapp.com/suggest/ [fav_song]

<li>results = list(track, artist, danceability, instrumentalness, loadness, speechiness, valance)



## Search Spotify API for artist info

<li>Use DS API - https://songsuggester-nyc.herokuapp.com/
<li>Access in Browser - https://songsuggester-nyc.herokuapp.com/artist/ [input_artist]

<li>results = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist'])

## Search Spotify API for track info
<li>Use DS API - https://songsuggester-nyc.herokuapp.com
<li>Access in Browser - https://songsuggester-nyc.herokuapp.com/track/ [input_song]

<li>results = spotify.search(str(user_input_song), type="track", limit=1)


## Search Spotify API for albums

<li>Use DS API - https://songsuggester-nyc.herokuapp.com
<li>Access in Browser - https://songsuggester-nyc.herokuapp.com/albums/ [input_artist]

<li>results = spotify.artist_albums(artistID)