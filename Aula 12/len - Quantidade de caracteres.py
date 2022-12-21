'''
num = input('Digite algo:')
num2 = len(num)

if num2 >= 4:
    print('ok',num2)
else:
    print('Nao')
'''
user = input('Digite o Usuário: ')
Senha = input('Digite Senha: ')
num2 = len(Senha)
num3 = len(user)
user1 = 'Deric'
Senha1 = '1234'


if num2 >= 4 and user == user1 and Senha == Senha1 and num3 >= 4:
    print('Ok, vc esta logado ')
else:
    print('Usuarios ou senha invalidos! ')