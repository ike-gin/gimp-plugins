#!/usr/bin/env python

from gimpfu import *

def sheetify(image, layer):

	pdb.gimp_image_undo_group_start(image)

#	f = open(r"C:\Users\ike\AppData\Roaming\gimp-plugin-debug.txt", 'wb')

	# progress bar constants and variables
	NUM_LAYERS = len(image.layers)
	PROGRESS_UPDATE_THRESHOLD = max(len(image.layers)/25, 1)
	curLayerProgress = 0

	cur_h = 0
	cur_w = 0

	for ly in image.layers:
		# update progress bars
		if curLayerProgress % PROGRESS_UPDATE_THRESHOLD == 0:
			pdb.gimp_progress_update(float(curLayerProgress) / float(NUM_LAYERS))
		curLayerProgress += 1

		# move layer
		pdb.gimp_layer_translate(ly, cur_w, cur_h)

		# next column
		cur_w += (10 + ly.width)

		# next row?
		if curLayerProgress % 10 == 0:
			cur_h += 135
#			cur_h += 135
			cur_w = 0

	pdb.gimp_image_resize_to_layers(image)

	pdb.gimp_image_undo_group_end(image)
	gimp.displays_flush()

	return

register(
    "python_fu_sheetify",
    "Organize multiple layers onto a singlelayer",
	"Organize multiple layers onto a singlelayer",
    "Ike Gingerich",
    "Ike Gingerich",
    "2018",
	"<Image>/Layer/Sheetify Layers",
	"*",
    [
    ],
    [],
    sheetify)

main()