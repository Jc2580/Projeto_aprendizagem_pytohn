saldo_total = int(input())
valor_saque = int(input())

def saldo_final():
   return (saldo_total - valor_saque)


if saldo_final()>=0:
   print("Saldo realizado com sucesso.Novo saldo:",saldo_final())
else :print("Saldo insuficiente. Saque nao realizado!")
   

