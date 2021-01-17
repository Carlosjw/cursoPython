'''
    OPERADORES ARITMÉTICOS:
    + = Adição
    - = Subtração
    * = Multiplicação
    / = Divisão ( com resultado decimal ou não)
    // = DivisãO Inteira (resultado arredondado para um valor inteiro)
    ** = Exponenciação
    % = Resto de (Resto da divisão entre um número e outro)
    () = São usados para alterar a precedências das operações

'''

print('Multiplicação * ', 10 * 10)
# print('Multiplicação * ', '10' + 10)   # Gera um erro. Não é possível concatenar
print('Carlos' + ' ' + 'tem' + str(33) + 'anos.')  # Concatencação longa com conversão de int para string
print('Multiplicação * ', 10 * '10')  # O 10 servirá como operador de repetição
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Divisão / ', 10 / 2)

print(10.5 / 3)  # 3.5 (valor real, sem arredondamento)
print(10.5 // 3)  # 3.0 (Valor arredondado)

print(2 ** 10)  # 1024
print(10 % 3)  # 1


print(5+2*10)  # Padrão
print((5 + 2) * 10)  # Com alteração de precedência
