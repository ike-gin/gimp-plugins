#!/usr/bin/env python

from gimpfu import *
	
def reset_layer_names(image, layer):

	# progress bar constants and variables
	NUM_LAYERS = len(image.layers)
	PROGRESS_UPDATE_THRESHOLD = len(image.layers)/25;
	curLayerProgress = 0

	for ly in image.layers:
		# update progress bars
		if curLayerProgress % PROGRESS_UPDATE_THRESHOLD == 0:
			pdb.gimp_progress_update(float(curLayerProgress) / float(NUM_LAYERS))
		curLayerProgress += 1

		pdb.gimp_item_set_name(ly, "Layer " + str(curLayerProgress-1))
		
	gimp.displays_flush()

	return

register(
    "python_fu_reset_layer_names",
    "Resets layer names to their current layer index",
	"Resets layer names to their current layer index",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Layer/Reset Layer Names",
	"*",
    [
    ],
    [],
    reset_layer_names)

main()