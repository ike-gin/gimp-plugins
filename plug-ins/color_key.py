#!/usr/bin/env python

from gimpfu import *
	
def color_key(image, layer):

#	f = open(r"C:\Users\ike\AppData\Roaming\gimp-plugin-debug.txt", 'wb')

	pdb.gimp_image_undo_group_start(image)

	# progress bar constants and variables
	NUM_LAYERS = len(image.layers)
	PROGRESS_UPDATE_THRESHOLD = max(len(image.layers)/25, 1)
	curLayerProgress = 0

	pdb.gimp_context_set_brush("Pixel (1x1 square)")
	pdb.gimp_context_set_brush_size(max(image.height, image.width))
	pdb.gimp_context_set_sample_threshold(0.0)

	for ly in image.layers:
		# update progress bars
		if curLayerProgress % PROGRESS_UPDATE_THRESHOLD == 0:
			pdb.gimp_progress_update(float(curLayerProgress) / float(NUM_LAYERS))
		curLayerProgress += 1
		
		pdb.gimp_layer_add_alpha(ly)

		pdb.gimp_selection_none(image)
#		pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, ly, (248, 0, 248))
#		pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, ly, (230, 0, 230))
#		pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, ly, (247, 0, 247))
#		pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, ly, (0, 255, 0))
		pdb.gimp_image_select_color(image, CHANNEL_OP_ADD, ly, (255, 255, 255))


		pdb.gimp_eraser(ly, 2, [ly.width/2,ly.height/2], 0, 1)
		
	pdb.gimp_image_undo_group_end(image)

	gimp.displays_flush()

	return

register(
    "python_fu_color_key",
    "Replace a color with alpha for all layers",
    "Replace a color with alpha for all layers",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Layer/Color Key",
	"*",
    [
    ],
    [],
    color_key)

main()