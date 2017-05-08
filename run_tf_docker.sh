#!/usr/bin/env bash

nvidia-docker run -it \
	-p $1:$1 \
	-v $(pwd -P):/BEGAN_cells \
	rorydm/tf-began \
	bash
