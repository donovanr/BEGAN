#!/usr/bin/env bash

# to run on eg GPU 2, use as:
#     bash run_BEGAN.sh 2 

GPUID=$1

CUDA_VISIBLE_DEVICES=$GPUID python main.py \
	--gpuid=$GPUID \
	--start-epoch=0 \
	--add-epochs=500 \
	--save-every=1 \
	--gamma=0.75 \
	--hidden_size=16 \
	--start-learn-rate=0.0001 \
	--decay-every=-1
