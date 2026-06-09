print('----------QUER SABER SE VOCê JA PODE VOTAR?--------------')
idade = int(input('qual é a sua idade atualmente?: '))

if idade >= 18:
    print('você ja tem idade o suficiente para votar, tire  seu titulo')
else:
    print('Você ainda não possui idade o suficiente, estude para não vender o seu voto')