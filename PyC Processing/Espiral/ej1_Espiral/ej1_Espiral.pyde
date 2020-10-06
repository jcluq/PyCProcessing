def setup():
    size(600,600)


def draw():

    texto = "                                                                        The coordinates are always rotated around their relative position to the origin. Positive numbers rotate objects in a clockwise direction and negative numbers rotate in the couterclockwise direction. Transformations apply to everything t"
    radius = 1.0
    espaciado = 12
    ##Rotamos desde el centro, en vez del (0,0)
    translate(width/2, height/2)
    for i in range(len(texto)):
        radius = radius + 0.5
        ## taken out because of non-constant spacing at large radius:
        ##rotate(0.5)
        ## this should give constant spacing, no matter the radius
        ## change 10 to some other number for a different spacing. 
        var = espaciado/radius
        
        rotate(-var)
        ## drawing at (0,radius) because were drawing onto a rotated canvas
        text(texto[i], 0, radius)
