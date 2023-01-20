#!/usr/bin/env python

from gimpfu import *


def layer_visible_next(image, layer):

    #   pdb.gimp_image_undo_group_start(image)

    layerPos = pdb.gimp_image_get_item_position(image, layer)

    if layer != image.layers[0]:
        nextLayer = image.layers[layerPos - 1]

        for lay in image.layers:
            lay.visible = False
        nextLayer.visible = True

        pdb.gimp_image_set_active_layer(image, nextLayer)

#   pdb.gimp_image_undo_group_end(image)

    pdb.gimp_displays_flush()

    return


register(
    "python_fu_layer_visible_next",
    "Makes the next layer exclusively visible",
    "Makes the next layer exclusively visible",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
    "<Image>/Layer/Layer Visible Next",
    "*",
    [
    ],
    [],
    layer_visible_next)

main()
