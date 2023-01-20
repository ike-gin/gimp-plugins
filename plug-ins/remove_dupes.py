#!/usr/bin/env python

from gimpfu import *

def add_text(image, txt):
	txtLayer = pdb.gimp_text_fontname(image, None, 0, 0, txt, 10, True, 24, PIXELS, "Sans")
	gimp.displays_flush()
	
	return

def compare_layers(image, l1, l2):
	l1p = l1.get_pixel_rgn(0, 0, l1.width, l1.height, False, False)
	l2p = l2.get_pixel_rgn(0, 0, l2.width, l2.height, False, False)

	return (l1p[0:l1.width, 0:l1.height] == l2p[0:l2.width, 0:l2.height])

def is_dupe_or_save(l):

	return "dupe" in pdb.gimp_item_get_name(l) or "save" in pdb.gimp_item_get_name(l)
	
def rem_dupes(image, layer):

	pdb.gimp_image_undo_group_start(image)

	layersToDelete = []
	nCompares = 0

	# progress bar constants and variables
	NUM_LAYERS = len(image.layers)
	curLayerProgress = 0
	
#	f = open(r"C:\Users\ike\AppData\Roaming\gimp-plugin-debug.txt", 'w')
	
	for l1 in image.layers:
		# update progress bars
		curProgressPct = float(curLayerProgress) / float(NUM_LAYERS)
		pdb.gimp_progress_update(curProgressPct)
		pdb.gimp_progress_set_text("Removing duplicate layers (layer " + str(curLayerProgress) + "/" + str(NUM_LAYERS) + ") " + str(int(curProgressPct * 100)) + "%")
		curLayerProgress += 1

		# confirm we will be comparing at least one unclassified layer
		if not is_dupe_or_save(l1):
			for l2 in image.layers:

				# no need to check layers already checked by the outer loops (giving us (n^2)/2 instead of n^2)
				if pdb.gimp_image_get_item_position(image, l2) > pdb.gimp_image_get_item_position(image, l1):
					nCompares += 1			
					if compare_layers(image, l1, l2):
						# don't add layers to the delete list that are already there
						if not is_dupe_or_save(l1):
							layersToDelete.append(l1)
						if not is_dupe_or_save(l2):
							layersToDelete.append(l2)

						# save one instance of groups of duplicate layers
						bNeedToSaveOne = not is_dupe_or_save(l1) and not is_dupe_or_save(l2)

						# never rename a "save" layer
						if "save" not in pdb.gimp_item_get_name(l1):
							pdb.gimp_item_set_name(l1, "save" if bNeedToSaveOne else "dupe")
						if "save" not in pdb.gimp_item_get_name(l2):
							pdb.gimp_item_set_name(l2, "dupe")

	for l in layersToDelete:
		if "save" not in pdb.gimp_item_get_name(l):
			image.remove_layer(l)

	add_text(image, "done, " + str(len(layersToDelete)) + " dupes, " + str(nCompares) + " compares");

	pdb.gimp_image_undo_group_end(image)
	
	gimp.displays_flush();

	return

register(
    "python_fu_remove_dupe_layers",
    "Remove Duplicate Layers",
    "Removes duplicate adjacent and non-adjacent layers from the image",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Layer/Remove Duplicate Layers",
	"*",
    [
    ],
    [],
    rem_dupes)

main()