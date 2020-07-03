nome = 'Andre'
idade = 27
altura = 1.75
peso = 75
data_1 = 2020
imc = peso / (altura ** 2)
datnasc = data_1 - idade


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} e {imc:.2f}.')
print(f'{nome} nasceu em {datnasc}.')