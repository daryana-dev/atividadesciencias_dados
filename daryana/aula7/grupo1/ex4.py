print (input("------------Ganhe desconto de 10% nos livros----------"))
a = float(input('Qual o valor do seu livro?:  '))
desc = 10
novalor = a - (a * desc/100)
print(f" o novo valor do seu livro sera de {novalor:.2f}")