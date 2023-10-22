while True:
 try:
 
   valor = float(input())

   if valor > 0:
     print("Deposito realizado com sucesso!\nSaldo atual: R$",format(valor,'.2f'))  
     break
   elif valor == 0:
    print("Encerrando o programa...")
    break
   else:
    print("Valor invalido! Digite um valor maior que zero.")
 except EOFError: break
 
 





     
