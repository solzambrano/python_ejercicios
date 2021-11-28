# Ejercicio 3
# Suma y Resta es Entre columnas verticales. En la resta se cambia el signo a la segunda matriz y se hace la operacion.
class Matris3D: # Se que no se ponen numeros para crear, pero era para no perderme tanto

    def __init__(self, matris , matrisDos):
        self.matris = matris
        self.matrisDos = matrisDos

    def Suma(self): # En la suma es sumar las verticales con verticales.
        
        newcolumnX = []
        newcolumnY = []
        newcolumnZ = []
        count = 0
        countDos = 0
        countTres = 0

        for x in self.matris["columnaX"]:
            newcolumnX.insert(count, x + self.matrisDos["columnaX"][count]) 
            count += 1
        for x in self.matris["columnaY"]:
            newcolumnY.insert(countDos, x + self.matrisDos["columnaY"][countDos]) 
            countDos += 1        
        for x in self.matris["columnaZ"]:
            newcolumnZ.insert(countTres, x + self.matrisDos["columnaZ"][countTres]) 
            countTres += 1

        MatrisFinal = {
            "columnX" : newcolumnX,
            "columnY" : newcolumnY,
            "columnZ" : newcolumnZ
        }

        return print(MatrisFinal)
    
    def Resta(self): # En la resta de matris se cambia el signo de la segunda, al multiplicar por -1 nos da el signo 
        newcolumnX = [] # contrario en ambos casos
        newcolumnY = []
        newcolumnZ = []
        count = 0
        countDos = 0
        countTres = 0

        for x in self.matris["columnaX"]:
            newcolumnX.insert(count, x + (self.matrisDos["columnaX"][count] * -1)) 
            count += 1
        for x in self.matris["columnaY"]:
            newcolumnY.insert(countDos, x + (self.matrisDos["columnaY"][countDos]* -1)) 
            countDos += 1        
        for x in self.matris["columnaZ"]:
            newcolumnZ.insert(countTres, x + (self.matrisDos["columnaZ"][countTres]* -1)) 
            countTres += 1

        MatrisFinal = {
            "columnX" : newcolumnX,
            "columnY" : newcolumnY,
            "columnZ" : newcolumnZ
        }

        return print(MatrisFinal)

    def Multi(self):
        newcolumnX = [] 
        newcolumnY = []
        newcolumnZ = []
         
        newcolumnX.insert(0,(self.matris["columnaX"][0] * self.matrisDos["columnaX"][0])+(self.matris["columnaY"][0] * self.matrisDos["columnaX"][1])+(self.matris["columnaZ"][0] * self.matrisDos["columnaX"][2]))
        newcolumnX.insert(1,(self.matris["columnaX"][1] * self.matrisDos["columnaX"][0])+(self.matris["columnaY"][1] * self.matrisDos["columnaX"][1])+(self.matris["columnaZ"][1] * self.matrisDos["columnaX"][2]))
        newcolumnX.insert(2,(self.matris["columnaX"][2] * self.matrisDos["columnaX"][0])+(self.matris["columnaY"][2] * self.matrisDos["columnaX"][1])+(self.matris["columnaZ"][2] * self.matrisDos["columnaX"][2]))

        newcolumnY.insert(0,(self.matris["columnaX"][0] * self.matrisDos["columnaY"][0])+(self.matris["columnaY"][0] * self.matrisDos["columnaY"][1])+(self.matris["columnaZ"][0] * self.matrisDos["columnaY"][2]))
        newcolumnY.insert(1,(self.matris["columnaX"][1] * self.matrisDos["columnaY"][0])+(self.matris["columnaY"][1] * self.matrisDos["columnaY"][1])+(self.matris["columnaZ"][1] * self.matrisDos["columnaY"][2]))
        newcolumnY.insert(2,(self.matris["columnaX"][2] * self.matrisDos["columnaY"][0])+(self.matris["columnaY"][2] * self.matrisDos["columnaY"][1])+(self.matris["columnaZ"][2] * self.matrisDos["columnaY"][2]))

        newcolumnZ.insert(0,(self.matris["columnaX"][0] * self.matrisDos["columnaZ"][0])+(self.matris["columnaY"][0] * self.matrisDos["columnaZ"][1])+(self.matris["columnaZ"][0] * self.matrisDos["columnaZ"][2]))
        newcolumnZ.insert(1,(self.matris["columnaX"][1] * self.matrisDos["columnaZ"][0])+(self.matris["columnaY"][1] * self.matrisDos["columnaZ"][1])+(self.matris["columnaZ"][1] * self.matrisDos["columnaZ"][2]))
        newcolumnZ.insert(2,(self.matris["columnaX"][2] * self.matrisDos["columnaZ"][0])+(self.matris["columnaY"][2] * self.matrisDos["columnaZ"][1])+(self.matris["columnaZ"][2] * self.matrisDos["columnaZ"][2]))
        
        MatrisFinal = {
            "columnX" : newcolumnX,
            "columnY" : newcolumnY,
            "columnZ" : newcolumnZ
        }

        return print(MatrisFinal)

MiMatris = Matris3D({
            "columnaX" : [1,4,5],  #  1 7 1 
            "columnaY" : [7,2,5],  #  4 2 4
            "columnaZ" : [1,4,5]   #  5 5 5  
        },{                             # Ingresar matrises a Sumar, restar y multiplicar 
            "columnaX" : [9,7,41], #  9 7 1                 
            "columnaY" : [7,2,5],  #  7 2 4
            "columnaZ" : [1,4,5]   #  41 5 5 
        })
# X  Y  Z    
# 99 26 34
# 214 52 32                               
# 285 70 50
