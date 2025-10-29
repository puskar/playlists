#!/bin/bash

set -x

cd  /home/puskar/workspace/github/puskar/playlists

uniq tmpsongs > songs.txt

. /home/puskar/workspace/github/puskar/playlists/secrets

~puskar/workspace/github/puskar/playlists/.venv/bin/python3 ~puskar/workspace/github/puskar/playlists/playlists.py

mv tmpsongs tmpsongs-lastweek
