#!/usr/bin/env bash

GPUID=$1

CUDA_VISIBLE_DEVICES=$GPUID python main.py \
	--gpuid=$GPUID \
	--start-epoch=0 \
	--add-epochs=1000 \
	--save-every=1 \
	--gamma=0.75 \
	--hidden_size=16 \
	--start-learn-rate=1.0 \
	--decay-every=-1
