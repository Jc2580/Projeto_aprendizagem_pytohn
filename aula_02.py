#for, range, while



texto=str(input("insera o texto:"))
VOGAIS="AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:print("final do laço")


for numero in range(0,51,5):
    print(numero,end=" ")

opcao=-1

while opcao!= 0:

 opcao=input("insira a opcão [1] \n sacar [2] \n extrato [0] \n sair")
 if opcao==1:
        print("extrato")
 elif opcao ==2:
        print("sacar")










