saldo=00
saque=400
limite=300
conta_normal=True
conta_universitaria=False


if conta_normal:
    if saldo>saque:
        print("saque realizado com sucesso")
    elif saldo+limite>saque:
        print("saque realizado com uso do cheque especial")
    else: print("saque não realizado")
elif conta_universitaria:
    if saldo>saque:
        print("saque realizado com sucesso")
    else:
        print("saque não realizado")


   








         

