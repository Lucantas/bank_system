#This is a ATM project, simulating the interations with a bank and a client, to create your bank account give us a call : 0800 not
from Conta import Conta
from Conta_Poup import Conta_Poup

contas = []

def cria_conta(Conta, contas):
    def agrupa_contas(Conta, contas):
        contas.append(Conta)

    agrupa_contas(Conta, contas)

cria_conta(Conta(1,1000,"Lucas",5000), contas)
cria_conta(Conta_Poup(2,2000, "Monique",5000), contas)

contas[0].deposita(600)
contas[0].transfere(500,contas[1])

contas[0].limite = 10000

contas[1].extrato()

print(contas[0].saldo_absoluto)


