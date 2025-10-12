import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"

#auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#playlists = sp.user_playlists('mchpuskar')
#while playlists:
#    for i, playlist in enumerate(playlists['items']):
#        print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
#    if playlists['next']:
#        playlists = sp.next(playlists)
#    else:
#        playlists = None

sp.user_playlist_create("mchpuskar", name="alpine_marmot - 10/08/2025", public=True, collaborative=False, description="alpine_marmot show for DATE")
