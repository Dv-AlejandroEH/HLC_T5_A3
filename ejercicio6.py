def crear_diccionario():
    palabras = ['gato', 'perro', 'elefante']
    contar = {}
    for palabra in palabras:
        contar[palabra] = len(palabra)
    return contar
mostrar = crear_diccionario()
print(mostrar)