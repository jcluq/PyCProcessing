########### MOVIMIENTO DEL MOUSE ################

def setup():
    size(800, 800)
    f = createFont("Arial", 24)
    textFont(f)

def draw():
    
    '''#### Movimiento del mouse
    #############################################################################################################################
    ### La posicion del mouse puede usarse como un dato para alterar parametros en nuestro codigo,
    ### podemos usar la posicion del mouse en X o Y para alterar el color y el tamaño del texto.
    ### Las funciones mouseX y mouseY guardan la posicion del mouse numericamente,
    ### podemos imprimir estos valores en consola respectivamente
    #############################################################################################################################'''
    
    mensaje_posicion = 'La posicion del mouse en X es: ' + str(mouseX) + ' posicion en Y es: ' + str(mouseY)
    
    print(mensaje_posicion)
    
    # Mensajes a ser imprimidos en pantalla:
    
    mensaje_movible = 'La posicion del mouse en Y \n cambia el tamaño ' 
    mensaje_estatico = 'LA POSICION DEL MOUSE TAMBIEN PUEDE ALTERAR \n EL COLOR DEL FONDO Y EL TEXTO' 
    
    '''####
    #############################################################################################################################
    ### En este caso como el tamaño del canvas es de 800x800 es necesario escalar los valores del mouse a unos mas pequeños
    ### para poder usarlos en el rango de color que maneja Processing .
    ### Usamos la funcion map() para escalar los valores,
    ### primero va el valor a ser escalado,
    ### seguido del rango que manejan los datos originales (desde 0 hasta la altura del canvas),
    ### y luego el valor al que se escalara ( de 0 a 255).
    ### Este nuevo valor escalado se le asigna a la variable "color_de_X" y "color_de_Y"
    #############################################################################################################################'''

    
    color_de_X = map(mouseX, 0, width, 0, 255)
    
    color_de_Y = map(mouseY, 0, height, 0, 255)
    
    
    #Estas nuevas variables son asignados al background y al fill del texto estatico
    
    background(255,color_de_X,color_de_Y)
    textSize(30)
    fill(color_de_X,color_de_Y - 50,color_de_Y)
    text(mensaje_estatico,height/2 - (textWidth(mensaje_estatico)/2),width/2) 
    
    # Al texto que va a estar moviendose asignamos directamente las variables de mouseY y mouseX sin escalar
    # Para este texto usaremos la posicion en Y del mouse para cambiar el tamaño del texto
    
    fill(0,0,0)
    textSize(mouseY/15)   
    
    # La posicion del texto seguira al mouse
    
    # Para que el texto este en el centro del mouse, la posicion en X del mouse se le restara 
    # la longitud del mismo texto divido 2'''  
    # la funcion mouseY se usara directamente
    
    text(mensaje_movible,mouseX - (textWidth(mensaje_movible)/2),mouseY) 
    
