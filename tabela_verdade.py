#IMPORTANTE: No terminal do PyCharm execute o comando pip install truth-table-generator

import ttg

while True:
    print('\n*****************************************DESCRIÇÃO*******************************************')
    print('Programa que fornece a tabela verdade de uma proposição lógica.')
    print('***************************************ENTRADA DE DADOS****************************************')
    print("[1] Use qualquer letra para indicar uma proposição, como por exemplo, p, q, r,...\n"
          "[2] Os operadores lógicos são indicados por:\n"
          "'não' -> '~', 'e' -> 'and', 'ou' -> 'or', 'implicação' -> '=>', 'dupla implicação' -> '='\n"
          "Por exemplo, para o cálculo do valor lógico das expressões\n"
          "                                     'p and q' e 'p or q'                                     \n"
          "digite:\n"
          "['p', 'q'] na primeira entrada (proposições simples) e\n"
          "['p and q', 'p or q'] na segunda entrada (proposições compostas)")
    print('****************************************SAÍDA DE DADOS*****************************************')
    a = input('Digite as proposições simples: ')
    b = input('Digite as propsições compostas: ')
    print(ttg.Truths(eval(a),eval(b)))
    print('             Programa obtido de: https://pypi.org/project/truth-table-generator/             \n')
    print('                 Versão Adaptada: Allan de Sousa Soares - IFBA VDC                    ')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    input('Digite Enter para continuar: ')


