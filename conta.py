from cliente import Cliente

class Conta:
    def __init__(self, numero, saldo, titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = Cliente(titular)
        self.nome_titular = self.__titular.nome

    def saca(self,valor):
        if(self.__saldo >= valor and valor > 0):
            self.__saldo -= valor
            return True
        else:
            print("Saldo Insuficiente!")
            return False        

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        valor_a_autorizar = self.saca(valor)
        if (valor_a_autorizar == True):
            destino.deposita(valor)
                   
    def Saldo(self):
        return self.__saldo

    def Titular(self):
        return self.__titular.mostra_nome()

