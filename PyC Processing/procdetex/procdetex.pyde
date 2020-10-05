####################Extraccion de substrings#####
#-Para este ejemplo, debemos crear un archivo de texto en la misma carpeta en la que se encuentra nuestro sketch
#-Presionamos CTRL + K o CMD + K y abrimos el archivo llamado texto.txt. Podemos cambiar el contenido de este archivo por uno de nuestra preferencia.
verso = ""
texto = ""

def setup():
    textMode(CENTER)
    textAlign(CENTER)
    global texto, verso
    size(600,400)
    #con este metodo cargamos el texto a un string
    
    texto = loadStrings("texto.txt")
    
    verso = ""
    
    for frase in texto:
        verso = verso + frase + "\n"
    
    
def draw():
    global verso
    background(120)
    text(verso,width/2,height/2) 
    
    
    
