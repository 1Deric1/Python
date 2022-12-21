# #definindo a função
# def test():
#     print("Ola mundo")
#
# #chamando a função
# test()

#vetor de outra forma


user_bd = []
for qtdv in range(0,2):
     user_bd.append(str(input("Cadastre o usuario: ")))
for ps, v in enumerate(user_bd):
    print(f"{v} está na posição {ps}")
print(f"{user_bd}")