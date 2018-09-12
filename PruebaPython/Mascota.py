class Mascota:
    def __init__(self,raza,nombreMascota,peso,color):
        self.raza=raza
        self.nombreMascota=nombreMascota
        self.peso=peso
        self.color=color
    def __str__(self):
        print(self.raza+" "+self.nombreMascota+" "+str(self.peso)+" "+self.color)
