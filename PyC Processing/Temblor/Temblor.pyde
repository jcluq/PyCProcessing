a = "Cuantas veces lo he visto por las sendas inutiles\nrecogiendo espejismos, como un lago estrellado!\nEs un dolor sentado mas alla de la muerte,\ndolor hecho de espigas y suenos desbandados."
x = 1
h = 2
def setup():

    size(500, 500, P3D)

def draw():
    global x
    global h
    background(255)
    fill(0)
    noStroke()
    textMode(CENTER)
    textAlign(CENTER,CENTER)
    textLeading(20)
    text(a,width/2+x,height/2)
    x = x + h
    
    if x>2 or x<-2:
        h=-h
                
        
