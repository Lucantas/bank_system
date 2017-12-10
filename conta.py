from cliente import Cliente

class Conta:
    def __init__(self, numero, saldo, titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = Cliente(titular)

    def saca(self,valor):
        self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def Saldo(self):
        return self.__saldo

    def Titular(self):
        return self.__titular

