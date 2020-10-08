posY = 600

def setup():
    size(800,800)
def draw():
    global posY
    '''#### Teclado interaccion
    #############################################################################################################################
    ### Processing puede saber cuando se oprime una tecla , estas se pueden usar para activar acciones en nuestro codigo,
    ### las teclas tambien tienen un valor numerico y puede usarse esta identificacion para controlarlas
    #############################################################################################################################'''
    
    fill(0)
    textSize(20)
    text('oprima \ncualquier tecla \nmenos "s" \no flecha abajo',100,500)
    
    '''#### Teclado interaccion
    #############################################################################################################################
    ### Aca usamos la funcion keyPressed junto a un 'if', si se detecta alguna tecla siendo oprimida se resuelve lo que esta
    ### espaciado dentro del if, al igual que en el anterior ejemplo creamos una lista con los posibles mensajes y generamos 
    ### una funcion de aleatoridad para que imprima aleatoriamente uno, tambien se aleatoriza los colores del texto y el fondo 
    #############################################################################################################################'''
    
    if keyPressed:
        background(random(255),random(255),random(255))
        
        mensajes_al_oprimir = ['versos poeticos','cosas elocuentes',
                          'metafisica pura', 'belleza sintetizada','sublime metafora']

        numero_de_frases = len(mensajes_al_oprimir)
        r = int(random(numero_de_frases))


        fill(random(255),random(255),random(255))
        textSize(80)
        text(mensajes_al_oprimir[r],70,height/2)
        
    
        '''#############################################################################################################################
        ### Dentro del primer if encontramos mas condicionales, si alguna de las teclas oprimidas es B, imprimira la letra B,
        ### Las teclas minusculas y mayusculas tienen distinta identificacion numerica y por lo tanto se agregan las dos condicionales
        #############################################################################################################################'''
    
        
        if key == 's' or key == 'S':
            background(255)
            fill(0)
            textSize(800)
            text('S',220,600)
            
            '''#############################################################################################################################
            ### Segundo condicional dentro del primer if, si alguna de estas teclas es una tecla especial(ENTER,BACKSPACE, FLECHAS ETC)
            ### pasa al siguiente if, cada una de estas teclas tiene un codigo especial. Pasamos al if dentro de este
            ### si el codigo de esta tecla especial es DOWN (codigo que se usa para referenciar la tecla de flecha abajo), haga lo siguiente..
            ### usamos uno de los primeros codigos de movimiento para mover el texto impreso hacia abajo
            #############################################################################################################################'''
        
        elif key == CODED:
            if keyCode == DOWN :
                background(255,random(120),0)
                fill(random(255),random(255),random(255))
                textSize(800)
                text('??',200,posY)
                posY = posY + 20
                print(posY)
                if posY>800:
                    posY = 100

      
