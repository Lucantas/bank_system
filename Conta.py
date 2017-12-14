from Cliente import Cliente

class Conta:
    """
    Class Conta, is a bank account, if you remember not to touch in
    the instance properties without calling it methods, you should be good!

    Remember to implement the validation of methods saca and transfere,
    because each child of Conta will have it's own way to deal with the
    transations


    """


    def __init__(self, numero, saldo, titular, limite):
        self._numero = numero
        self._saldo = saldo
        self._titular = Cliente(titular)
        self._limite = limite

    @property
    def saldo_absoluto(self):
        return self._saldo + self._limite
        
    def saca(self,valor):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def transfere(self, valor, destino):
        if (self.saca(valor) and valor <= 500):
            destino.deposita(valor)

    def extrato(self):
        print("Olá sr.(a) {}, o seu saldo atual é: R$ {}"
        .format(self.titular, self.saldo))
    
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
        return self._saldo

    @property
    def titular(self):
        return self._titular.nome

    @staticmethod
    def codigo_banco():
        return "001"