'''
Condições if, elif e Else - Aula 4
'''
# IF (se) se essa ação for verdadeira executa esse codigo abaixo mais é falsa
cont=n0
id = (int(input("Digite um numero: ")))
if(id>=15 and id < 18 ):
        print("Voce pode votar mas não é obrigatorio")
        cont = +1

elif(id>=18):
    print("Obrigatorio votar")
    cont = +1

elif(id<15):
    print("Não pode votar")
    cont = +1

while(id>=0):

    id= (int(input("Digite um numero: ")))

    if (id >= 15 and id < 18):
        print("Voce pode votar mas não é obrigatorio")
        cont = +1

    elif (id >= 18):
        print("Obrigatorio votar")
        cont =+1
    elif (id <= 16):
        print("Não pode votar")
        cont = +1
    if(id==0):
        print(f"{cont}")
        break