import random
from time import sleep


def menu():
    print('*=*='*21,'\n')
    titulo = 'JOGO DA MEMÓRIA'
    print(titulo.center(84),'\n')
    print('*=*='*21,'\n')
    print('''MENU

(1)- JOGAR
(2)- ESCOLHER O NÍVEL DE DIFICULDADE
(3)- VER PONTUAÇÃO
(4)- CONTINUAR JOGO EXISTENTE
(5)- SAIR
''')
    #Todas as partes de interação com o usuário tem tratamento de erro.
    sair = True
    while sair:
        try:
            opcao = input('Insira a opção que deseja: ')
            numero = int(opcao)
            if (numero>=1 and numero<=5):
                sair = False
        except:
            print('O valor digitado deve ser um inteiro entre 1 e 5')
            opcao =('Insira a opção que deseja: ')
    print()
    print('*=*='*21,'\n')
    return numero

def verificador(m,m2,c):#matriz, matriz[linha][coluna],tamanho da coluna
    cont = 0
    for linha in range(0,c):
        for coluna in range(0,c):
            if (m[linha][coluna]==m2):
                cont+=1
    if (cont>2):
        return True  #varre a matriz obtida nas funçoes de nivel e retorna true ou false
                    # se retorna true a o while da funcao de nivel continua atuando
                    #assim é garantido que só terá 2 numeros iguais na matriz
    else:
        return False
                            
            
def nivel1(): #função do nível
    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print ('   C1 C2 C3 C4 ')
    print()
    for linha in range(0,4):
        print(f'L{linha+1}',end = '  ')
        for coluna in range(0,4):
            matriz[linha][coluna]=random.randint(1,8) #sorteia o elemento
            while (verificador(matriz,matriz[linha][coluna],4)):
                matriz[linha][coluna]=random.randint(1,8) #enquanto a matriz tiver mais de 2 numeros iguais ele vai sortear um novo numero
            print(matriz[linha][coluna],end ='  ')
        print('\n')
    return matriz

def nivel2():
    matriz=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    print('    C1  C2  C3  C4  C5  C6 ')
    print()
    for linha in range(0,6):
        print(f'L{linha+1}',end='  ')
        for coluna in range(0,6):
            matriz[linha][coluna]=random.randint(1,18)
            while (verificador(matriz,matriz[linha][coluna],6)):
                matriz[linha][coluna]=random.randint(1,18)
            if (matriz[linha][coluna]>=10):
                print(matriz[linha][coluna],end ='  ')
            else:
                print(f' {matriz[linha][coluna]}',end='  ')    
        print('\n')
    return matriz

def nivel3():
    matriz=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    print('    C1  C2  C3  C4  C5  C6  C7  C8')
    print()
    for linha in range(0,8):
        print(f'L{linha+1}',end='  ')
        for coluna in range(0,8):
            matriz[linha][coluna]=random.randint(1,32)
            while (verificador(matriz,matriz[linha][coluna],8)):
                matriz[linha][coluna]=random.randint(1,32)
            if (matriz[linha][coluna]>=10):
                print(matriz[linha][coluna],end ='  ')
            else:
                print(f' {matriz[linha][coluna]}',end='  ')    
        print('\n')
    return matriz

def matrizSelecao(l1,c1,l2,c2,mat1,mat2,n=1,m=1):#linha1,coluna1,linha2,coluna2,matriz[l1][c1],matriz[l2][c2],nivel,matriz
    if m ==1: #cria uma matriz nova zerada
        if (n==1):
            matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        elif(n==2):
            matriz=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
                [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] 
        elif(n==3):
            matriz=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    else:
        matriz = m #matriz ja existente
        
    matriz[l1][c1]=mat1   #passa matriz[l1][c1] para a matriz zerada
    matriz[l2][c2]=mat2  #passa matriz[l2][c2] para matriz zerada

    for c in range(len(matriz)):      #printa a nova matriz 
        print(f'   C{c+1}',end='')
    print()
    for l in range(0,len(matriz)):
        print(f'L{l+1} ', end='')
        for c in range(0,len(matriz)):
            if (matriz[l][c]>=10):
                print(matriz[l][c],end='   ')
            else:
                print(matriz[l][c],end='    ')
        print('\n')
    return matriz

def jogar(n=1,pontuacao=0,matriz=[],matriz2=[]):
    print('*=*='*21,'\n')
    titulo = 'REGRAS DO JOGO'
    print(titulo.center(84),'\n')
    print('''1 - Cada acerto você ganha 1 ponto
2 - Cada erro você perde 1 ponto

EXEMPLO Posição do valor 3:

    C1 C2 C3 C4
L1  3  0  0  0 
L2  0  0  0  0 
L3  0  0  0  0
L4  0  0  0  0
PARA ACESSAR O VALOR 3 L=1 E C=1''')
    sleep(5)    
    print('Você tem 10 segundos para memorizar a sequencia...')
    print()
    if (matriz==[]):  # se o jogo é novo acessa as funcoes de nivel e cria uma sequencia de elementos nova
        if (n == 1):
            matriz = nivel1()
        elif (n==2):
            matriz = nivel2()
        elif(n==3):
            matriz = nivel3()
    else:
        matriz = mostrarMatriz(matriz) # se o jogo é continuado utiliza a matriz criada anteriormente
        
    print()
    sleep(3)
    for c in range (1,11):
        sleep(1)
        print(c,end= '... ') # printa os 10s
    for cont in range(50):
        print()
    while True:  # tratamento de erro recebendo valores do usuario
        try:
            print('Insira as coordenadas da linha e coluna onde estão os pares!!')
            l1 = int(input('Linha 1 :L '))-1          
            c1 = int(input('Coluna 1 :C '))-1
            l2 = int(input('Linha 2 :L '))-1
            c2 = int(input('Coluna 2 :C '))-1
            print()
            if (l1==l2 and c1==c2):
                print('Digite posições diferentes!!')
                continue
            elif(matriz2!=[] and matriz2[l1][c1]==0 and matriz2[l2][c2]==0):
                sele = matrizSelecao(l1,c1,l2,c2,matriz[l1][c1],matriz[l2][c2],n,matriz2)  # se o jogo esta sendo continuado coloca a matriz de zeros como
                                                                                            #parametro
            elif matriz2==[]:
                sele = matrizSelecao(l1,c1,l2,c2,matriz[l1][c1],matriz[l2][c2],n) #se o jogo é novo cria matriz nova zerada
            else:
                print('Esse valor já tem par, digite outro valor!')
                continue
                
        except ValueError:
            print('Opção Inválida!!')
            continue
        except IndexError:
            print('Não existe essa linha e essa coluna, insira valores válidos!')
            continue
        while True:
            try :
                quer = int(input ('Deseja continuar jogando? [1] - sim, [2] - Não: '))
            except ValueError:
                print('Digite [1] para continuar jogando e [2] para parar!!! ')
                continue
            else:
                break 
        if (matriz[l1][c1]==matriz[l2][c2]): #soma 1 na pontuacao e atualiza a matriz de zeros guardando os acertos
            pontuacao+=1
            matriz2=sele[:]
            matriz2[l1][c1]==matriz[l1][c1]
            matriz2[l2][c2]==matriz[l2][c2]
            
        elif(matriz[l1][c1]!=matriz[l2][c2] and matriz2!=[]): #subtrai 1 na pontuacao e atualiza matriz de zeros colocando 0 no lugar do erro
            matriz2[l1][c1]=0
            matriz2[l2][c2]=0
            pontuacao-=1
        else: # se a pessoa errou mas é a primeira jogada atualiza pontuação subtraindo 1
            pontuacao-=1
        if (quer !=1):
            break
    print(f'Sua pontuacao foi de {pontuacao} pontos')
    while True:  # função que salva o jogo
        try:
            salvar = int(input('Deseja salvar seu jogo?[1]-Sim [2]-Não: '))
        except ValueError:
            print('Digite um numero entre 1 e 2!!')
            continue
        else:
            if (salvar==1): #abre o arquivo que salva a matriz sorteada, a matriz de 0 e a pontuacao
                nome = str(input('Insira o nome que você quer que seu jogo salvo tenha: '))
                arq = open(nome+'.txt','w')
                arq.write(f'{matriz}\n')
                arq.write(f'{matriz2}\n')
                arq.write(f'{pontuacao}\n')
                arq.close()
                arq2 = open('Jogos Salvos.txt','a') #arquivo com uma lista dos arquivos de jogos salvos
                arq2.write(f'{nome}.txt'+'\n')
                arq2.close()
                break
            else:
                break
    
def verPontuacao(): # função que acessa o arquivo 
    j ='JOGOS SALVOS'
    print(j.center(84),end='\n')# acessa o arquivo que tem todos os nomes dos arquivos de jogos salvos
    print('*=*='*21,'\n')
    arq = open('Jogos Salvos.txt','r')
    l = arq.readline()  # transforma o conteudo em uma lista para facilitar a busca 
    c = 1
    lista=[]
    while (l!=''):
        print(f'{c} - {l}',end='\n')
        lista.append(l)
        c+=1
        l=arq.readline()
     
    while True:
        try :
            opcao = int(input('Insira o numero do arquivo que você deseja ver a pontuação: '))
        except ValueError:
            print('Opção inválida!!')
            continue
        except IndexError:
            print('Opção inválida!!')
        else:
            break
    lista2=[]  # acessa a pontuacao atraves da lista 1
    jogo = str(lista[opcao-1]) 
    jogo1= jogo.split('\n') #retira o \n 
    jogo2=str(jogo1[0]) #transforma em string para abrir o arquivo
    arq2 = open(f'{jogo2}','r')
    l2 = arq2.readline()
    while (l2!=''):
        lista2.append(l2)
        l2=arq2.readline()
    pont=int(lista2[2])
    arq2.close()
    arq.close() #transforma o conteudo em outra lista e pega o elemento 3 que é o da pontuação
    print(f'Pontuação {jogo2}: {pont}')
    
def continuarJogo():
    j ='JOGOS SALVOS'
    print(j.center(84),end='\n')
    print('*=*='*21,'\n')
    arq = open('Jogos Salvos.txt','r') # faz a mesma coisa que a função anterior com o arquivo jogos salvos
    l = arq.readline()
    c = 1
    lista=[]
    while (l!=''):
        print(f'{c} - {l}',end='\n')
        lista.append(l)
        c+=1
        l=arq.readline()
     
    while True:
        try :
            opcao = int(input('Insira o numero do arquivo que você deseja continuar: '))
        except ValueError:
            print('Opção inválida!!')
            continue
        except IndexError:
            print('Opção inválida!!!')
            continue
        else:
            break
    
    jogo = str(lista[opcao-1])
    jogo1= jogo.split('\n')#mesma coisa da função anterior
    jogo2=str(jogo1[0])
    arq2 = open(f'{jogo2}','r')
    #primeira matriz
    m=arq2.readline()
    m1=m.split('\n') #separa a matriz sorteada em string
    matriz=m1[0]
    #segunda matriz
    n=arq2.readline()
    n1=n.split('\n') #separa a matriz de zeros em string
    matriz2=n1[0]
    #pontuacao
    pont=arq2.readline()
    pontuacao=int(pont) # separa a pontuação 
    return matriz,matriz2,pontuacao

def transMatriz(n):#transforma as matrizes que estão em string em matrizes novamente 
    strin1 = n.replace('[','').replace(']','')#retira os espaços e os colchetes
    l = strin1.split(',')
    l2=[]
    lista=[]
    for cont in range(0,len(l)):
        l2.append(int(l[cont]))#deixa tudo em uma lista grande
    if (len(l2)==16):#dependendo do tamanho da lista grande da um n que vai separar essa lista em lista de listas
        n=4
    elif(len(l2)==36):
        n=6
    elif(len(l2)==64):
        n=8
    for cont in range(0,len(l2),n):
        lc = l2[cont:cont+n] #utiliza o fatiamento para transforma a lista grande em uma lista de listas 
        lista.append(lc)
    return lista        

def mostrarMatriz(m):#funcao printa a matriz recuperada
    n = 0
    if (len(m)==4):
        n = 4
        c = 'C1   C2   C3   C4'
    elif(len(m)==6):
        n = 6
        c = 'C1   C2   C3   C4   C5   C6'
    elif(len(m)==8):
        n=8
        c='C1   C2   C3   C4   C5   C6   C7   C8'
    if n!=0:
        print(f'    {c}')
        for l in range(0,n):
            print(f'L{l+1}',end='  ')
            for c in range(0,n):
                if (m[l][c]>=10):
                    print(m[l][c],end='   ')
                else:
                    print(m[l][c],end='    ')
            print('\n')
    return m

def main():
    while True:
        m = menu()
        if (m == 5):
            titulo = 'Até mais, e obrigado pelos peixes!!!'
            print(titulo.center(84),'\n')
            print('*=*='*21,'\n')
            break
        elif (m==1):
            jogo = jogar() 
            sleep(2)
        elif (m==2):
            nivel = 'NIVEIS DISPONÍVEIS'
            print(nivel.center(84),'\n')
            print('''[1] - 4 linhas 4 colunas
[2] - 6 linhas e 6 colunas
[3] - 8 linhas e 8 colunas ''')
            while True:
                try:
                    n = int(input('Insira o nivel que deseja jogar: '))
                    j = int (input ('Deseja jogar agora?  [1]-Sim [2]-Não'))
                except ValueError:
                    print('Opção inválida, insira um numero entre 1 e 3!')
                    continue
                else:
                    break
            if (j==1):
                jogo = jogar(n) #utiliza a matriz jogar mas com o nível selecionado
        elif(m==3):
            pont = verPontuacao()
        elif(m==4):
            contJogo = continuarJogo() #transforma em tupla o conteudo do arquivo
            m1=transMatriz(contJogo[0]) #matriz sorteada
            m2=transMatriz(contJogo[1]) #matriz de zeros
            pont=contJogo[2] #pontuação
            jogo = jogar(pontuacao=pont,matriz=m1,matriz2=m2) #funçao jogar com as matrizes recuperadas
            
main()         
            
        
            

