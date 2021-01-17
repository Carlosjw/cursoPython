'''
    TIPOS DE DADOS:
    str - strings(textos)
    int - inteiro
    float - real/ponto futuante (decimais)
    bool - booleano/lógico - True/False
'''


# VERIFICAR O TIPO DE DADO:

# Função type() verifica o tipo de valor inserido no seu parâmetro

print('Luiz', type('Luiz'))  # Luiz <class 'str'>
print(10, type(10))  # 10 <class 'int'>
print(25.23, type(25.23))  # 25.23 <class 'float'>
print(10==10, type(10==10))  # True <class 'bool'>
print('l'=='l', type('l'=='l'))  # True <class 'bool'>
print('L'=='l', type('L'=='l'))  # False <class 'bool'>

# CONVERTENDO TIPOS DE DADOS EM OUTROS:

print('Luiz', type('Luiz'), bool('Luiz'))  # Luiz <class 'str'> True
print('10', type('10'), type(int('10')))  # 10 <class 'str'> <class 'int'>



