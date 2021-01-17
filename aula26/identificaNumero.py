num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# if num1.isnumeric() and num2.isnumeric():
try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
# else:
except:
    print('Não pude converter os números para calcular.')