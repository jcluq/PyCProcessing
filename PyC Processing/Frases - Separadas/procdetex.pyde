####################Extraccion de substrings#####
#-Para este ejemplo, debemos crear un archivo de texto en la misma carpeta en la que se 
#-encuentra nuestro sketch
#-Presionamos CTRL + K o CMD + K y abrimos el archivo llamado texto.txt. 
#-Podemos cambiar el contenido de este archivo por uno de nuestra preferencia.
verso = ""
texto = ""
tam_letras = 18


def setup():
    global texto
    textMode(CENTER)
    textAlign(CENTER)
    textSize(tam_letras)
    size(800,400)
    #con este metodo cargamos el texto a un string
    
    texto = loadStrings("texto.txt")
    

    
    
def draw():
    global verso, texto
    background(10,0,120)
    
    
    
    ### Determinamos el centro de nuestro texto para posicionarlo en el centro de la pantalla:
    centroX = width/2
    ### la posicion central en el eje Y es igual al numero de renglones,
    ### multiplicado por el tamaño de las letras
    ### dividido en dos 
    pos_central = ( (len(texto) + 1 ) * tam_letras )/ 2.0
    
    ### restamos a la posicion centroY la posicion del centro de nuestro texto:
    centroY = (height/2) - pos_central
    
    for ind, frase in enumerate(texto):
    
        fill(random(255),random(255),random(255)) # asingamos un color al azar
        
        
        ##el centro en Y para cada frase es disinto, y corresponde a la cantidad de frases pasadas x el tamaño de las letra
        centroy_frase = centroY+(ind*tam_letras) 
        
        ## ponemos el texto
        text(frase,centroX,centroy_frase) 
        
        ##un delay para reducir la velocidad de iterado
        delay(20)
    
    
    
    
    
    
    
