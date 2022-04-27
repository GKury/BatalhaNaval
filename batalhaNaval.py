'''/*
Entrega do Trabalho 02 - Algoritmos e Programação II
Nós,
Abdo Smeili
Gabriel Kury Fonseca
declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
*/'''


import random

def inicializaGrid():
    grid = []
    for i in range(11):
        linha = []
        for j in range(11):
            linha.append('.')
        grid.append(linha)

    for x in range(11):
        grid[0][x] = x
        grid[x][0] = x

    grid[0][0] = " "
    return grid



def posicionar_porta_avioes(grid, linha, coluna, vertical):

    if vertical == False:

        while linha < 1 or linha > 10:
            linha = int(input("Você inseriu um valor inválido para a linha. Insira um valor entre 1 e 10\n"))

        while coluna < 1 or coluna > 6:
            coluna = int(input("Você inseriu um valor inválido para a coluna. Insira um valor entre 1 e 6\n"))
            
        for i in range(coluna, coluna + 5):
            grid[linha][i] = "P"

    if vertical == True:

        while coluna < 1 or coluna > 10:
            coluna = int(input("Você inseriu um valor inválido para a coluna. Insira um valor entre 1 e 10\n"))

        while linha < 1 or linha > 6:
            linha = int(input("Você inseriu um valor inválido para a linha. Insira um valor entre 1 e 6\n"))


           
            
        for j in range(linha, linha + 5):
            grid[j][coluna] = "P"

    return grid



def posicionar_porta_avioes_automatico(grid, linha, coluna, vertical):

    if vertical == False:

        while linha < 1 or linha > 10:
            linha = random.randint(1, 10)

        while coluna < 1 or coluna > 6:
            coluna = random.randint(1, 6)
            
        for i in range(coluna, coluna + 5):
            grid[linha][i] = "P"

    if vertical == True:

        while coluna < 1 or coluna > 10:
            coluna = random.randint(1, 10)

        while linha < 1 or linha > 6:
            linha = random.randint(1, 6)


           
            
        for j in range(linha, linha + 5):
            grid[j][coluna] = "P"

    return grid
        


def posicionar_encouraçado(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 4:
            chave = 0

            while coluna < 1 or coluna > 7 or linha < 1 or linha > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

                
            for i in range(coluna, coluna + 4):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 4:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(coluna, coluna + 4):
            grid[linha][j] = "E"


    chave2 = 0
    if vertical == True:
        while chave2 != 4 or linha < 1 or linha > 7 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 7 or coluna < 1 or coluna > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))


            chave2 = 0
            for i in range(linha, linha + 4):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 4:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(linha, linha + 4):
            grid[j][coluna] = "E"


          
    return grid



def posicionar_encouraçado_automatico(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 4:
            chave = 0

            while coluna < 1 or coluna > 7 or linha < 1 or linha > 10:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 7)

                
            for i in range(coluna, coluna + 4):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 4:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(coluna, coluna + 4):
            grid[linha][j] = "E"


    chave2 = 0
    if vertical == True:
        while chave2 != 4 or linha < 1 or linha > 7 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 7 or coluna < 1 or coluna > 10:
                linha = random.randint(1, 7)
                coluna = random.randint(1, 10)


            chave2 = 0
            for i in range(linha, linha + 4):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 4:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(linha, linha + 4):
            grid[j][coluna] = "E"


          
    return grid
    
                
def posicionar_cruzador(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 3:
            chave = 0

            while coluna < 1 or coluna > 8 or linha < 1 or linha > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

                
            for i in range(coluna, coluna + 3):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 3:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(coluna, coluna + 3):
            grid[linha][j] = "C"


    chave2 = 0
    if vertical == True:
        while chave2 != 3 or linha < 1 or linha > 8 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 8 or coluna < 1 or coluna > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))


            chave2 = 0
            for i in range(linha, linha + 3):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 3:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(linha, linha + 3):
            grid[j][coluna] = "C"


          
    return grid


def posicionar_cruzador_automatico(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 3:
            chave = 0

            while coluna < 1 or coluna > 8 or linha < 1 or linha > 10:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 8)

                
            for i in range(coluna, coluna + 3):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 3:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(coluna, coluna + 3):
            grid[linha][j] = "C"


    chave2 = 0
    if vertical == True:
        while chave2 != 3 or linha < 1 or linha > 8 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 8 or coluna < 1 or coluna > 10:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)


            chave2 = 0
            for i in range(linha, linha + 3):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 3:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(linha, linha + 3):
            grid[j][coluna] = "C"


          
    return grid      
                


def posicionar_submarino(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 2:
            chave = 0

            while coluna < 1 or coluna > 9 or linha < 1 or linha > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

                
            for i in range(coluna, coluna + 2):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 2:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(coluna, coluna + 2):
            grid[linha][j] = "S"


    chave2 = 0
    if vertical == True:
        while chave2 != 2 or linha < 1 or linha > 9 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 9 or coluna < 1 or coluna > 10:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))


            chave2 = 0
            for i in range(linha, linha + 2):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 2:
                print("Você escolheu um local inadequado. Selecione uma nova linha e coluna\n")
                linha = int(input("Nova linha: \n"))
                coluna = int(input("Nova coluna: \n"))

        for j in range(linha, linha + 2):
            grid[j][coluna] = "S"


          
    return grid



def posicionar_submarino_automatico(grid, linha, coluna, vertical):
    chave = 0
    if vertical == False:
        while chave != 2:
            chave = 0

            while coluna < 1 or coluna > 9 or linha < 1 or linha > 10:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 9)

                
            for i in range(coluna, coluna + 2):
                if grid[linha][i] == ".":
                    chave += 1

            if chave != 2:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(coluna, coluna + 2):
            grid[linha][j] = "S"


    chave2 = 0
    if vertical == True:
        while chave2 != 2 or linha < 1 or linha > 9 or coluna < 1 or coluna > 10:
            while linha < 1 or linha > 9 or coluna < 1 or coluna > 10:
                linha = random.randint(1, 9)
                coluna = random.randint(1, 10)


            chave2 = 0
            for i in range(linha, linha + 2):
                if grid[i][coluna] == ".":
                    chave2 += 1

            if chave2 != 2:
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10)

        for j in range(linha, linha + 2):
            grid[j][coluna] = "S"


          
    return grid 
    



def imprime(grid):
    for y in range(11):
        print("\n")
        for k in range(11):
            print(grid[y][k], end = " ")



def atirar(grid, linha, coluna):
    while grid[linha][coluna] == "O" or grid[linha][coluna] == "X" or linha < 1 or linha > 10 or coluna < 1 or coluna > 10:
        linha = int(input("Você selecionou uma região na qual ja atirou ou uma região inexistente\nSelecione outra região\nInsira uma linha\n"))
        coluna = int(input("Insira uma coluna\n"))

    if grid[linha][coluna] == "P" or grid[linha][coluna] == "E" or grid[linha][coluna] == "C" or grid[linha][coluna] == "S":
        grid[linha][coluna] = "X"
    else:
        grid[linha][coluna] = "O"

    countP = 5
    countE = 4
    countC = 3
    countS = 2

    for i in range(11):
        for j in range (11):
            if grid[i][j] == "P":
                countP -=1
            if grid[i][j] == "E":
                countE -=1
            if grid[i][j] == "C":
                countC -=1
            if grid[i][j] == "S":
                countS -=1

    if countP == 5:
        print("\n\nTodos porta-aviões foram destruídos\n")
    if countE == 4:
        print("\nTodos encouraçados foram destruídos\n")
    if countC == 3:
        print("\nTodos cruzadores foram destruídos\n")
    if countS == 2:
        print("\nTodos submarinos foram destruídos\n")
        
    return grid, grid[linha][coluna], linha, coluna            
    

def main():
    grid = inicializaGrid()

    imprime(grid)

    print("\n\n\n")


    linha = int(input("Insira a linha na qual deseja posicionar o Porta-Aviões\n"))
    coluna = int(input("Insira a coluna na qual deseja posicionar o Porta-Aviões\n"))
    vertical = int(input("\nSe deseja colocar o Porta-Aviões na vertical digite 1\n Se deseja colocar o Porta-Aviões na horizontal digite 2\n"))

    while vertical != 1 and vertical != 2:
        vertical = int(input("Você inseriu um valor inválido para posição. Insira 1 para vertical ou 2 para horizontal\n"))
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_porta_avioes(grid, linha, coluna, vertical)
    imprime(grid)


    linha = int(input("\n\nInsira a linha na qual deseja posicionar o encouraçado\n"))
    coluna = int(input("Insira a coluna na qual deseja posicionar o encouraçado\n"))
    vertical = int(input("\nSe deseja colocar o encouraçado na vertical digite 1\n Se deseja colocar o Porta-Aviões na horizontal digite 2\n"))

    while vertical != 1 and vertical != 2:
        vertical = int(input("Você inseriu um valor inválido para posição. Insira 1 para vertical ou 2 para horizontal\n"))
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_encouraçado(grid, linha, coluna, vertical)

    imprime(grid)


    linha = int(input("\n\nInsira a linha na qual deseja posicionar o cruzador\n"))
    coluna = int(input("Insira a coluna na qual deseja posicionar o cruzador\n"))
    vertical = int(input("\nSe deseja colocar o cruzador na vertical digite 1\n Se deseja colocar o cruzador na horizontal digite 2\n"))

    while vertical != 1 and vertical != 2:
        vertical = int(input("Você inseriu um valor inválido para posição. Insira 1 para vertical ou 2 para horizontal\n"))
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_cruzador(grid, linha, coluna, vertical)

    imprime(grid)


    linha = int(input("\n\nInsira a linha na qual deseja posicionar o submarino\n"))
    coluna = int(input("Insira a coluna na qual deseja posicionar o submarino\n"))
    vertical = int(input("\nSe deseja colocar o submarino na vertical digite 1\n Se deseja colocar o submarino na horizontal digite 2\n"))

    while vertical != 1 and vertical != 2:
        vertical = int(input("Você inseriu um valor inválido para posição. Insira 1 para vertical ou 2 para horizontal\n"))
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_submarino(grid, linha, coluna, vertical)

    imprime(grid)

    print("\n\n\n<----------------------------------------------------------------------------->")
    print("\n\nAgora que você posicionou suas embarcações deverá afundar as inimigas\n\n\nAs posições que contém um ponto(.) são possíveis alvos\nAs posições que contém um X marcam os tiros que você acertou\nAs posições que contem um O marcam tiros que você errou\n\nVocê tem direito a 20 tiros\n\n")

    grid = inicializaGrid()

    linha = random.randint(1, 10)
    coluna = random.randint(1, 10)
    vertical = random.randint(1, 2)

    while vertical != 1 and vertical != 2:
        vertical = random.randint(1, 2)
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_porta_avioes_automatico(grid, linha, coluna, vertical)



    linha = random.randint(1, 10)
    coluna = random.randint(1, 10)
    vertical = random.randint(1, 2)

    while vertical != 1 and vertical != 2:
        vertical = random.randint(1, 2)
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_encouraçado_automatico(grid, linha, coluna, vertical)



    linha = random.randint(1, 10)
    coluna = random.randint(1, 10)
    vertical = random.randint(1, 2)

    while vertical != 1 and vertical != 2:
        vertical = random.randint(1, 2)
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_cruzador_automatico(grid, linha, coluna, vertical)



    linha = random.randint(1, 10)
    coluna = random.randint(1, 10)
    vertical = random.randint(1, 2)

    while vertical != 1 and vertical != 2:
        vertical = random.randint(1, 2)
    
    if vertical == 1:
        vertical = True

    if vertical == 2:
        vertical = False

    grid = posicionar_submarino_automatico(grid, linha, coluna, vertical)


    grid2 = inicializaGrid()


    for i in range(20):
        print("\n\nTiro ", i + 1, "\n")
        imprime(grid2)
        linha = int(input("\n\n\nInsira uma linha na qual deseja atirar\n"))
        coluna = int(input("\nInsira uma coluna na qual deseja atirar\n"))
        grid, res, lin, col = atirar(grid, linha, coluna)
        grid2[lin][col] = res

    print("\n\n\nOs resultados:\n\nSua visão final:\n\n\n")
    
    imprime(grid2)
    
    print("\n\n\nO campo inimigo ao final:\n\n\n")
    imprime(grid)

main()















