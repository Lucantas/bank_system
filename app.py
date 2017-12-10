#This is a ATM project, simulating the interations with a bank and a client, to create your bank account give us a call : 0800 not
from conta import Conta

conta_1 = Conta(1,1000,"Lucas")
conta_2 = Conta(2,10,"Monique")


conta_1.transfere(100,conta_2)

print(conta_2.Saldo())
print(conta_1.Saldo())




