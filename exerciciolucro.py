# Definindo o valor do produto

produto =float (input("Digite o valor do produto: R$"))

# Calculo

if produto < 20 :
    print("O valor do produto já com a margem de lucro é", (produto * 0.45) + produto)

else :
    print("O valor do produto já com a margem de lucro é", (produto * 0.30) + produto)