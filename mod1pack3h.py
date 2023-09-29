temp = int(input("Insira a sua temperatura:"))
while temp != "SAIR" :
    if temp >= 38 and temp <= 39 :
        print("Você está com febre. Tome um remédio e repouse")
        temp = int(input("Insira a sua temperatura:"))
    elif temp > 39 :
        print("Você está com febre. Tome um remédio, procure um médico.")
        temp = int(input("Insira a sua temperatura:"))
    elif temp < 38 :
        print("Nada de febre")
        temp = int(input("Insira a sua temperatura:"))
else :
    print("Finalizando programa.")