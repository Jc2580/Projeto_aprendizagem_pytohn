valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())



def valor_final():
   return valor_inicial * (1+taxa_juros)**periodo


print("Valor final do investimento: R$", round(valor_final(),2))