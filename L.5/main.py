import pgzrun
import random
import time

WIDTH=700
HEIGHT=500
TITLE="Sequence"

storesattelite=[]
sattelitepos=0
lines=[]
timr=0
timtaken=0
def on_mouse_down(pos): 
    global sattelitepos
    global lines
    if storesattelite[sattelitepos].collidepoint(pos):
        if sattelitepos:
           lines.append((storesattelite[sattelitepos-1].pos, storesattelite[sattelitepos].pos))
        sattelitepos=sattelitepos+1
        print(sattelitepos)
    else:
        lines=[]
        sattelitepos=0    


def drawsattelite():
    global timr
    for i in range(8):
        x=random.randint(50,600)
        y=random.randint(50,400)
        actor1 = Actor("satalite.png")
        actor1.pos=(x,y)
        storesattelite.append(actor1)
    timr=time.time()
       
def update():
    pass


def draw():
    screen.blit("bg.png", (0,0))
    labels = 1
    global timtaken
    if sattelitepos<=7:
       timtaken=time.time()-timr
       timtaken=round(timtaken,2)
       screen.draw.text(str(timtaken),(10,10),color="green",fontsize=50)
    else:
           screen.draw.text(str(timtaken),(10,10),color="green",fontsize=50)
    for i in storesattelite:
        i.draw()
        screen.draw.text(str(labels),(i.x,i.y+20),color="white",fontsize=25)
        labels=labels+1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")  
          

 




drawsattelite()
pgzrun.go() 