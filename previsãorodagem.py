def previsaoRodagem(gasolina,km):
    prevkms = gasolina * km
    print("A quantidade de KMS que você vai conseguir rodar é de", prevkms, "quilometros.")

gasolina = float(input("Insira os litros de gasolina"))
km = float(input("Insira quantos KM você consegue rodar com 1 litro de gasolina:"))
previsaoRodagem(gasolina,km)
