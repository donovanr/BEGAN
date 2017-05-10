#!/usr/bin/env bash

GPUID=$1
EPOCH=6

CUDA_VISIBLE_DEVICES=$GPUID python main.py \
	--gpuid=$GPUID \
	--start-epoch=$EPOCH \
	--train=0 \
	--add-epochs=0 \
	--hidden_size=16 \

