
class cNo:

    def __init__(self, dado=None):
        self.__dado__ = dado
        self.__prox__ = None

    def setDado(self, dado):

        # if type(dado) == int:
            self.__dado__ = dado

    
    def setProx(self, prox):

        # if type(prox) == cNo:
            self.__prox__ = prox


    def getDado(self):
        return self.__dado__


    def getProx(self):
        return self.__prox__ 
