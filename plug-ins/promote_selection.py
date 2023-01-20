#!/usr/bin/env python

from gimpfu import *


def promote_selection(image, layer):

    if False == pdb.gimp_selection_is_empty(image):
        pdb.gimp_image_undo_group_start(image)

        pdb.gimp_floating_sel_to_layer(pdb.gimp_selection_float(layer, 0, 0))

        pdb.gimp_image_undo_group_end(image)

        pdb.gimp_displays_flush()

    return


register(
    "python_fu_promote_selection",
    "Promote current selection to new adjacent layer ",
    "Promote current selection to new adjacent layer ",
    "Ike Gingerich",
    "Ike Gingerich",
    "2016",
    "<Image>/Select/Promote Selection",
    "*",
    [
    ],
    [],
    promote_selection)

main()
