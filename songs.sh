#!/bin/bash

cd ~/workspace/github/puskar/playlists/
curl -s https://wobc.stream/main.xspf | grep '<title>'  | uniq | sed 's#<title>##' | sed 's#</title>##' | tr \\r , | sed 's#      ##' >> tmpsongs
