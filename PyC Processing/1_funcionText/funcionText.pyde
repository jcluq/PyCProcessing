################Funcion text#####################



def setup():
    size(500, 500, P3D)

def draw():
    background(255)
    fill(0)
    
    ###String_______________________________________________________________________
    ### text(string, posicionX, posicionY)
    
    text("Esto es un String", 20, 20)
    
    
    ###Numero_______________________________________________________________________
    ### text(numero, posicionX, posicionY)
    
    text(12.10, 20, 60)
    
    
    ###Variable -> de tipo String o numerica________________________________________
    ### text(variable, posicionX, posicionY)

    f = "Esto es un string"
    text(f,20,100)
    

    ###Usamos "\n" para asignar saltos de linea________________________________________
    
    ejemplo = "Linea de arriba\nLinea de abajo"
    text(ejemplo,20,140)
    
    ###Podemos asignar el espacio en el que queremos disponer nuestro texto
    ###La caja roja es para demostrar ese espacio
    ### text(string, posX, posY, ancho, alto)________________________________________
    
    text(
    "Shasta is a delicious, and sometimes underrated, "
    "soft drink. I love it, and I drink it virtually "
    "every day. Yep.\n\nIf you don't like Shasta, then "
    "I don't like you.", 
    400, 12, 80, 300)
    
    stroke('#FF0000')
    noFill()
    rect(400, 12, 80, 300)
    
    ###Es posible asignar valores en el eje Z***
    ## text(numero, posicionX, posicionY,posicionZ)____________________________________
    
    text("Pence", width/2, height/2, 500 * cos(millis() / 300.0))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
