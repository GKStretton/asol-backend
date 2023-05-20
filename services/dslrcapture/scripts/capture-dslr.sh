#!/bin/bash
# Capture and save a DSLR photo to $1

set -e

gphoto2\
	--capture-image-and-download \
	--force-overwrite \
	--filename $1

chown 1000:1000 $1