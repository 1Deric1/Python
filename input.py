nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? ')) #int
ano_atual = int(input('Qual o ano atual? '))
altura = float(input('Qual sua altura? ')) #float
nasc1 = int(input('Qual o seu mês de nascimento? '))
nasc = int(ano_atual- 1 - idade )
peso = float(input('Qual seu peso? '))
imc = float(peso // (altura**2))
l_idade = 18
dia = input('Qual o dia do seu Aniversario?')
print(f'{nome} você tem {altura} metros altura e nasceu no dia {dia} do {nasc1} de {nasc}.')
print(f'Pesa {peso} e seu imc é {imc} kg. ')
if l_idade <= idade:
   print(f'{nome} você tem {idade} anos  e é maior de idade!')# maior
else:
    print(f'{nome} você tem {idade} anos e é menor de idade!') #menor