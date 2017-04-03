#!/bin/bash

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

# Don't forget to edit the list of your Plist files below!
FILES="Info.plist
Info2.plist
StickerPack/Info.plist
Watch App/Info.plist
Watch App Extension/Info.plist"

for f in $FILES
do
	python3 xcode-build-increase.py "$f"
done

# restore $IFS
IFS=$SAVEIFS