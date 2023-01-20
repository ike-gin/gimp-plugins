#!/usr/bin/env python

from gimpfu import *
	
def shrink_layers(image, layer):

	pdb.gimp_image_undo_group_start(image)

#	f = open(r"C:\Users\ike\AppData\Roaming\gimp-plugin-debug.txt", 'wb')

	# progress bar constants and variables
	NUM_LAYERS = len(image.layers)
	PROGRESS_UPDATE_THRESHOLD = max(len(image.layers)/25, 1)
	curLayerProgress = 0

	for ly in image.layers:
		# update progress bars
		if curLayerProgress % PROGRESS_UPDATE_THRESHOLD == 0:
			pdb.gimp_progress_update(float(curLayerProgress) / float(NUM_LAYERS))
		curLayerProgress += 1

		# crop
		pdb.gimp_image_set_active_layer(image, ly)
		pdb.plug_in_autocrop_layer(image, ly)

		# move to upper left corner
		x_off, y_off = ly.offsets
		pdb.gimp_layer_translate(ly, -x_off, -y_off)

	pdb.gimp_image_undo_group_end(image)

	gimp.displays_flush()

	return

register(
    "python_fu_shrink_layers",
    "Autocrop and align all layers in upper left corner",
	"Autocrop and align all layers in upper left corner",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Layer/Shrink Layers",
	"*",
    [
    ],
    [],
    shrink_layers)

main()