def permissao(idade) :
    if idade >= 18 :
        print("Você já pode beber e dirigir!")
    else :
        print("Você não pode dirigir ou beber ainda.")

idade = int(input("Insira idade:"))
permissao(idade)  