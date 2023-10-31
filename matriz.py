o=0
while o==0:
    lin = int(input("A quantidade de linhas da matriz é: "))
    col = int(input("A quantidade de colunas da matriz é: "))
    matriz=[]
    def criarMatriz(lin, col):
        for i in range(lin):
            a=[]
            for j  in range(col):
                val=int(input(f"Insira o valor de {i},{j}: "))
                a.append(val)
            matriz.append(a)

    criarMatriz(lin , col)

    def mostrarMatriz():
        for lin in (matriz):
            print(lin)

    def DiagonalPrincipal(lin,col):
        for i in range(min(lin,col)):
            print(matriz[i][i])
            
    def DiagonalSecundaria(lin,col):
        for i in range(min(lin, col)):
            print(matriz[i][col -1 -i])


    for i in range(3):
        a=int(input('Selecione as opções:1 = Mostrar Matriz, 2 = Diagonal Principal e 3 = Diagonal Secundária: '))
        if a==1:
            print("Opção 1: Essa é a matriz!")
            print(mostrarMatriz())
            
        if a==2:
            print("Opção 2: Essa é a diagonal principal!")
            print(DiagonalPrincipal(lin, col))
            
        if a==3:
            print("Opção 3: Essa é a diagonal secundária!")
            print(DiagonalSecundaria(lin, col))
            
    o=int(input('Deseja recomeçar? \n'))
    if o==1:
        print("Obrigado pela atenção ^^")
 
