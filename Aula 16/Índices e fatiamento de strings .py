'''
Manipulando strings - Aula 6
* String indices 
* Fatiamento de string [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''
# indices positivos [012345678] entt eu posso imprimir qualquer letra de acordo com os numeros de 0 a 8
texto  =            'Python_s2'
print(texto[:])
# indices negativos -[987654321]
#url = 'www.google.com.br/'
#print(url[:-1])
#ns = (texto[0:9])# o 6 nao é incluido va ate o 5 sempre um a menos de onde começa : a onde termina.
#ns1 = (texto[:])# o zero não precisa escrever entt vai zero [- onde começa:- onde termina]
#ns1 =texto[0:9:2]# [o zero é de onde e começo : o nove é de onde eu termino : e o dois eu quero q ele pule de 2 em 2]
#print(ns1)
for letra in texto:
    print(letra)