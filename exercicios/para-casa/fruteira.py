#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#Define função de cálculo do preço total
def calcula_preco(preco_kg1, peso1, preco_kg2, peso2):
    preco_total = (preco_kg1 * peso1) + (preco_kg2 * peso2)
    return preco_total

try:
#Valores de peso inseridos pela pessoa usuária do sistema
    peso_morango = float(input("Qual o peso de morangos? "))
    peso_maca = float(input("Qual o peso de maçãs? "))

#Calcula peso total de frutas
    peso_total = peso_morango + peso_maca

#Testa se os valores de peso inseridos são positivos. Se sim, define os preços de cada fruta, de acordo com peso.
    if peso_morango >=0 and peso_maca >=0:
        if peso_morango <=5:
            preco_morango_kg = 2.50
            preco_maca_kg = 1.80
        else:
            preco_morango_kg = 2.20
            preco_maca_kg = 1.50

#Aplica desconto de 10% caso o peso total de frutas seja maior que 8 Kg ou o preço total for maior que 25.
        preco = calcula_preco(preco_morango_kg, peso_morango, preco_maca_kg, peso_maca)
        if peso_total > 8 or preco > 25:
            preco_total = 0.9 * preco
        else:
            preco_total = preco

#Imprime preço total
        print(f"O preço total é: R$ {preco_total:,.2f}")

#Se peso inserido for negativo, retorna mensagem de erro.
    else:
        print("Peso deve ser maior que zero!")

#Retorna uma mensagem de erro caso o valor de peso inserido não seja numérico
except(ValueError):
    print("Valor de peso inválido! Por favor, insira um valor numérico.")