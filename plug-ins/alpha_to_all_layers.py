#!/usr/bin/env python

from gimpfu import *
	
def alpha_to_all(image, layer):

	PROGRESS_UPDATE_THRESHOLD = len(image.layers)/25;
	curLayerProgress = 0

	for ly in image.layers:
		# update progress bars
		if curLayerProgress % PROGRESS_UPDATE_THRESHOLD == 0:
			pdb.gimp_progress_update(float(curLayerProgress) / float(len(image.layers)))
		curLayerProgress += 1
		
		pdb.gimp_layer_add_alpha(ly)
				
	gimp.displays_flush()

	return

register(
    "python_fu_add_alpha_to_all_layers",
    "Add an alpha channel to all layers",
    "Add an alpha channel to all layers",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Layer/Alpha to all layers",
	"*",
    [
    ],
    [],
    alpha_to_all)

main()