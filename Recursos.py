class Recurso:
    def __init__(self, tipo : str, descripcion : str):
        self.tipo = tipo
        self.descripcion = descripcion
    
    def __str__(self):
        return f"Recurso de {self.tipo} con descripcion de {self.descripcion}"




