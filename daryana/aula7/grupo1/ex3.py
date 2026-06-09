print ("-----Aumento de Salário---------")
salatual = float(input("Qual é o seu salário atual?: "))
print(input("voce receberá um aumento de 21% em seu salário"))

porcet = 21
salnovo = salatual * (1 + porcet/100 )
print (f"seu salario novo é de {salnovo:.2f} reais")