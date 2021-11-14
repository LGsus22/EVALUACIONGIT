"""Examen de Unidad 4
Jesus Peralta Tapia
"""
import Personal
print("Archivo modificado desde pycharm")
print("Empresa 'TraditionalStart'")
Nombre=str(input("Ingrese su nombre: "))
Edad=int(input("Ingrese su edad: "))
Altura=float(input("Ingrese su altura: "))
Vestimenta=str(input("Ingrese su vestimenta: "))
print("Seleccione su puesto dependiendo el numero:")
print(" 1.-Gerente.\n","2.-Empleado.\n","3.-Persona.")
Puesto=int(input("Numero: "))
if Puesto == 1:
    gerente=Personal.Gerente(Nombre,Altura,Edad,Vestimenta)
    gerente.getInfo()
    gerente.Entrevistando()
elif Puesto == 2:
    empleado=Personal.Empleado(Nombre,Altura,Edad,Vestimenta)
    empleado.getInfo()
    empleado.Trabajanto()
elif Puesto == 3:
    persona=Personal.Persona(Nombre,Altura,Edad,Vestimenta)
    persona.getInfo()
    persona.Solicitando()