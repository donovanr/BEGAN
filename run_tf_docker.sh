#!/usr/bin/env bash

nvidia-docker run -it \
	-p $1:$1 \
	-v $(pwd -P):/BEGAN_cells_128/BEGAN \
	rorydm/tf-began \
	bash
