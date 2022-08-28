#IMPORTANTE: No terminal do PyCharm execute o comando pip install truth-table-generator

import ttg

while True:
    print('\n******************************************DESCRIÇÃO********************************************')
    print('Programa que fornece a tabela verdade de uma proposição lógica e a classifica em Tautologia, \n'
          'Contingência ou Contradição.')
    print('***************************************ENTRADA DE DADOS****************************************')
    print("[1] Use qualquer letra para indicar uma proposição, como por exemplo, p, q, r,...\n"
          "[2] Os operadores lógicos são indicados por:\n"
          "'não' -> '~', 'e' -> 'and', 'ou' -> 'or', 'implicação' -> '=>', 'dupla implicação' -> '='\n"
          "Por exemplo, para o cálculo do valor lógico da proposição\n"
          "                                     'p and q'                                     \n"
          "digite:\n"
          "['p', 'q'] na primeira entrada (proposições simples) e\n"
          "['p and q'] na segunda entrada (proposições compostas)\n"
          "Em particular, o exemplo em questão trata-se de uma contingência.")
    print('****************************************SAÍDA DE DADOS*****************************************')
    a = input('Digite as proposições simples: ')
    b = input('Digite as propsições compostas: ')
    print(ttg.Truths(eval(a),eval(b)))
    table_val = ttg.Truths(eval(a),eval(b))
    if str(table_val.valuation()) == 'Tautology':
        print('A proposição em questão é uma Tautologia.\n')
    if str(table_val.valuation()) == 'Contingency':
        print('A proposição em questão é uma Contingência.\n')
    if str(table_val.valuation()) == 'Contradiction':
        print('A proposição em questão é uma Contradição.\n')
    print('             Programa obtido de: https://pypi.org/project/truth-table-generator/             \n')
    print('                 Versão Adaptada: Allan de Sousa Soares - IFBA VDC                    ')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    input('Digite Enter para continuar: ')
