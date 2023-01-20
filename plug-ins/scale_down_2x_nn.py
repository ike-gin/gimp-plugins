#!/usr/bin/env python

from gimpfu import *
	
def scale_down_2x_nn(image, layer):

	pdb.gimp_context_set_interpolation(INTERPOLATION_NONE)
	pdb.gimp_image_scale(image, image.width*0.5, image.height*0.5)
		
	gimp.displays_flush()

	return

register(
    "python_fu_scale_down_2x_nn",
    "Quick image 0.5x scale using no interpolation",
    "Quick image 0.5x scale using no interpolation",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
	"<Image>/Image/Scale 0.5x NN",
	"*",
    [
    ],
    [],
    scale_down_2x_nn)

main()