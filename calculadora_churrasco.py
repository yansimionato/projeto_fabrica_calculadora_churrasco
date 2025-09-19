# Crie um programa que calcule a quantidade de bebidas e de carne
# para a organização de um churrasco.

# Etapas da resolução:
# 1) solicitar o número de convidados
# 2) criar uma função para calcular a quantidade total de bebidas
# 3) criar uma função para calcular a quantidade total de canes
# 4) apresentar o resultado com os valores de total de carne e bebidas
# a serem comprados.

# usamos o int por que convidados deve ser um número inteiro.
convidados = int(input('Digite o número de convidados: '))

def calcular_bebidas(convidados, consumo_por_pessoa_ml = 800, volume_garrafa_litro = 2.25):
    total_ml = convidados * consumo_por_pessoa_ml # calcula o consumo de bebidas total por convidado/ml
    total_litro = total_ml/1000 # converte o consumo para litro

    garrafas = int(total_litro//volume_garrafa_litro) # divide o total do consumo pelo volume da garrafa
    if total_litro % volume_garrafa_litro > 0: # se o resultado for um número decimal
        garrafas += 1 # acrescenta uma garrafa na compra
    return total_litro, garrafas # retorna o total em litros e o número de garrafas
    
# resultado = calcular_bebidas(convidados)
# print(resultado)

def calcular_carne(convidados,consumo_por_pessoa_grama = 400):
    total_gramas = convidados * consumo_por_pessoa_grama # informa a quantidade total de carne em gramas
    total_kg = total_gramas / 1000 # transformando o valor total em gramas para quilo
    return total_kg


litros, garrafas = calcular_bebidas(convidados)
carne_kg = calcular_carne(convidados)

print('\n___Quantidade total para Churrasco___')
print(f'Número de convidados: {convidados}')
print(f'Refrigerantes necessários: {litros:.2f} litros.')
print(f'Garrafas de 2,5L: {garrafas} unidades.')
print(f'Carne necessária: {carne_kg:.2f} Kg.')