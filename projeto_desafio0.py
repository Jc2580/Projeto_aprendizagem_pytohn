saldo_atual=float(input())
valor_deposito=float(input())
valor_retirada=float(input())

def saldo_final():
   return (saldo_atual + valor_deposito - valor_retirada)

#if saldo_final()>0:
# print ( round(saldo_final(),1))
#elif saldo_final ==0:
# 0
#else:saldo_final()<0
#print(f" o" round(saldo_final(),1))
   


print ("O saldo atualizado na conta", round(saldo_final(),1))
