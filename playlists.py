import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import html

scope = "playlist-modify-public"

auth_manager=SpotifyOAuth(scope=scope)
#auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

#sp.user_playlist_create("mchpuskar", name="alpine_marmot - 10/08/2025", public=True, collaborative=False, description="alpine_marmot show for DATE")

user = 'mchpuskar'

def read_songs(song_file):
    with open(song_file, 'r') as f:
        songs = f.readlines()
    songs = [html.unescape(song.strip()) for song in songs]
    return songs


def get_track_id(track):
    results = sp.search(q=track, limit=1)
    items = results['tracks']['items']
    track_ids = []
    if items:
        track_id = items[0]['uri']
        track_ids.append(track_id)
        return track_ids
    else:
        return None
        
def get_playlist_id(plname):
    pl = sp.user_playlists(user, limit=50)
    for list in pl['items']:
        if list['name'] == 'alpine_marmot - 10/08/2025':
            playlist_id = list['id']
            break
    return playlist_id

plid = get_playlist_id('alpine_marmot - 10/08/2025')

songlist = read_songs('songs.txt')

for s in songlist:
    tracks = get_track_id(s)
    if tracks:
        print(f'Adding {s} to playlist')
        #sp.playlist_add_items(plid, tracks)
    else:
        print(f'Could not find {s} on Spotify')
