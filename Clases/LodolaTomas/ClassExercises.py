class ComplexNumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumbers(self.real * other.real, self.imaginary * other.imaginary)

    def __truediv__(self, other):
        return ComplexNumbers(self.real / other.real, self.imaginary / other.imaginary)

    def __str__(self):
        return str(self.real) + ' + ' + str(self.imaginary) + "i"


print(ComplexNumbers(1, 3) / ComplexNumbers(4, 1))
