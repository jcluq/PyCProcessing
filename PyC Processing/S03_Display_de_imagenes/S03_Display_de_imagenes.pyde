def setup():
    
    '''#### Display de imagenes
    #############################################################################################################################
    ### Processing puede usar imagenes guardadas e imprimirlas en la pantalla, primero cargaremos las imagenes con la funcion'loadImage.
    ### Le asignaremos a cada imagen una variable y las declararemos como variables globales, lo ideal es hacer este proceso en el setup
    ### ya que es un proceso que solo se realiza una vez.
    #############################################################################################################################'''
    
    global img_1,img_2,img_3,img_4,img_5,img_6
    size(600, 400)
    background(255,0,0)
    img_1 = loadImage("1.jpg")
    img_2 = loadImage("2.jpg")
    img_3 = loadImage("3.jpg")
    img_4 = loadImage("4.jpg")
    img_5 = loadImage("5.jpg")
    img_6 = loadImage("6.jpg")
    textSize(30)
    text('click para cambiar de imagen',50,height/2)

def draw():
    None
    
    '''#### 
    #############################################################################################################################
    ### Con el metodo mouseReleased(), activaremos la busqueda de una imagen y una frase aleatoria cada vez que se oprima y se suelte el mouse
    ### Usando el ejemplo de random de ejercicios anteriores, se seleccionara una imagen y una frase aleatoria
    ### Para imprimir a la imagen usaremos la funcion image()
    #############################################################################################################################'''
    
def mouseReleased(): 
    
    # Creamos 2 listas, una con las variables de las imagenes y otra con las posibles frases
    
    imagenes = [img_1,img_2,img_3,img_4,img_5,img_6]
    palabras = ['nadie_mirando','nosotrxs_alla','el_verso_aca','ella_riendo','tu_mirada_aca','un_espejo_aqui','misterios']
    
    # Con la funcion len() extraemos el dato de que tantos elementos hay dentro de cada lista y lo almacenamos en una variable
    
    numero_de_imagenes = len(imagenes)
    numero_de_palabras = len(palabras)
    
    # Con random() asignamos un valor aleatorio dentro del rango de cada lista 

    r_img = int(random(numero_de_imagenes))
    r_pal = int(random(numero_de_palabras))
    
    # En el momento de imprimir imagenes y frases llamamos a la lista y dentro de este '[ ]' usamos el valor aleatorio 'r_img' y 'r_pal'
    # para seleccioanar un objeto dentro de la lista
    
    image(imagenes[r_img],0,0)
    fill(255,0,0)
    textSize(80)
    text(palabras[r_pal],((width/2)-(textWidth(palabras[r_pal])/2)),height/2)

   
