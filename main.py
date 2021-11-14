"""Archivo para las clases"""
print("Archivo modificado en pycharm")
class Puesto:
    def __init__(self, Gerente, Empleado, Jefe):
        self.__Gerente=Gerente
        self.__Empleado=Empleado
        self.__Jefe=Jefe
    def GetGerente(self):
        return self.__Gerente
    def GetEmpleado(self):
        return self.__Empleado
    def GetJefe(self):
        return self.__Jefe

class Uniforme:
    def __init__(self, Comercial, Operativo, Seguridad, Sectorsalud):
        self.__Comercial=Comercial
        self.__Operativo=Operativo
        self.__Seguridad=Seguridad
        self.__Sectorsalud=Sectorsalud



