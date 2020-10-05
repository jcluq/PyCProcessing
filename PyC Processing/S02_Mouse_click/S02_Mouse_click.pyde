def setup():
    size(800, 800)
    background(255,0,0)

def draw():
    
    '''#### Mouse Click
    #############################################################################################################################
    ### Processing puede saber cuando se hace click y cuando se suelta el boton del mouse,estas acciones pueden ser usadas
    ### para activar condiciones en nuestro codigo, para esto usamos la funcion mousePressed y el metodo mouseReleased(): 
    #############################################################################################################################'''
    
    #Declaramos las variables color_de_X y color_de_Y como variables globales para poder usarlas en cualquier parte del codigo
    
    global color_de_X,color_de_Y
    
    #Como en el anterior ejercicio, mapeamos los valores del mouse a los valores usados en color y les asignamos a las variables globales
    
    color_de_X = map(mouseX, 0, height, 0, 255)
    color_de_Y = map(mouseY, 0, width, 0, 255)
    
    '''####
    #############################################################################################################################
    ### MousePressed junto a 'if' funcionan como un condicional, si se oprime el mouse ocurre lo que este abajo
    #############################################################################################################################'''
    
    if mousePressed:
        fill(255,color_de_X,color_de_Y)
        textSize(60)
        text('oprimido',mouseX,mouseY) 
        # Se imprimen 2 veces el mismo texto para darle el efecto de sombra, una se imprime en negro y el otro con colores
        fill(0)
        text('oprimido',mouseX,mouseY) 
         
    # Mientras no se este oprimiendo el mouse se activara aquello que esta debajo del 'else'
    else:
        fill(0)
        textSize(60)
        text('suelto',mouseX,mouseY)
        fill(color_de_Y,255,0)
        text('suelto',mouseX,mouseY) 
    
'''#### Mouse Click
    #############################################################################################################################
    ### mouseReleased es un metodo al igual que lo es 'draw', se activa cada vez que soltemos el boton del mouse
    ### Las variables color_de_X y color_de_Y se establecieron arriba  como globales para poder usarlas aca
    #############################################################################################################################'''

def mouseReleased(): 
    
    # Lista de posibles mensajes que se imprimiran cuando se  suelte el mouse
    
    mensajes_al_soltar = ['soltaste \n el \n mouse','no \n sueltes \n el mouse',
                          'por que \n sueltas \n el mouse \n ??????', 'soltaste \n soltaste \n soltaste \n']
    
    # La funcion 'len' extrae el numero de mensajes que hay en una lista' y guarda este valor en la variable numero_de_frases
    
    numero_de_frases = len(mensajes_al_soltar)
    
    # con la funcion 'random' la variable 'r' toma un valor aleatorio entre el numero de mensajes en la lista
    
    r = int(random(numero_de_frases))
    
    #Vuelve a imprimir el fondo para limpiar lo dibujado, las variables de color tomaran los datos del momento en que soltamos el mouse
    
    background(255,color_de_Y,color_de_X)
    fill(0)
    textSize(100)
    
    # Cuando imprime el texto, selecciona un mensaje aleatorio 'r' entre la lista de mensajes de arriba
    
    text(mensajes_al_soltar[r],height/2 - (textWidth(mensajes_al_soltar[r])/2),250)
