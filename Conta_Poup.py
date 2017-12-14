from Conta import Conta

class Conta_Poup(Conta):
    """
    This kind of Conta should:

    - pay for each saca it uses

    - have a limit of transfering 500 a day



    """

    def __init__(self, numero, saldo, titular, limite):
        super().__init__(numero, saldo, titular, limite)

    def saca(self,valor):
        if(self._saldo >= valor):
            self._saldo -= (valor + 0.01) 
            return True
        else:
            print("Saldo Insuficiente!")

        