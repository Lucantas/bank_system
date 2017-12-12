from Conta import Conta

class Conta_Poup(Conta):

    def __init__(self, numero, saldo, titular, limite):
        super().__init__(numero, saldo, titular, limite)

    def saca(self,valor):
        if(self.__valida_saque(valor)):
            self.__saldo -= (valor - 0.01) 
            return True
        else:
            print("Saldo Insuficiente!")

        