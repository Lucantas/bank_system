"""
This is a ATM project, simulating the interations with a bank 
and a client, to create your bank account give us a call : 
0800 not

If you're not a portuguese speaker, and I will assume that you're
not, even tought I wrote this code in the most clearly Port_English
i will help you getting trough it:

Conta and it's childs are Bank Accounts
Cliente is the Client

saca == withdraw
deposita == deposit
transfere == transfer
numero == number
titular == owner
saldo == balance
limite == limit

"""
from Conta import Conta
from Conta_Poup import Conta_Poup

contas = []

def cria_conta(Conta, contas):
    def agrupa_contas(Conta, contas):
        contas.append(Conta)

    agrupa_contas(Conta, contas)

cria_conta(Conta(1,50,"Lucas",100), contas)
cria_conta(Conta_Poup(2,2000, "Monique",5000), contas)

contas[1].transfere(500,contas[0])

contas[0].extrato()
contas[1].extrato()




