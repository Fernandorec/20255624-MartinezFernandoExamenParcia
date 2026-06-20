from Multas import MultaPrestamoSala, MultaPrestamoLibro
from Recursos import Recurso

class RegistroAtencion:
    def __init__(self, codigo, carnet : str, bibliotecario : str):
        self.codigo = codigo  
        self.carnet = carnet
        self._recursos = []
        self.bibliotecario = bibliotecario
        self.multas = int

    def agregar_recurso(self, recurso):
        if len(self._recursos) >= 4:
            raise ValueError("No se pueden agregar más de 4 recursos.")
        self._recursos.append(recurso)

    def obtener_recursos(self):
        return self._recursos.copy()
    

    
    def __str__(self):
        return f"{self.codigo}, {self.carnet}, {self.bibliotecario}"



    def revision_Saldos(self, multas):
        self.multas = sum(self.multas)
    
    
    def Obtener_multas(self)
        if ((sum(self.multas)* 100% / 15)) >= 15 :
            raise ValueError("CUENTA_SUSPENDIDA")
