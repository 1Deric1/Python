'''
:s Texto (Strings)
:d Inteiros (Int)
:f Numeros de ponto flutuante (Float)
:. (NUMERO)f quantidade de casas decimais (Float) #printf'{variavel:.2f}'
:(CARACTERE)(> ou < ^)(QUANTIDADE)(TIPO - s, d ou f ) Preenche com a quantidade de numeros adicionada (f'{var:0>10}')
>-Esquerda
<-Direito
^-Centro
'''

n = 10
n1 = 3
n2 = n / 3
print(f'{n2:.1f}')

nome = 'Deric'
n1 = (f'{nome:s}')
print(n1)

no = 1
n1 = (f'{no:0^10}')
print(n1)

nome = 'deric'
n = (len(nome))
n1 = (f'{n:#^10}')
print(n1)

nf = 'Deric'
print('{:@^11}'.format(nf))

nome = 'deric'
nome = nome.ljust (25,  '%')
print(nome)

nome1 = ('Deric')
print(nome1.lower()) # Menusculo
print(nome1.upper()) # Maiusculo
print(nome1.title()) # Primeiras letras maiusculas
