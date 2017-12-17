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
from Conta_Corr import Conta_Corr
from Cliente import Cliente

clientes = []

clientes.append(Cliente("lucas"))
clientes.append(Cliente("23123"))
clientes.append(Cliente("2j"))

print(clientes[1].nome)



##contas = []

#def cria_conta(Conta, contas):
 #   def agrupa_contas(Conta, contas):
        #contas.append(Conta)

  #  agrupa_contas(Conta, contas)

#cria_conta(Conta_Corr(1,50,"Lucas",100), contas)
#cria_conta(Conta_Poup(2,2000, "Monique",5000), contas)

#contas[0].transfere(100,contas[1])

##contas[0].extrato()
#contas[1].extrato()





