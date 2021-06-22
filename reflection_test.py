lista = ['hola', 'como', 'estas']

string = 'hola como estas'

for lista_value in lista:
    if lista_value in string:
        print('Hallo')

values = list([val in string for val in lista])
print(all(values))
