#1 - Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas (+,-,*,/).
class imaginario:
    def __init__(self, r, j):
        self.r=r
        self.j=j

    def __str__(self):
        if self.j > 0:
            return str(self.r)+" + j"+str(self.j)
        else:
            return str(self.r)+" - j"+str(abs(self.j))

    def sumar(a,b):
        ar = a.r
        aj = a.j
        br = b.r
        bj = b.j
        cr = ar+br
        cj = aj+bj
        
        return imaginario(cr,cj)
    
    
    
    def restar(a,b):
        ar = a.r
        aj = a.j
        br = b.r
        bj = b.j
        cr = ar-br
        cj = aj-bj
        
        return imaginario(cr,cj)
            
    def multiplicar(a,b):
        ar = a.r
        aj = a.j
        br = b.r
        bj = b.j
        cr = (ar*br - aj*bj)
        cj = (ar*bj + aj*br)
        
        return imaginario(cr,cj)

    
    def dividir(a,b):
        ar = a.r
        aj = a.j
        br = b.r
        bj = b.j
        cr = (ar*br + aj*bj)/(br*br + bj*bj)
        cj = (aj*br - ar*bj)/(br*br + bj*bj)
        
        return imaginario(cr,cj)



