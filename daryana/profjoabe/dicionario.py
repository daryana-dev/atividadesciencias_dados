lista = []
dicionario = {}
gírias = { 'gambiarra:', 'solução improvisada' , 'treta:' "confusão"}
alimentos = dict(goiaba='fruta' , abobora='legume' , feijão = 'grão')

capitais={
    "Brasil":"Brasília", "Rússia": "Moscou" , "Italia": "Roma"
}
print(capitais["Brasil"])
#adicionar
capitais['China'] = 'Xangai'
#alterar
capitais['china'] = 'Pequim'
#imprimir
print(capitais)
#apagar
del capitais ['Italia']
#pegar item inexistente
#print(capitais["india"])
print (capitais.get('India'))
#listas
países = capitais.keys()
cidades = capitais.values()
print(países)
print(cidades)
#interação - percorre
for pais in capitais:
    print('Bem - vindo a' ,pais)
for pais, cidade in capitais.items():
    print(cidade, "é a capital de", pais)

npc = {
    'classe': 'mago', 
}
