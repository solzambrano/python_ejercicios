from vector import vector
#3- Crear una clase que represente una matriz de 3x3 dimensiones. Tengan 3 metodos que permitan las operaciones matematicas basicas (excluimos la division) (+ y - entre matrices, * solo por un vector).
# La matriz se crea a partir de vectores creados desde vector.
class matriz:
    def __init__(self,a,b,c):
        self.ax=a.x
        self.ay=a.y
        self.az=a.z
        self.bx=b.x
        self.by=b.y
        self.bz=b.z
        self.cx=c.x
        self.cy=c.y
        self.cz=c.z
    
    def __str__(self):
        return f"""|{self.ax} {self.ay} {self.az}|
|{self.bx} {self.by} {self.bz}|
|{self.cx} {self.cy} {self.cz}|"""


    def sumar(a,b):
        rax = (a.ax + b.ax)
        ray = (a.ay + b.ay)
        raz = (a.az + b.az)
        rbx = (a.bx + b.bx)
        rby = (a.by + b.by)
        rbz = (a.bz + b.bz)
        rcx = (a.cx + b.cx)
        rcy = (a.cy + b.cy)
        rcz = (a.cz + b.cz)
        return matriz(vector(rax,ray,raz),vector(rbx,rby,rbz), vector(rcx,rcy,rcz))
        
        
    def restar(a,b):
        rax = (a.ax - b.ax)
        ray = (a.ay - b.ay)
        raz = (a.az - b.az)
        rbx = (a.bx - b.bx)
        rby = (a.by - b.by)
        rbz = (a.bz - b.bz)
        rcx = (a.cx - b.cx)
        rcy = (a.cy - b.cy)
        rcz = (a.cz - b.cz)
        return matriz(vector(rax,ray,raz),vector(rbx,rby,rbz), vector(rcx,rcy,rcz))
        
    def multiplicar(a,b):
        rax=(a.ax*b.ax)+(a.ay*b.bx)+(a.az*b.cx)
        ray=(a.ax*b.ay)+(a.ay*b.by)+(a.az*b.cy)
        raz=(a.ax*b.az)+(a.ay*b.bz)+(a.az*b.cz)
        rbx=(a.bx*b.ax)+(a.by*b.bx)+(a.bz*b.cx)
        rby=(a.bx*b.ay)+(a.by*b.by)+(a.bz*b.cy)
        rbz=(a.bx*b.az)+(a.by*b.bz)+(a.bz*b.cz)
        rcx=(a.cx*b.ax)+(a.cy*b.bx)+(a.cz*b.cx)
        rcy=(a.cx*b.ay)+(a.cy*b.by)+(a.cz*b.cy)
        rcz=(a.cx*b.az)+(a.cy*b.bz)+(a.cz*b.cz)
        
        return matriz(vector(rax,ray,raz),vector(rbx,rby,rbz), vector(rcx,rcy,rcz))
