#!/usr/bin/env python

from gimpfu import *
	
def scale_2x_nn(image, layer):

	pdb.gimp_context_set_interpolation(INTERPOLATION_NONE)
	pdb.gimp_image_scale(image, image.width*2, image.height*2)
		
	gimp.displays_flush()

	return

register(
    "python_fu_scale_2x_nn",
    "Quick image 2x scale using no interpolation",
    "Quick image 2x scale using no interpolation",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Image/Scale 2x NN",
	"*",
    [
    ],
    [],
    scale_2x_nn)

main()