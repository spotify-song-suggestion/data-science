from json.decoder import JSONDecodeError
import json as simplejson

# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

#string_1 = {"external_urls":{"spotify":"https://open.spotify.com/artist/3fMbdgg4jU18AjLCKBhRSm"},"followers":{"href":null,"total":15507686},"genres":["pop","r&b","soul"],"href":"https://api.spotify.com/v1/artists/3fMbdgg4jU18AjLCKBhRSm","id":"3fMbdgg4jU18AjLCKBhRSm","images":[{"height":640,"url":"https://i.scdn.co/image/51dad9aaabe5643818840207a9a8957c2ad91bf2","width":640},{"height":320,"url":"https://i.scdn.co/image/2e6f35b90c131c137669d06e3c36b1a5d3172864","width":320},{"height":160,"url":"https://i.scdn.co/image/4ba613bd55b4954a027377b70b8c6d48639fd70b","width":160}],"name":"Michael Jackson","popularity":84,"type":"artist","uri":"spotify:artist:3fMbdgg4jU18AjLCKBhRSm"}

string2={"acousticness":0.725,"analysis_url":"https://api.spotify.com/v1/audio-analysis/6llUzeoGSQ53W3ThFbReE2","danceability":0.371,"duration_ms":413587,"energy":0.721,"id":"6llUzeoGSQ53W3ThFbReE2","instrumentalness":0.000139,"key":5,"liveness":0.349,"loudness":-9.952,"mode":0,"speechiness":0.0488,"tempo":92.481,"time_signature":4,"track_href":"https://api.spotify.com/v1/tracks/6llUzeoGSQ53W3ThFbReE2","type":"audio_features","uri":"spotify:track:6llUzeoGSQ53W3ThFbReE2","valence":0.673}

print(simplejson.dumps(string2, sort_keys=True, indent=4))


