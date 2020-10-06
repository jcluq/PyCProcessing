######## MOVIMIENTO #########

posicion = 100 #posicion inicial en X
velocidad = 2 #velocidad de desplazamiento en X
posX = 100

def setup():
    size(500, 500, P3D)
    textAlign(CENTER)
def draw():
    global posX, posicion, velocidad
    background(255)
    fill(0)
    
    
    
    """#### Movimiento unidireccional
    #############################################################################################################################
    ###En el movimiento unidireccional, buscamos que el objeto se desplace hacia una direccion hasta un posible limite
    ###En ese limite podemos colocar nuevas condiciones, tal como posicionar el objet en la posicion inicial.
    #############################################################################################################################"""
    
    text("Derecha",posX, 400)
    posX = posX + 5
    if posX>500:
        posX = 100
    
    
    
    
        
    """#### Movimiento oscilatorio
    #############################################################################################################################
    ### En este ejemplo, tomamos una posicion inicial llamada posicion(100) y sumamos una variable llamada velocidad(2) 
    ### esto hara que la posicion aumente en cada iteracion (100+2 = 104) + 2 = 106)...etc
    ### Cuando posicion sea superior a 200, velocidad se multiplicara por -1 (velocidad = 2 * -1 = -2)
    ### Al sumar velocidad a posicion, hara que posicion diminuya (posicion = 200 +(-2) = 198 +-2 = 196...) 
    ### posicion disminuira hasta ser menor que 100, donde velocidad se vuelve a multiplicar por -1 (velocidad = -2*-1 = 2)
    ### Esto hara que el valor de posicion vuelva a incrementar en cada iteracion, generando asi un movimiento oscilatorio.
    #############################################################################################################################"""
    
    posicion = posicion + velocidad
    
    if posicion > 200:
        velocidad = velocidad * -1
    if posicion <100:
        velocidad = velocidad * -1
        
    text("horizontal",posicion,100)
    text("Vertical",100,posicion)
    text("Diagonal",posicion,posicion)

    
    
    """### Movimiento oscilatorio con radianes (circular)
    #############################################################################################################################
    ### Podemos asignar oscilaciones con radianes, valiendonos de un numero que cambie de manera lineal.
    ### Usamos la funcion millis(), la cual guarda la cantidad de milisegundos desde la ejecucion del programa
    ### e implementamos 
    ### obtenemos un movimiento diagonal.
    ### 
    ### ***posicion y posicionY son las mismas variables del ejemplo pasado,
    ### al tener limites distintos, la direccion de la velocidad no siempre es la misma para ambos ejes, 
    ### lo que genera el efecto de rebotar en los bordes de un rectangulo
    #############################################################################################################################"""
    
    
    y = 100 * sin(radians(millis()/10))+width/2
    x = 100 * cos(radians(millis()/10))+height/2
    
    text("Circular",x,y)
    
    
