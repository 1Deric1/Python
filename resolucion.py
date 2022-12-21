user_bd = list()
for qtdv in range(0,1):
     user_bd.append(str(input("Cadastre o usuario: ")))

senha_db = list()
for num in range(0,1):
    senha_db.append(str(input("Cadastre a senha: ")))

user = []
senha = []
user.append(str(input("Digite o Úsuario: ")))
senha.append(str(input("Digite uma Senha: ")))

if (user_bd == user and senha_db == senha):
    print("logado!")
else:
    print("Erro ao logar!!")