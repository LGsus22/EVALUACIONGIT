"""Archivo para las clases"""
print("Archivo modificado en pycharm")
class Gerente:
    def __init__(self, Nombre, Altura, Vestimenta):
        self.__Vestimenta=Vestimenta
        self.__Altura=Altura
        self.__Nombre=Nombre
    def status(self):
        print("El gerente de la empresa es un empleado que mide ", self.__Altura, "mts")
        print("Se llama ", self.__Nombre, "y tiene", self.__Vestimenta)

    def Entrevistando(self):
        return ("En este momento el Gerente esta entrevistando a una persona para su contratacion")
    def Supervisando(self):
        return ("En este momento el Gerente esta supervisando las áreas de trabajo")
    def Noasiste(self):
        return ("El gerente no asistio")
class Empleado(Gerente):
    def __init__(self, Nombre, Altura, Vestimenta):
        super().__init__(Nombre, Altura, Vestimenta)
    def status(self):
        super().status()
    def Trabajanto(self):
        print("En este momento el empleado esta trabajando.")
    def Descansando(self):
        print("En este momento el empleado esta descansando.")
    def Cobrar(self):
        print("En este momento el trabajador esta cobrando.")
class Persona(Gerente):
    def __init__(self, Nombre, Altura, Vestimenta):
        super().__init__(Nombre, Altura, Vestimenta)
    def status(self):
        super().status()
    def Solicitando(self):
        print("En este momento la persona esta solicitando empleo")
    def Buscando(self):
        print("En este momento la persona esta buscando empleo")
    def Aceptado(self):
        print("La persona ha sido aceptada")
