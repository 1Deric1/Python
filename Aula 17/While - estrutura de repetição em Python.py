'''
while em Python - Aula 7
utilizado para realizar ações enquanto
uma condição for verdadeira
Requisitos: Entender condições e operadores
'''
# while True:
#    nome = input('Qual seu nome? ')
#    print(f'Olá {nome}!')
# else:
#    print('Nao sera executada')
import os

'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break termina a linha
        # continue nao executa a proxima linha dentro de while


    print(x)
    x = x + 1
print('acabou!!')
'''
'''
x = 0 # coluna
while x < 10:
    y = 0 # linha
    while y < 5:
        print(f'X({x}, Y{y})')
        y += 1

    x += 1 #x = x +1
print('acabou')
'''
'''
#Calculadora
while True:
    print()
    n1 = input('Digite um numero: ')
    op = input('Digite um operador: ')  # + - / *
    n2 = input('Digite outro numero: ')
    sair = input('Deseja sair? [s]im ou [n]ão ')

    if sair == 's':
        break

    # + - / *

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um numero!')


    n1 = int(n1)
    n2 = int(n2)

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '*':
        print(n1 * n2)
    else:
        print('Operador invalido!')
'''

while True:
    user = input('Digite um usuario: ')
    senha = input('Digite a senha: ')
    user_bd = 'Deric'
    senha_bd = 'Deric123'
    if user == user_bd and senha == senha_bd:
        print('Bem vindo vc esta logado!')
        os.startfile('mspaint')
    else:
        print('Erro usuário ou senha invalidos!')
    sair = input('Deseja sair? [s]im [n]ão: ')
    if sair == 's':
        break


