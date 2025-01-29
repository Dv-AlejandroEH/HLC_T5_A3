def contar_frecuencia():
    entrada = 'hola mundo hola'
    palabras = entrada.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
mostrar = contar_frecuencia()
print(mostrar)