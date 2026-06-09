print('=================SENHA FORTE=======================')
senha = input('digite uma senha com 8 caracteres, pelo menos um numero okay?:  ')
temnumero = False
temmaiuscula = False

if len(senha)< 8:
    print('senha muito beta')
else:
    for caracteres in senha:
        if caracteres.isupper():
         tem_maiuscula = True
if not temmaiuscula:
    print('erra nã tem maiuscula')
elif not temnumero:
    print('error beta cade o 67')
else:
    print('essa senha é farmador de aurea')