from Conta import Conta 

class Conta_Corr(Conta):
    
    """
    Conta_Corr should have a monthly charge for it's users, and it's
    the only Conta child that can use method saca untill reach it's 
    limite
    """


    def __init__(self, numero, saldo, titular, limite):
        super().__init__(numero, saldo, titular, limite)
    