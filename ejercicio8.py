def calcular_vocales_y_consonantes(frase):
    vocales_lista = ['a', 'e', 'i', 'o', 'u']
    cuenta = {'vocales': 0, 'consonantes': 0}
    for i in frase:
        if i in vocales_lista:
            cuenta['vocales'] += 1
        elif i == ' ':
            ''
        else:
            cuenta['consonantes'] += 1
    return cuenta
frase1 = input('Introduzca una frase para contar sus vocales y consonantes: ')
resultado = calcular_vocales_y_consonantes(frase1)
print(resultado)