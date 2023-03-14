from Nó import cNo

class fila:
    
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
        self.ultimo = None


    def insere(self,dado):
        nodo =cNo(dado)

        if self.ultimo is None:
            self.ultimo = nodo
        else:
            self.ultimo.__prox__ = nodo
            self.ultimo = nodo
        if self.primeiro is None:
            self.primeiro = nodo
        
        self.tamanho = self.tamanho + 1

    def remove(self):
        if self.tamanho > 0:
            elemento = self.primeiro.__dado__
            self.primeiro = self.primeiro.__prox__
            self.tamanho = self.tamanho - 1
            return elemento

    def mostra(self):
        if self.tamanho > 0:
            elemento = self.primeiro.__dado__
            return elemento
    
    