from pydoc import visiblename
from clase_zombies import Zombi
from clase_jugadores import Personas
import os
print()
print("encabezado y reglas")
print()
nombre=str(input("por favor indique el nombre del jugador")).capitalize()

jugador=Personas(nombre)
horda=[]

for i in range (10):
    z=Zombi()
    horda.append(z)
#ojo que no comprendo porque no coloca el i en ninguna parte de ese bucle

while True: 
    
    os.system("cls")
    
    print(jugador.situacion())

    calles=[]
    for zombi in horda: 
        calles.append(zombi.calle)
    calles.sort()
    for elementos in calles:
        print(elementos,end="")
        print()

    if jugador.calle>40:
        print("has ganado")
        break

    perdido=False
    for zombi in horda: 
        if zombi.calle==jugador.calle:
            perdido=True
    if perdido:
        print("perdiste, te encontró el zombi")
        break

    velocidad=""
    
    while velocidad not in ("1","2","3"): 
        velocidad=str(input("cuanto desea correr? 1,2 o 3 cuadras, responda con números"))
    jugador.moverse(velocidad)


    for z in list(horda): 
        z.moverse()
        if z.no_visible():
            horda.remove(z)




    
