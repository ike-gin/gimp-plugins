; TODO: test undo groups, and if script operates fast enough to not corrupt undo state

(define (script-fu-next-layer-visible inImg)
    (let* 
        ( 
            (layers       (cadr (gimp-image-get-layers inImg) ) )
            (numLayers    (car (gimp-image-get-layers inImg) ) )
			(curLayer	  (car (gimp-image-get-active-layer inImg) ) )
			(curLayerPos  (car (gimp-image-get-layer-position inImg curLayer ) ) )
			(nextLayerPos (- curLayerPos 1) )
        )

		; if not past end of layer list
		(if (< -1 nextLayerPos)
			(begin

				; set next layer as the active layer
				(gimp-image-set-active-layer inImg (aref layers nextLayerPos ) )
				
				; set all layers invisible
				(let loop ((lay 0))
					(if (< lay numLayers)
						(begin
							(gimp-item-set-visible (aref layers lay) FALSE)
							(loop (+ lay 1) )
						)
					)
				)

				; set newly active layer visible
				(gimp-item-set-visible (aref layers nextLayerPos)  TRUE)
				
				; redraw
				(gimp-displays-flush)
			)
		)
	)
)

(script-fu-register
    "script-fu-next-layer-visible"
    "<Image>/Layer/Next Layer Visible"
    "svis"
    "Ike Gingerich"
    "Ike Gingerich"
    "2018"
    "*"
    SF-IMAGE    "Image" 0
)