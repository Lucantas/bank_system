from Conta import Conta 

class Conta_Corr(Conta):

    def __init__(self, numero, saldo, titular, limite):
        super().__init__(numero, saldo, titular, limite)

    