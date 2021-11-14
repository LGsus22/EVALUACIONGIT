"""Este archivo unicamente se utiliza para dar información de la empresa...
Solo se requiere en caso de colocar el metodo de la clase
Cuenta como archivo adicional
"""
class Company:
    def __init__(self, Nombre, Direccion, Vacante):
        self.__Nombre=Nombre
        self.__Direccion=Direccion
        self.__Vacante=Vacante
    def GetInfoEmpresa(self):
        print("El nombre de la empresa es:", self.__Nombre)
        print("La direccion es:", self.__Direccion)
        print("Tipo de vacante:", self.__Vacante)