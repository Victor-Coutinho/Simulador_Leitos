import random

class paciente:

    def __init__(self,numero):
        self.gravidade = str(random.randint(3,5))
        self.idade = str(random.randint(0,2))
        self.numero = str(numero)
        self.resultado = str(self.gravidade + self.idade + self.numero)
    
class leito:
    
    def __init__(self,numero):
        self.idade = str(random.randint(0,2))
        self.numero = str(numero)
        self.resultado = str(self.idade + self.numero)
    

