################# COMANDO INPUT ##################

"""
O  comando input, serve para interacao com o usuario, que no caso serve como uma entrada de dados.
No caso o comando input serve pra criacao de uma string que sera dada pela entrada de dados do usuario.


"""


"""
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')

ano_nascimento = 2020-int(idade)  # Temos que entender que o input retorna uma string, mesmo idade sendo um numero, no caso um erro vai ser exibido, para converter, teremos que fazer um type casting.

print()
"""
"""
#Exemplo 1

#print(f'O usuario digitou {nome} e o tipo da variavel e '
#     f'{type(nome)}')

print(f'{nome} tem {idade} anos. '
f'{nome} nasceu em {ano_nascimento}.')
"""

#Exemplo 2 - Calculadora de somas

numero_1 = int(input('digite um numero: '))
numero_2 = input('digite outro numero: ')
numero_2 = int(numero_2)

print(numero_1 + numero_2)





