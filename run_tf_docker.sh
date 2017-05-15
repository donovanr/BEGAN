#!/usr/bin/env bash

nvidia-docker run -it \
	-p $1:$1 \
	-v $(pwd -P):/BEGAN \
	rorydm/tf-began \
	bash
