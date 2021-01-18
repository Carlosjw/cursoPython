'''
    # Funćão Join em Python:
    Usada para transformar uma lista em uma string
'''
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = ','.join(lista)  # Junta todos os elementos da lista separando
# todos com uma vírgula.

print(lista)
print(string2)
