while True:
	nome = input('Digite o usuario: ')
	senha = input('Digite a senha: ')
	nome_bd = 'Deric'
	senha_bd = 'deric14s'
	if nome_bd == nome and senha == senha_bd:
		print('Você está logado')
	else:
		print('Erro no login')
	sair = input('Deseja sair?')
	if sair == 's':
		break
