while True:
    user = input('Digite um usuario: ')
    senha = input('Digite a senha: ')
    sair = input('Deseja sair? [s]im [n]ão: ')
    user_bd = 'Isabele'
    senha_bd = 'Isabele123'
    if sair == 's':
        break
    if user == user_bd and senha == senha_bd:
        print('Bem vindo vc esta logado!')
    else:
        print('Erro usuário ou senha invalidos!')

