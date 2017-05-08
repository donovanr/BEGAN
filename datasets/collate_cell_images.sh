#!/usr/bin/env bash

DIR="2d_aligned_v2/"
mkdir -p "$DIR"

for image in $HOME/2d_images/*/*.ome.tif_flat.png; do
        cp "$image" "$DIR"
done

