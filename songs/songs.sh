#!/bin/bash

set -x
cd ~/songs
curl -s https://wobc.stream/main.xspf | grep '<title>'  | uniq | sed 's#<title>##' | sed 's#</title>##' | tr \\r , | sed 's#      ##' >> tmpsongs
