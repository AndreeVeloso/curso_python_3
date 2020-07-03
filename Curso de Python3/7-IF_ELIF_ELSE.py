########### CONDICOES IF, ELIF E ELSE #############

# Exemplo 1

"""

if True:
    print('Verdadeiro')

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)
# IF = SE , no caso, passa uma condicao podendo ela ser verdade ou nao.

"""

# Exemplo 2

"""
if False:
    print('Verdadeiro')
print('A minha expressao nao e verdadeira') # nesse caso independente da condicao ser satisfeita ou nao( True ou False)
o comando print da expresao nao ser verdadeira, sera executado pq ele nao participa da hierarquia onde o if se apresenta!

"""

# Exemplo 3
"""
if True:
    print('Verdadeiro')
else:                           # else NAO PODE SER USADO SEM VIR UM IF ANTES!
    print('Nao e verdadeiro!')

"""

# Exemplo 4
"""
if False:
    print('Verdadeiro')
    print('teste 2')
elif True:
    print('Agora e verdadeiro!')
    nome = input('Qual seu Nome? ')
elif False:
    print('Mais uma verdadeira')
    print(22+22)
else:                           # else NAO PODE SER USADO SEM VIR UM IF ANTES!
    print('Nao e verdadeiro!')
    print('HELLO WORLD')
"""

    """
    ALGO BEM INTERESSANTE PRA SE COMENTAR E QUE, USANDO AS EXPRESSOES IF,ELIF E ELSE, ELAS NECESSITAM DE 4 ESPACOS PRA SEGUIREM A HIERARQUIA DAS CONDICOES
    E NO CASO, ASSIM QUE A PRIMEIRA OU ALGUMAS DAS DEMAIS CONDICOES FOREM SATISFEIRAS, O RESTO DO CODIGO ABAIXO SERA DEIXADO DE LADO E EXIBIRA A O QUE FOR
    PROGRAMADO NA CONDICAO QUE TENHA SIDO CONSIDERADA SATISFEITA!
    """



