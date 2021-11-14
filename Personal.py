"""Archivo para las clases"""
print("Archivo modificado en pycharm")
class Gerente:
    def __init__(self, Nombre, Altura, Edad, Vestimenta):
        self.__Vestimenta=Vestimenta
        self.__Altura=Altura
        self.__Edad=Edad
        self.__Nombre=Nombre
    def getInfo(self):
        print("El nombre es: ", self.__Nombre)
        print("La edad es: ", self.__Edad)
        print("La altura es:", self.__Altura)
        print("La vestimenta es: ", self.__Vestimenta)
    def Entrevistando(self):
        return ("El Gerente esta entrevistando a una persona")
    def Supervisando(self):
        return ("El Gerente esta supervisando las áreas de trabajo")
    def Noasiste(self):
        return ("El gerente no asistio")
class Empleado(Gerente):
    def __init__(self, Nombre, Altura, Edad, Vestimenta):
        super().__init__(self, Nombre, Altura, Edad, Vestimenta)
    def getInfo(self):
        print("El nombre es: ", self.__Nombre)
        print("La edad es: ", self.__Edad)
        print("La altura es:", self.__Altura)
        print("La vestimenta es: ", self.__Vestimenta)
    def Trabajanto(self):
        print("El empleado esta trabajando.")
    def Descansando(self):
        print("El empleado esta descansando.")
    def Cobrar(self):
        print("El trabajador esta cobrando.")
class Persona(Gerente):
    def __init__(self, Nombre, Altura, Edad, Vestimenta):
        super().__init__(self, Nombre, Altura, Edad, Vestimenta)
    def getInfo(self):
        print("El nombre es: ", self.__Nombre)
        print("La edad es: ", self.__Edad)
        print("La altura es:", self.__Altura)
        print("La vestimenta es: ", self.__Vestimenta)
    def Solicitando(self):
        print("La persona esta solicitando empleo")
    def Buscando(self):
        print("La persona esta buscando empleo")
    def Aceptado(self):
        print("La persona ha sido aceptada")
