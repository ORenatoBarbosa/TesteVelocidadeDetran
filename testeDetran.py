velocidade = float(input("Digite a velocidade do seu carro:"))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado em R$ %7.2f!" % multa)
if velocidade <=80:
    print("Sua velocidade está ok, boa viagem!")
    
# Renato Barbosa
