#2 - Crear una clase que represente un vector de 3 dimensiones. Tenga 4 metodos que permitan las operaciones matematicas basicas (+,-,* y / por un escalar).
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return str(self.x)+"i "+str(self.y)+"j "+str(self.z)+"k"
    
    
    def sumar(a,b):
        
        x = (a.x + b.x)
        y = (a.y + b.y)
        z = (a.z + b.z)
        
        return vector(x,y,z)
    
    def restar(a,b):
        x = (a.x - b.x)
        y = (a.y - b.y)
        z = (a.z - b.z)
        
        return vector(x,y,z)
        
    def multiplicar(a,b):
        x=(a.y*b.z - b.y*a.z)
        y=-(a.x*b.z - b.x*a.z)
        z=(a.x*b.y - b.x*a.y)
        
        return vector(x,y,z)
        
    def dividir(a,c):
        c=float(c)
        x=a.x/c
        y=a.y/c
        z=a.z/c
        return vector(x,y,z) 

