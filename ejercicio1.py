# def ordenar_numeros(numeros_lista):
#     numeros_lista.sort()
#     print(numeros_lista)
# numeros= []
# while True:
#     numeros.append(int(input('Introduzca números para ser ordenados (escriba 0 para terminar de escribir): ')))
#     if numeros[-1] == 0:
#         numeros.remove('exit')
#         break
# ordenar_numeros(numeros)

def ordenar_numeros(numeros_lista):
    numeros_lista.sort()
    print(numeros_lista)
numeros= [5, 2, 9, 1, 6]
ordenar_numeros(numeros)