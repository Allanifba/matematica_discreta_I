
while True:
    def soma(x,y,b):
        x = str(x)
        y = str(y)
        if b == 2:
            res=bin(int(x,b) + int(y,b))
            print('Soma = ',res[2:])
        if b == 8:
            res=oct(int(x,b) + int(y,b))
            print('Soma = ',res[2:])
        if b == 16:
            res=hex(int(x,b) + int(y,b))
            print('Soma = ',res[2:])


    def prod(x,y,b):
        x = str(x)
        y = str(y)
        if b == 2:
            res=bin(int(x,b)*int(y,b))
            print('Produto = ',res[2:])
        if b == 8:
            res=oct(int(x,b)*int(y,b))
            print('Produto = ',res[2:])
        if b == 16:
            res=hex(int(x,b)*int(y,b))
            print('Produto = ',res[2:])

    def sub(x,y,b):
        x = str(x)
        y = str(y)
        if b == 2:
            if x>=y:
                res=bin(int(x,b) - int(y,b))
                print('Subtração = ',res[2:])
            else:
                res = bin(int(y, b) - int(x, b))
                print('Subtração = -',res[2:])
        if b == 8:
            if x >= y:
                res = oct(int(x, b) - int(y, b))
                print('Subtração = ',res[2:])
            else:
                res = oct(int(y, b) - int(x, b))
                print('Subtração = -',res[2:])
        if b == 16:
            if x >= y:
                res = hex(int(x, b) - int(y, b))
                print('Subtração = ',res[2:])
            else:
                res = hex(int(y, b) - int(x, b))
                print('Subtração = -',res[2:])

    def div(x,y,b):
        x = str(x)
        y = str(y)
        if b == 2:
            res_q=bin(int(int(x,b)/int(y,b)))
            res_r=bin(int(int(x,b)%int(y,b)))
            print('Elementos da Divisão: ',f'q = {res_q[2:]}, r = {res_r[2:]}')
        if b == 8:
            res_q=oct(int(int(x,b)/int(y,b)))
            res_r=oct(int(int(x,b)%int(y, b)))
            print('Elementos da Divisão: ',f'q = {res_q[2:]}, r = {res_r[2:]}')
        if b == 16:
            res_q=hex(int(int(x,b)/int(y,b)))
            res_r=hex(int(int(x,b)%int(y, b)))
            print('Elementos da Divisão: ',f'q = {res_q[2:]}, r = {res_r[2:]}')
    print('\n****************************************DESCRIÇÃO*****************************************')
    print('Programa que calcula a soma, a subtração, o produto e a divisão de dois números x e y em\n'
          'uma das bases 2, 8 ou 16. ')
    print('*************************************ENTRADA DE DADOS*************************************')
    b1 = input('Digite a base: ')
    x1 = input('Digite o primeiro número: ')
    y1 = input('Digite o segundo número: ')
    print('**************************************SAÍDA DE DADOS**************************************')
    soma(str(x1),str(y1),int(b1))
    sub(str(x1),str(y1),int(b1))
    prod(str(x1),str(y1),int(b1))
    div(str(x1),str(y1),int(b1))
    print('******************************************************************************************')
    print('\n                       Autoria: Allan de Sousa Soares - IFBA VDC                        ')
    print('             Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    input('Digite Enter para continuar: ')
