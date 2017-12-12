from Conta import Conta

class Conta_Poup(Conta):

    def __init__(self, numero, saldo, titular, limite):
        Conta.__init__(self, numero, saldo, titular, limite)