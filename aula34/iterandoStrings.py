#  Índices
#  0123456789.......................33 (no caso 34 elementos)

frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''  # String vazia
# total_letras = 0

input_do_usuario = input('Qual letra deseja tornar maiúscula? ')

# Iteracao <- Iterar
while contador < tamanho_frase:
    # print(f'{frase[contador]} | {contador}')  # Imprime cada letra ao lado do seu índice
    # nova_string += frase[contador]
    letra = frase[contador]
    if letra == input_do_usuario:  # Verifica se a letra é minúscula e...
        nova_string += input_do_usuario.upper()  # ... substitui TODAS AS OCORRENCIAS pela maiúscula
    else:
        nova_string += letra  # Caso não, apenas mantém a letra

    # if frase[contador] == input_do_usuario:
    #     total_letras += frase[contador]
    contador += 1

print(nova_string)
# print(total_letras)
