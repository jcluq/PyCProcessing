######COLORES#############




def setup():
    size(500,500)
    
def draw():
    
    
    """#### Fondo
    #############################################################################################################################
    ### El color del fondo lo definimos despues de la funcion draw
    ### El metodo a usar es: background()
    #############################################################################################################################"""
    
    ###Definimos el fondo, un solo paramtero es una escala de grises, 0 es negro, 255 es blanco, prueba cambiar el numero uno en este rango
    background(120)
    
    """#### Relleno
    #############################################################################################################################
    ### Para cambiar el color de las letras, cambiaremos el elemento de relleno, 
    ### esto cambiara el color de rleleno de todas las figuras creadas, inculuidas las letras
    ### El metodo a usar es: Fill()
    #############################################################################################################################"""
   
   
    #un parametro asigna un color a escala de grises
    fill(0) #reseteamos a 0
    text("soy el color predeterminado",20,30)
    
    #si usamos dos parametros, el segundo equivale a la opacidad
    fill(0,100)
    text("Soy negro, con mi opacidad disminuida",20,60)
    
    
    #Podemos usar tres parametros para asignar escalas de rojo, verde y azul (R,G,B),
    #cada color puede tener un valor de minimo cero y maximo 255
    #prueba cambiando algunos numeros de las funciones fill()
    
    fill(255,0,0) 
    text("soy rojo",20,90)
    
    fill(0,255,0) 
    text("soy verde",20,120)
    
    fill(0,0,255) 
    text("soy azul",20,150)
    
    #si agregamos un cuarto parametro, funcionara como opacidad para los colores
    fill(0,0,255,80)
    text("soy azul, con opacidad reducida",20,180)
    
    #tambien podemos asignar colores con codigo hexadecimal ***el valor se asigna como string
    
    fill("#3DE0DC")
    text("soy #3DE0DC",20,210)
    
    #el color de relleno no cambiara hasta que volvamos a cambiarlo
    #por eso al inicio de esta seccion, reseteamos el valor de fill() a 0
    
    
    
    
    
    
    
