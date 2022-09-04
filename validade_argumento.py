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
          "Por exemplo, para o cálculo do valor do argumento\n"
          "                                 'p or q'     (premissa 1)\n"
          "                                 '~p or r'    (premissa 2)\n"
          "                                 ________\n"
          "                                 'q or r'     (conclusão)\n"
          "digite:\n"
          "['p', 'q','r'] na primeira entrada (proposições simples) e\n"
          "['((p or q) and ((~p) or r))=>(q or r)'] na segunda entrada (condicional da conjunção dos \n"
          "argumentos pela conclusão). Em particular, o exemplo em questão trata-se de um argumento\n"
          " válido correspondendo à regra Resolução. Note que ~p deve ser digitada como (~p).\n")
    print('****************************************SAÍDA DE DADOS*****************************************')
    a = input('Digite as proposições simples: ')
    b = input('Digite a condicional da conjunção dos argumentos pela conclusão: ')
    print(ttg.Truths(eval(a),eval(b)))
    table_val = ttg.Truths(eval(a),eval(b))
    if str(table_val.valuation()) == 'Tautology':
        print('O argumento é válido.\n')
    if str(table_val.valuation()) == 'Contingency':
        print('O argumento não é válido.\n')
    if str(table_val.valuation()) == 'Contradiction':
        print('O argumento não é válido.\n')
    print('             Programa obtido de: https://pypi.org/project/truth-table-generator/             \n')
    print('                 Versão Adaptada: Allan de Sousa Soares - IFBA VDC                    ')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    input('Digite Enter para continuar: ')