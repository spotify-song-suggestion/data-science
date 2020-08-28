from json.decoder import JSONDecodeError
import json as simplejson

# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

#string_1 = {"external_urls":{"spotify":"https://open.spotify.com/artist/3fMbdgg4jU18AjLCKBhRSm"},"followers":{"href":null,"total":15507686},"genres":["pop","r&b","soul"],"href":"https://api.spotify.com/v1/artists/3fMbdgg4jU18AjLCKBhRSm","id":"3fMbdgg4jU18AjLCKBhRSm","images":[{"height":640,"url":"https://i.scdn.co/image/51dad9aaabe5643818840207a9a8957c2ad91bf2","width":640},{"height":320,"url":"https://i.scdn.co/image/2e6f35b90c131c137669d06e3c36b1a5d3172864","width":320},{"height":160,"url":"https://i.scdn.co/image/4ba613bd55b4954a027377b70b8c6d48639fd70b","width":160}],"name":"Michael Jackson","popularity":84,"type":"artist","uri":"spotify:artist:3fMbdgg4jU18AjLCKBhRSm"}

string2={"acousticness":0.725,"analysis_url":"https://api.spotify.com/v1/audio-analysis/6llUzeoGSQ53W3ThFbReE2","danceability":0.371,"duration_ms":413587,"energy":0.721,"id":"6llUzeoGSQ53W3ThFbReE2","instrumentalness":0.000139,"key":5,"liveness":0.349,"loudness":-9.952,"mode":0,"speechiness":0.0488,"tempo":92.481,"time_signature":4,"track_href":"https://api.spotify.com/v1/tracks/6llUzeoGSQ53W3ThFbReE2","type":"audio_features","uri":"spotify:track:6llUzeoGSQ53W3ThFbReE2","valence":0.673}

string3={'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/162DCkd8aDKwvjBb74Gu8b'}, 'href': 'https://api.spotify.com/v1/artists/162DCkd8aDKwvjBb74Gu8b', 'id': '162DCkd8aDKwvjBb74Gu8b', 'name': 'Weather Report', 'type': 'artist', 'uri': 'spotify:artist:162DCkd8aDKwvjBb74Gu8b'}], 'available_markets': ['AD', 'AE', 'AL', 'AR', 'AT', 'AU', 'BA', 'BE', 'BG', 'BH', 'BO', 'BR', 'BY', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'KZ', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MD', 'ME', 'MK', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SE', 'SG', 'SI', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'UA', 'US', 'UY', 'VN', 'XK', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/03CBiPwr9yFsSNtFv5HK7Y'}, 'href': 'https://api.spotify.com/v1/albums/03CBiPwr9yFsSNtFv5HK7Y', 'id': '03CBiPwr9yFsSNtFv5HK7Y', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273672c04454aafc5169a9a0473', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02672c04454aafc5169a9a0473', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851672c04454aafc5169a9a0473', 'width': 64}], 'name': 'Mr. Gone', 'release_date': '1978-04-17', 'release_date_precision': 'day', 'total_tracks': 10, 'type': 'album', 'uri': 'spotify:album:03CBiPwr9yFsSNtFv5HK7Y'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/162DCkd8aDKwvjBb74Gu8b'}, 'href': 'https://api.spotify.com/v1/artists/162DCkd8aDKwvjBb74Gu8b', 'id': '162DCkd8aDKwvjBb74Gu8b', 'name': 'Weather Report', 'type': 'artist', 'uri': 'spotify:artist:162DCkd8aDKwvjBb74Gu8b'}], 'available_markets': ['AD', 'AE', 'AL', 'AR', 'AT', 'AU', 'BA', 'BE', 'BG', 'BH', 'BO', 'BR', 'BY', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'KZ', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MD', 'ME', 'MK', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SE', 'SG', 'SI', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'UA', 'US', 'UY', 'VN', 'XK', 'ZA'], 'disc_number': 1, 'duration_ms': 413586, 'explicit': False, 'external_ids': {'isrc': 'USSM10023515'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6llUzeoGSQ53W3ThFbReE2'}, 'href': 'https://api.spotify.com/v1/tracks/6llUzeoGSQ53W3ThFbReE2', 'id': '6llUzeoGSQ53W3ThFbReE2', 'is_local': False, 'name': 'Young and Fine', 'popularity': 28, 'preview_url': 'https://p.scdn.co/mp3-preview/eb9487d82beab3e1f7eb2763919cfc79fb9d0478?cid=3da84aa1068b4f46bd133c1927bccf89', 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:6llUzeoGSQ53W3ThFbReE2'}



print(simplejson.dumps(string3, sort_keys=True, indent=4))

