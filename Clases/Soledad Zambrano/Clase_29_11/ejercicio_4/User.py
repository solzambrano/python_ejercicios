from Contenedor import Contenedor

class User():

    def __init__(self, username, password, email) -> None: # "-> None" indica el tipo de dato que devuelve el método
        self.username = username
        self.password = password
        self.email = email
        self.contenedor = Contenedor()

    def addNewItem(self, item):
        self.contenedor.add(item)