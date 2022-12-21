'''
numer = input('Digite um número inteiro: ')

if numer.isdigit():
    numer=int(numer)
    if numer % 2 == 0:
        print(f'{numer} é par')
    else:
        print(f'{numer} é impar')
else:
   print('Erro')
'''
'''
numer = input('Digite um numero: ' )

if not numer.isdigit():
    print('isso nao é um numero! ')
else:
    numer = int(numer)
    if numer % 2 == 0:
        print(f'{numer} é par')
    else:
        print(f'{numer} é impar')
'''
'''
hr = input('Digite um hórario: ')
if hr.isdigit():
    hr = int(hr)
    if hr < 0 or hr > 24:
        print('Horario deve estar entre 0 a 24 ')
    else:
        if hr >= 0 and hr <=4 :
             print('Boa noite!')
        elif hr <= 11:
             print('Boa dia!')
else:
    print('Por favor digite um horario de 0 a 23')
'''
nome = input('Digite seu nome: ')
tam = len(nome)

if tam < 4:
    print('Seu nome é curto')
elif tam >= 5 and tam <= 6:
    print('Seu nome é normal ')
elif tam > 6:
    print('Seu nome é grande')