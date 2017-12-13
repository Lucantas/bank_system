#This is a ATM project, simulating the interations with a bank and a client, to create your bank account give us a call : 0800 not
from Conta import Conta
from Conta_Poup import Conta_Poup

contas = []

def cria_conta(Conta, contas):
    def agrupa_contas(Conta, contas):
        contas.append(Conta)

    agrupa_contas(Conta, contas)

cria_conta(Conta(1,50,"Lucas",100), contas)
cria_conta(Conta_Poup(2,2000, "Monique",5000), contas)

contas[0].transfere(200,contas[1])

contas[0].extrato()
contas[1].extrato()




