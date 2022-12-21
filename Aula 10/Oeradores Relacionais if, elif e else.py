

'''
Operadores Relacionas - Aula 4
== igualdade ou pergunta
>= maior que ou igual a
< menor que
<= menor q ou igual a
!= diferente
> maior q
>= maior q ou igual a
'''
'''
var1 = 'Deric'
var2 = 'Santos'
var3 = var1 < var2
print(var3)

# Limite para pegar um emprestimo
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

idade = int(idade)

idade_limite = 18
if idade >= idade_limite:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo.')
'''
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

idade = int(idade)
idade_limite = 18
if not idade_limite :
    print(f'{nome} pode pegar o emprestimo.')
    if 'd' in nome:
        print('Rif')
else:
    print(f'{nome} não pode pegar o emprestimo.')
