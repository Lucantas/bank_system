from Conta import Conta 

class Conta_Corr(Conta):
    
    """
    Conta_Corr should have a monthly charge for it's users, and it's
    the only Conta child that can use method saca untill reach it's 
    limite
    """
    def __init__(self, numero, saldo, titular, limite):
        super().__init__(numero, saldo, titular, limite)


    @property
    def saldo_absoluto(self):
        return self._saldo + abs(self._limite)

    def saca(self, valor):
        if(self.saldo_absoluto >= valor):
            self._saldo -= valor
            return True
        else:
            print("Saldo Insuficiente!")