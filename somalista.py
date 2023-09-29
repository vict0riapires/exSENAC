uni = float(input("Insira a quantidade de números a ser somado:"))
soma = 0
uni_inicial = 0
while (uni_inicial < uni) :
    x = int(input("Insira o número:"))
    soma = soma + x
    uni_inicial = uni_inicial + 1
    print("A soma dos números é", format(soma))