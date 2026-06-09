'''#enquanto: while
lista_aluno = []
while True:
    aluno = input('digite o aluno: ')
    if aluno == 'sair':
        break
    print(aluno)
    lista_aluno.append(aluno.capitalize())
    print(lista_aluno)
    
#continução
while True:
    numero = float(input('digite um numero: '))
    if numero == 0:
        break
    # % esse sinal tambem serve pra fazer comparação
    if numero % 2 == 0:
        continue
    print(numero, 'é impar')
    
# interação - for
palavra = 'paralellepípedo' # 14
for letra in palavra: 
    if letra == 'd':
        break
    print(letra)
    if letra == 'l':
        continue
    print(letra)'''
    
# import bibliotecas
import random
soma = 0
for dafo in range(0, 3):
    soma += random.randint(1, 6)
    if soma < 6:
        print('falha')
    elif soma >= 6 and soma <= 12:
        print('sucesso')
    else:
        print('betinha moggado')
        
#dungeon 
itens = ['espada' , 'poção' , 'escudo' , 'cajado' , 'mapa' , 'armadura' , 'tesouro' , 'nothing' , 'se passando' , 'poção duvidosa']
random.shuffle(itens)
escolha = int(input('escolha 0-9'))
print(itens[escolha])