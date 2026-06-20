class Multa:
    def __init__(self, monto : float, motivo : str):
        self.monto = monto
        self.motivo = motivo
    
    def __str__(self):
        return f"Multa de {self.monto} por {self.motivo}"
    

class MultaPrestamoLibro(Multa):
    def __init__(self, horas_retraso : float):
        monto = horas_retraso * 2.50
        motivo = f"Retraso de {horas_retraso} horas en la devolución del libro."
        super().__init__(monto, motivo)
    
    def CalcularMulta(self):
        return self.monto
    
class MultaPrestamoSala(Multa):
    def __init__(self, horas_exceso, factor_penalizacion):
        monto = horas_exceso * factor_penalizacion
        motivo = f"Exceso de {horas_exceso} horas en el uso de la sala con un factor de penalización de {factor_penalizacion}."
        super().__init__(monto, motivo)
    
    def CalcularMulta(self):
        return self.monto
    
