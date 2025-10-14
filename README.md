# playlists.py

### Generate a Spotify playlist from a list of songs.
These are scripts to:
- put list of songs collected from an endpoint (specifically an [Icecast](https://icecast.org) server) in a file
- generate a `uniq` list and put that in file `songs.txt`
- Create a playlist on Spotify and the songs in `songs.txt` to the playlist

### Format of `songs.txt` <a name="songs"></a>

The format of songs in the file should be:

``` 
Artist1 - Title1
Artist2 - Title2
Artist3 - Title3
```

See [songs.txt](https://github.com/puskar/playlists/blob/main/songs.txt) for an example

### Authorization
The script `playlists.py` uses the [spotipy](https://spotipy.readthedocs.io/) module and Spotify's OAuth2 authZ flow.

### Files

`crontab` - The crontab entries necessary to record a streamed radio show, create the podcast feed, and create the playlist

`make_playlist.sh` - Create the `songs.txt` file, source the file containing the Spotify credentials, and create Spotify playlist

`playlists.py` - Create the playlist and populate it with the songs from `songs.txt`

`songs.sh` - Get the songs from the [Icecast](https://icecast.org) server endpoint and do some munging of the returned value

`songs.txt` - The file containing a list artists and songs. See [above](#songs) for more info