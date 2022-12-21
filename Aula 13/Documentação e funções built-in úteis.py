#isnumeric isdigit isdecimal

num = input('Digite um número: ')
num2 = input('Digite um número: ')

if num.isdigit() and num2.isdigit():
    pass # o id.digit transforma as strings em numeros

    num = int(num)
    num2 = int(num2)
    print(num + num2)
else:
    print('Não pôde converter!!')
# Esse buit-in úteis serve para converter numeros e varias outraas coisas