import copy

def eliminar_pares():
    numeros = [1,2 ,2 ,2 ,2 ,2 ,2 , 2, 3, 4, 5, 6]
    copia_numeros = copy.deepcopy(numeros)
    for i in copia_numeros:
        if i % 2 == 0:
            numeros.remove(i)
    return numeros
resultado = eliminar_pares()
print(resultado)