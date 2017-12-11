#This is a ATM project, simulating the interations with a bank and a client, to create your bank account give us a call : 0800 not
from conta import Conta

contas = []

def cria_conta(Conta, contas):
    def agrupa_contas(Conta, contas):
        contas.append(Conta)

    agrupa_contas(Conta, contas)

cria_conta(Conta(1,1000,"Lucas"), contas)
cria_conta(Conta(2,2000, "Monique"), contas)

contas[0].deposita(600)
contas[0].transfere(500,contas[1])


print("O saldo da conta do(a) {} é {} ".format(contas[1].titular, contas[1].saldo))
print("O saldo da conta do(a) {} é {} ".format(contas[0].titular, contas[0].saldo))




