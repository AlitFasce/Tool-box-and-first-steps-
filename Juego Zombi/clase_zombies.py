import random

class Zombi:
    def __init__(self):
        self.calle=random.randint(10,20)
        self.direccion=random.choice (["izquierda","derecha"])
        self.velocidad=random.randint(1,3)

    def moverse (self):
        if self.direccion=="izquierda":
            self.calle-=self.velocidad
        else: 
            self.calle+=self.velocidad
    
    def no_visible(self):
        if self.calle <0 or self.calle>40:
            return True
        else:
            return False