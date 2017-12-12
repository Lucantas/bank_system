from Cliente import Cliente

class Conta:
    def __init__(self, numero, saldo, titular, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = Cliente(titular)
        self.__limite = limite

    @property
    def saldo_absoluto(self):
        return self.__saldo + self.__limite
        
    def __valida_saque(self, valor):
        if(self.saldo_absoluto < valor and valor < 0):
            return False
        else:
            return True

    def saca(self,valor):
        if(self.__valida_saque(valor)):
            self.__saldo -= valor
            return True
        else:
            print("Saldo Insuficiente!")
        

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        if (self.saca(valor)):
            destino.deposita(valor)

    def extrato(self):
        print("Olá sr.(a) {}, o seu saldo atual é: R$ {}".format(self.titular, self.saldo))
    
    def historico(self):
        #Method to show accounts history, to be implemented
        pass

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property           
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.nome

    @staticmethod
    def codigo_banco():
        return "001"