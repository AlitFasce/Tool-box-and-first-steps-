import random

class Personas:
    def __init__(self,nombre):
        self.nombre=nombre
        self.calle=1


    def moverse (self, velocidad):
        if velocidad=="1":
            self.calle+=1
        elif velocidad=="2":
            self.calle+=2
        else:
            self.calle+=3

    def situacion(self):
        return "el jugador {}, esta en la calle {}".format(self.nombre,self.calle)

    

