"""Examen de Unidad 4
Jesus Peralta Tapia
"""
import Personal
import Empresa
empresa=Empresa.Company("TraditionalStart", "Zona centro, Calle Alfonzo Luna No.32", "Puesto de empleado")
empresa.GetInfoEmpresa()
Nombre=str(input("Ingrese su nombre: "))
Altura=float(input("Ingrese su altura: "))
Vestimenta=str(input("Ingrese su vestimenta: "))
print("Seleccione su puesto dependiendo el numero:")
print(" 1.-Gerente.\n","2.-Empleado.\n","3.-Persona.")
Puesto=int(input("Numero: "))
if Puesto == 1:
    gerente=Personal.Gerente(Nombre,Altura,Vestimenta)
    gerente.status()
    gerente.Entrevistando()
elif Puesto == 2:
    empleado=Personal.Empleado(Nombre,Altura,Vestimenta)
    empleado.status()
    empleado.Trabajanto()
elif Puesto == 3:
    persona=Personal.Persona(Nombre,Altura,Vestimenta)
    persona.status()
    persona.Solicitando()