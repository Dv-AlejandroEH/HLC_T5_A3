# def recibir_lista():
#     lista_numeros = []
#     while True:
#         numero = int(input('Introduzca los números (Introduzca "0" para dejar de recibir números): '))
#         if numero == 0:
#             break
#         lista_numeros.append(numero)
#     return lista_numeros
# def calcular_suma(lista_numeros):
#     suma = 0
#     for i in range(len(lista_numeros)):
#         suma += lista_numeros[i]
#     return suma
# def calcular_promedio(lista_numeros, suma):
#     promedio = suma / len(lista_numeros)
#     return int(promedio)
# def imprimir_por_pantalla():
#     lista_numeros = recibir_lista()
#     suma = calcular_suma(lista_numeros)
#     promedio = calcular_promedio(lista_numeros, suma)
#     print('La suma de los números es:', suma, 'y el promedio de los números es:', promedio)
# imprimir_por_pantalla()


def recibir_lista():
    lista_numeros = [10, 20, 30]
    return lista_numeros
def calcular_suma(lista_numeros):
    suma = 0
    for i in range(len(lista_numeros)):
        suma += lista_numeros[i]
    return suma
def calcular_promedio(lista_numeros, suma):
    promedio = suma / len(lista_numeros)
    return int(promedio)
def imprimir_por_pantalla():
    lista_numeros = recibir_lista()
    suma = calcular_suma(lista_numeros)
    promedio = calcular_promedio(lista_numeros, suma)
    print('La suma de los números es:', suma, 'y el promedio de los números es:', promedio)
imprimir_por_pantalla()