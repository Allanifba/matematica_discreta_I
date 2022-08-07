#Programa que converte um número na base 10 para uma base b, n não maior que 36.
#Leia os COMENTÁRIOS de cada linha marcada com #(*) ao final do código.

while True:
    def dec_to_base(num,base):                          #(1)
        base_num = ""                                   #(2)
        while num>0:                                    #(3)
            dig = int(num%base)                         #(4)
            if dig<10:                                  #(5)
                base_num += str(dig)                    #(5.1)
            else:
                base_num += chr(ord('A')+dig-10)        #(5.2)
            num //= base                                #(6)
        base_num = base_num[::-1]                       #(7)
        return base_num                                 #(8)

    print('\n***************************************DESCRIÇÃO****************************************')
    print('Programa que converte um número da base 10 para uma base qualquer b, b não maior que 36.')   #(9)
    print('*************************************ENTRADA DE DADOS*************************************')
    num = int(input('Digite um número na base 10: '))                                                   #(10)
    base = int(input('Digite a base a qualquer deseja converter o número: '))                           #(idem 10)
    resposta=dec_to_base(num,base)                                                                      #(11)
    print('**************************************SAÍDA DE DADOS**************************************') #(idem 10)
    print(f'A conversão de {num} na base 10 para a base {base} é {resposta}.')                          #(12)
    print('\n                       Autoria: Allan de Sousa Soares - IFBA VDC                        ')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    input('Digite Enter para continuar: ')

    '''
    *********************************************COMENTÁRIOS*********************************************
    (1) Corresponde à função que executará o processo de conversão quando chamada.  
    (2) Campo vazio para receber uma string (palavra, letra)
    (3) Comando que repetirá um processo enquanto('while') uma condição for atendida
    (4) 'dig' recebe o resto da divisão de 'num' por 'base'
    (5) O 'if' se divide em duas partes: 
        (5.1) caso o valor encontrado no passo anterior seja menor que 10
        ele é tomando como uma string normalmente (10 como palavra)
        (5.2) caso ele seja igual ou maior
        que 10 então ele é repassado para uma das letras A, B, C,... Por exemplo, 
                    A + 13 - 10 = A + 3 = D
    (6) Repete o processo com o novo quociente
    (7) Toma a palavra obtida na ordem inversa. Note que, por exemplo, o valor '1AF' não é entendido
        como um número pelo programa mas sim uma palavra que para nós é um número.
    (8) O processo 'while' para e o valor do número convertido 'base_num' é armazenado
    (9) O comando 'print('...')' exibe na tela valores que o usuário irá ler durante a execução
        do programa
    (10) O comando 'input' solicita que o usuário insira um valor, entendido inicialmente como uma
        string mas convertido para inteiro 'int'
    (11) A variável 'resposta' recebe o valor advindo como comando 'dec_to_base(num,base)' tomando 
        as variáveis 'num' e 'base' inputadas pelo usuário. O comando 'dec_to_base(num,base)' chama a
        função que executará todo o processo de conversão.
    (12) O comando 'print(f'..')', com f antes das aspas internas permite que se mescle texto e variáveis
        desde que as variáveis estejam dentro de chaves { }
    *****************************************************************************************************
    '''
