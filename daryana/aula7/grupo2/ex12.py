print('----------Maior de tres--------')
print(input('voce vai digita tre numeros para jogarmos esse game'))
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'o primeiro numero é maior que todos. numero {n1}')
elif n2 > n1 and n2 > n3:
    print(f'o segundo numero é maior que todos. numero {n2}')
else:
    print(f'o terceiro  numero é maior que todos. numero {n3}')


