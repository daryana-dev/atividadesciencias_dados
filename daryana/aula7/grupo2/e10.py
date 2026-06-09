print('----------SENHA----------')
senha = str(input('defina uma senha para o seu login: '))
print(input('senha definida'))
ver = str(input('digite sua senha novamente: c'))

if senha == ver:
    print('login feito com sucesso')
else:
    print('senha incorreta tente novamente')