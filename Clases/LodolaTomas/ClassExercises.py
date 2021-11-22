class ComplexNumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other): #sobrecarrega el operador +
        return ComplexNumbers(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other): #sobrecarrega el operador -
        return ComplexNumbers(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other): #sobrecarrega el operador *
        return ComplexNumbers(self.real * other.real, self.imaginary * other.imaginary)

    def __truediv__(self, other): #sobrecarrega el operador /
        return ComplexNumbers(self.real / other.real, self.imaginary / other.imaginary)

    def __str__(self): #sobrecarrega el operador str
        return str(self.real) + ' + ' + str(self.imaginary) + "i"


#print(ComplexNumbers(1, 2)) # llama a la sobrecarga del operador str : 1 + 2i
#print(ComplexNumbers(1, 3) + ComplexNumbers(4, 1)) #complexNumbers(1,3)__add__(complexNumbers(4,1)) is the same

class ThreeDimensionalVector: #clase que representa un vector de 3 dimensiones
    def __init__(self, x, y, z):
        self.matrix = [x, y, z]

    def __add__(self, other): #sobrecarrega el operador +
        return ThreeDimensionalVector(self.matrix[0] + other.matrix[0], self.matrix[1] + other.matrix[1], self.matrix[2] + other.matrix[2])

    def __sub__(self, other): #sobrecarrega el operador -
        return ThreeDimensionalVector(self.matrix[0] - other.matrix[0], self.matrix[1] - other.matrix[1], self.matrix[2] - other.matrix[2])

    def __mul__(self, other): #sobrecarrega el operador *
        return ThreeDimensionalVector(self.matrix[0] * other.matrix[0], self.matrix[1] * other.matrix[1], self.matrix[2] * other.matrix[2])

    def __truediv__(self, other): #sobrecarrega el operador /
        return ThreeDimensionalVector(self.matrix[0] / other.matrix[0], self.matrix[1] / other.matrix[1], self.matrix[2] / other.matrix[2])

    def __str__(self): #sobrecarrega el operador str
        return str(self.matrix)

#print(ThreeDimensionalVector(1, 2, 3)) # llama a la sobrecarga del operador str : 1 2 3
#print(ThreeDimensionalVector(4, 0, -3) + ThreeDimensionalVector(-1, -4, 3)) #ThreeDimensionalVector(1,2,3)__add__(ThreeDimensionalVector(4,5,6)) is the same

class DimensionalMatrix3x3:
    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.matrix = [[a,b,c],[d,e,f],[g,h,i]]
    
    def __add__(self, other): #sobrecarrega el operador +
        return DimensionalMatrix3x3(self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1], self.matrix[0][2] + other.matrix[0][2],
                                    self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1], self.matrix[1][2] + other.matrix[1][2],
                                    self.matrix[2][0] + other.matrix[2][0], self.matrix[2][1] + other.matrix[2][1], self.matrix[2][2] + other.matrix[2][2])

    def __sub__(self, other): #sobrecarrega el operador -
        return DimensionalMatrix3x3(self.matrix[0][0] - other.matrix[0][0], self.matrix[0][1] - other.matrix[0][1], self.matrix[0][2] - other.matrix[0][2],
                                    self.matrix[1][0] - other.matrix[1][0], self.matrix[1][1] - other.matrix[1][1], self.matrix[1][2] - other.matrix[1][2],
                                    self.matrix[2][0] - other.matrix[2][0], self.matrix[2][1] - other.matrix[2][1], self.matrix[2][2] - other.matrix[2][2])

    def __mul__(self, other): #sobrecarrega el operador *
        return DimensionalMatrix3x3(self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0] + self.matrix[0][2] * other.matrix[2][0],
                                    self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1] + self.matrix[0][2] * other.matrix[2][1],
                                    self.matrix[0][0] * other.matrix[0][2] + self.matrix[0][1] * other.matrix[1][2] + self.matrix[0][2] * other.matrix[2][2],
                                    self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0] + self.matrix[1][2] * other.matrix[2][0],
                                    self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1] + self.matrix[1][2] * other.matrix[2][1],
                                    self.matrix[1][0] * other.matrix[0][2] + self.matrix[1][1] * other.matrix[1][2] + self.matrix[1][2] * other.matrix[2][2],
                                    self.matrix[2][0] * other.matrix[0][0] + self.matrix[2][1] * other.matrix[1][0] + self.matrix[2][2] * other.matrix[2][0],
                                    self.matrix[2][0] * other.matrix[0][1] + self.matrix[2][1] * other.matrix[1][1] + self.matrix[2][2] * other.matrix[2][1],
                                    self.matrix[2][0] * other.matrix[0][2] + self.matrix[2][1] * other.matrix[1][2] + self.matrix[2][2] * other.matrix[2][2])

    

print(DimensionalMatrix3x3(0,-7,3,2,4,-1,12,7,-6) * DimensionalMatrix3x3(5,4,-3,0,-6,10,-2,8,11))