def eliminar_duplicados(palabras_lista):
    lista_sin_duplicados = set(palabras_lista)
    print(lista_sin_duplicados)
palabras= []
while True:
    palabras.append(input('Introduzca palabras para eliminar los duplicados (escriba exit para terminar de escribir): '))
    if palabras[-1] == 'exit':
        palabras.remove('exit')
        break
eliminar_duplicados(palabras)