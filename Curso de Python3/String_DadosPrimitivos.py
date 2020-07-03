################# Strings (str) -> Textos dentro de aspas #################

# Obs -> Podendo ser aspas simples ou aspas duplas e ou ate aspas triplas!

print('Essa é uma string (str).')

print("Essa é uma 'string'(str).")

print("Andre", 'Strin \n g', """str""")

# /n -> quebra a linha

################# DADOS PRIMITIVOS #################


# Tipos de Dados Primitivos

# Strings (Str) = Textos dentro de aspas! = assim' ou "assim ou """assim""""
# Inteiro (Int) = Numeros Inteiros = 123456, 15000, 15, 1 ,0
# Float ( Numero real flutuante) = 10.5, 10,50, -50.13, 0.0
# Booleano (Valor logico) = True/False = 10 == 10
#
print(type('Andre'))

# No caso acima chamamos a funcao type, que no caso retorna o valor da classe entre os parenteses

# print('10' + 10)

# nao se pode somar um texto com um numero inteiro, porem pode-se se juntar um inteiro com outro inteiro,
# podemos tbm transformar um numero em string do tipo print('10', int('10') que no caso temos uma string com escrita 10 e depois trasnformamos ela em um inteiro, isso se chama type casting!

 ##################### RESOLUCAO DO PROBLEMA DA AULA! ########################
#String Nome
print('Andre Vitor Veloso Paim', type('Andre Vitor Veloso Paim'))
#Int, Idade
print(27, type(27))
#Float, Altura
print(1.75, type(1.75))
#Bool, Maior de idade
print(27 >= 18, type(27 >= 18))

