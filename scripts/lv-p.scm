(define (script-fu-lvp inImg)
	(define numLayers (car (gimp-image-get-layers inImg) ) )
	(define allLayers (vector->list (cadr (gimp-image-get-layers inImg) ) ) )
	(define activeLayerId (car (gimp-image-get-active-layer inImg) ) )
	(define activeLayerPos (car (gimp-image-get-item-position inImg activeLayerId) ) )

	(if (< activeLayerPos (- numLayers 1))
		(begin
			; determine "next" layer and set active layer to it
			(define nextLayerId (nth (+ activeLayerPos 1) allLayers) )
			(set! activeLayerId nextLayerId)
			
			; generate visibility mask based on the new active layer
			(define visibilityLayerMask (map (lambda(i) (if (= i activeLayerId) 1 0 ) ) allLayers ) )

			; tell gimp about the new active layer and all layer visibility
			(gimp-image-set-active-layer inImg activeLayerId)
			(map gimp-item-set-visible
				allLayers
				visibilityLayerMask)
			(gimp-displays-flush)
		)
	)
)

(script-fu-register
    "script-fu-lvp"
    "<Image>/Layer/lvp"
    "lvp"
    "Ike Gingerich"
    "Ike Gingerich"
    "2018"
    "*"
    SF-IMAGE    "Image" 0
)