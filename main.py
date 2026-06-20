from RegistroAtencion import RegistroAtencion
from Multas import MultaPrestamoSala, MultaPrestamoLibro
from Recursos import Recurso

recurso1 = Recurso("Libro", "Noche de amor")
print(recurso1)
recurso2 = Recurso("Libro", "Noche de amor")
print(recurso1)
recurso3 = Recurso("Libro", "Noche de amor")
print(recurso1)
recurso4 = Recurso("Libro", "Noche de amor")
print(recurso1)
recurso5 = Recurso("Libro", "Noche de amor")
print(recurso1)


Registro1 = RegistroAtencion("REG-2026-A", "20255624", "TulioMarco")
print(RegistroAtencion)

Registro1.agregar_recurso(recurso1)
Registro1.agregar_recurso(recurso2)
Registro1.agregar_recurso(recurso3)
Registro1.agregar_recurso(recurso4)
print(recurso1)

Registro1.obtener_recursos()

multa1 = MultaPrestamoLibro(5)
print(multa1)