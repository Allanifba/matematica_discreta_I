#Programa que converte um número na base b, b não maior que 36 para base 10.
#Leia os COMENTÁRIOS de cada linha marcada com #(*) ao final do código.

def base_to_dec(num_str,base):                      #(1)
    num_str = num_str[::-1]                         #(2)
    num = 0                                         #(3)
    for k in range(len(num_str)):                   #(4)
        dig = num_str[k]                            #(5)
        if dig.isdigit():                           #(6)
            dig = int(dig)                          #(6.1)
        else:
            dig = ord(dig.upper())-ord('A')+10      #(6.2)
        num += dig*(base**k)                        #(7)
    return num                                      #(8)

print('\n***************************************DESCRIÇÃO****************************************')
print('Programa que converte um número de uma base b, b não maior que 36, para a base 10')          #(9)
print('*************************************ENTRADA DE DADOS*************************************')
num_str = input('Digite o número na base b: ')                                                      #(10)
base = int(input('Digite a base b no qual o número está: '))                                        #(11)
resposta=base_to_dec(num_str,base)                                                                  #(12)
print('**************************************SAÍDA DE DADOS**************************************')                             #(idem 10)
print(f'A conversão de {num_str} na base {base} para a base 10 é {resposta}.')                      #(13)
print('\n             Autoria: Allan de Sousa Soares - IFBA VDC             ')
print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

'''
print('\n***************************************DESCRIÇÃO****************************************')
print('Programa que converte um número da base 10 para uma base qualquer b, b não maior que 36.')   
print('*************************************ENTRADA DE DADOS*************************************')
num_str = input('Digite um número na base 10: ')                                                 
base = int(input('Digite a base a qualquer deseja converter o número: '))                           
resposta=dec_to_base(num,base)                                                                      
print('************************SAÍDA DE DADOS************************')                             
print(f'A conversão de {num} na base 10 para a base {base} é {resposta}.')                          
print('\n             Autoria: Allan de Sousa Soares - IFBA VDC             ')
print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

*********************************************COMENTÁRIOS*********************************************
(1) Corresponde à função que executará o processo de conversão quando chamada. 
(2) Comando que reverte o número digitado trocando a ordem dos seus dígitos. Ex: 124 ---> 421
(3) Variável que receberá as somas das parcelas do número a ser convertido.
(4) Comando que repetirá um processo enquanto('while') uma condição for atendida
(5) Toma o dígito da posição k de um número, k começando de 0. Ex. num_str = 2485 ---> num_str[0] = 2, 
    num_str[2] = 8
(6) O 'if' se divide em duas partes: 
    (6.1) se o dígito for um número de 0 a 9 então toma a string correspondente a ele como sendo um
    inteiro (para poder ser operada a seguir)
    (6.2) se o dígito for uma letra A(=10), B(=11), etc, então o comando 'ord(dig.upper())-ord('A')+10'
    o converte para o valor correspondente à letra. Ex: ord('B'.upper())-ord('A')+10 = 11,
    ord('F'.upper())-ord('A')+10 = 15, em que o primeiro valor entre aspas pode ser uma das letras,
    A(=10), B(=11), ..., Z(=35).
(7) Adiciona, em cada etapa do while k, o valor dig*(base**k) ao valor à variável num. 
    Ex: 123_7 = 3*7**0 + 2*7**1 + 1*7**2 em
    que cada uma dessas parecelas 3*7**0, 2*7**1 e 1*7**2 é adicionada à variável 'num' em um passo
    do 'while'. Para k=0 adciona-se 3*7**0, para k=1 adiciona-se 2*7**1, para k=2 adiciona-se 1*7**2.
    Notou porque o passo (2) foi importante?
(8) O processo termina armazenando a variável 'num'
(9) O comando 'print('...')' exibe na tela valores que o usuário irá ler durante a execução
(10) O comando 'input' solicita que o usuário insira um valor, entendido inicialmente como uma
    string
(11) O comando 'input' solicita que o usuário insira um valor, entendido inicialmente como uma
    string mas convertido para inteiro 'int'
(12) A variável 'resposta' recebe o valor advindo como comando 'dec_to_base(num,base)' tomando 
    as variáveis 'num_str' e 'base' inputadas pelo usuário. O comando 'dec_to_base(num,base)' chama a
    função que executará todo o processo de conversão.
(13) O comando 'print(f'..')', com f antes das aspas internas permite que se mescle texto e variáveis
    desde que as variáveis estejam dentro de chaves { }
*****************************************************************************************************
'''