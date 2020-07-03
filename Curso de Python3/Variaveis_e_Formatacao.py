################### AULA DE VARIAVEIS ###################
"""

nome = 'Andre' , estilo de atribuicao de variavel

obs: Se inicia com letra, pode conter numeros, para separar as palavrasa ou numeros e letras se usa '_'
feita em letras minusculas


no caso, nome = Andre
entao

print(nome) -> imprime na tela o valor declarado = Andre

podemos ainda pedir a classificacao da variavel

print(nome, type(nome))
"""

nome = 'Andre'
idade = 27
altura = 1.75
peso = 75
e_maior = idade > 18
imc = peso/ (altura ** 2)


"""
print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('E maior de idade: ', e_maior)
"""

################# RESOLUCAO DO EXERCICIO ####################

"""
print(nome, 'tem', idade, 'anos de idade e seu imc e: ', imc)
"""

################# FORMATACAO DE VARIAVEIS ###################


# Exemplo
print(f'{nome} tem {idade} anos de idade e seu imc e: {imc:.2f}')

# Pra formatacao dos numeros de casas decimais do imc, damos :.2f para que apareca apenas 2 casas decimais do numero float que e gerado

# OUTRA FORMA DE FORMATAR AS VARIAVEIS E USANDO O COMANDO .format

#Exemplo 2

print('{0} tem {1} anos e seu imc e: {2:.2f}'.format(nome,idade, imc))

# usando o .format, definimos uma sequencia das variaveis e podemos usar elas na sequencia que quisermos, mas respeitando sempre que agora as variaveis sao organizadas em ordem numero

# Exemplo 3


print('{n} {i} {im:.2f} '.format(n=nome, i=idade, im=imc)) ### podendo redefinir tambem


