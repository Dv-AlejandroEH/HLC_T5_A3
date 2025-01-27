def ordenar_numeros(numeros_lista):
    numeros_lista.sort()
    print(numeros_lista)
numeros= []
while True:
    numeros.append(int(input('Introduzca números para ser ordenados (escriba 0 par terminar de escribir): ')))
    if numeros[-1] == 0:
        break
ordenar_numeros(numeros)