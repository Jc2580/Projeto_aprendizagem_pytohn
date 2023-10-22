nome= "joão Carlos"
idade=34
profissão="Técnico em segurança"

dados= {"nome":"Guilherme", "idade":34}
saldo=45.4563

print("nome: %s , idade: %d" %(nome,idade))
print("nome: {} , idade: {}".format(nome,idade))
print("nome: {1} , idade: {0}".format(nome,idade))
print("nome: {nome} , idade: {idade}".format(nome=nome,idade=idade))
print("nome: {name} , idade: {age}".format(name=nome, age=idade))
print("nome:{name} idade:{age} {name} {name} {age}".format(age=idade, name=nome))
print("nome:{nome} idade{idade}".format(**dados))
print(f"{nome} e {idade} e {saldo:10.2f}")