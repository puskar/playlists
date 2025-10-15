import datetime
import html
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

### source the secrets file before running or you will get an auth error!

scope = "playlist-modify-public"

auth_manager=SpotifyOAuth(scope=scope)
#auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

user = 'mchpuskar'
show = "alpine_marmot"
today = datetime.date.today()

playlist_name = f"{show} - {today:%m/%d/%Y}"

plout = sp.user_playlist_create(user, name=playlist_name, public=True, collaborative=False, description=f"{show} music playlist for {today:%m/%d/%Y}")
plid = plout['id']
pl_url = plout['external_urls']['spotify']

with open("/tmp/playlist_url", "w") as urlfile:
  urlfile.write(pl_url)

def read_songs(song_file):
    with open(song_file, 'r') as f:
        songs = f.readlines()
    songs = [html.unescape(song.strip()) for song in songs]
    return songs


def get_track_id(track):
    results = sp.search(q=track, limit=1)
    items = results['tracks']['items']
    if items:
        track_id = items[0]['uri']
        return track_id
    else:
        return None


# use the return value from the user_playlist_create call instead of this function
def get_playlist_id(plname):
    pl = sp.user_playlists(user, limit=50)
    for list in pl['items']:
        if list['name'] == playlist_name:
            playlist_id = list['id']
            break
    return playlist_id

#plid = get_playlist_id(playlist_name)

songlist = read_songs('songs.txt')

tracks=[print(f'Adding {s} to the list') or get_track_id(s) for s in songlist]

sp.playlist_add_items(plid, tracks)
