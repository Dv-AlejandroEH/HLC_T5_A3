def divisores(n):
    if n >= 1:
        res = n
        divisores_lista = []
        for i in range(1, n+1):
            if n % i == 0:
                divisores_lista.append(int(res / i))
        divisores_lista.sort()
        return divisores_lista
    else:
        return 'Error: El número indicado no tiene divisores'

numero = int(input('Escriba un número para calcular sus divisores: '))
resultado = divisores(numero)
print(resultado)