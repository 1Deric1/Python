
from re import S


while True:
    user = input('Digite o usuario: ')
    senha = input('Digite a senha: ')
    user_bd = 'Deric'
    senha_bd = '1234'
    sair = input('Dejesa sair? [s]im [n]ão: ')
    if sair =='s':
     break
    elif user == user_bd and senha == senha_bd:
        import os
        os.startfile('mspaint')
    else:
        print('Usuario ou Senha inválidos! ')
    
       
















