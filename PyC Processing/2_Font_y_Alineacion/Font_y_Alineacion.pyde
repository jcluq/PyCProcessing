########### TIPOGRAFIA Y ALINEADO ################


def setup():
    size(640, 360)
    
    """#### Tipografia
    #############################################################################################################################
    Para usar distintas tipografias en processing, debemos crear una variable de tipo de fuente, 
    cargarla con una fuente y asignarle esta al selector de fuentes.
    Para esto nos valdremos de diferentes herramientas:
    #############################################################################################################################"""
    
    
    # primero, miramos cuales fuentes tenemos disponibles, 
    # al correr este metodo, se imprimira un listado con las fuentes disponibles en la consola, ubicada en la parte inferior
    printArray(PFont.list())
    
    #creamos una variable y le asignamos el resultado de la funcion createFont
    #como primer parametro asignamos el nombre de la fuente, y como segundo parametro el tamano
    f = createFont("Ubuntu", 24)
    
    
    #Aplicamos la fuente a los textos que vamos a usar con la funcion textFont(), que recibe como parametro la variable que acabamos de crear.
    textFont(f)




def draw():
    background(102)
    
    """#### Alineacion
    #############################################################################################################################
    Podemos alinear la posicion del texto cambiando su punto de referencia respecto a sus cordenadas
    para esto usamos textAlign(), y los parametros RIGHT, CENTER y LEFT.
    #############################################################################################################################"""
    
    #La linea sirve para visualizar la mitad
    line(width/2,0,width/2,height)
    
    textAlign(RIGHT)
    text("Palabra",width/2,100)
    
    textAlign(CENTER)
    text("Palabra",width/2,150)
    
    textAlign(LEFT)
    text("Palabra",width/2,200)
