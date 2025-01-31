def calcular_alumnos():
    alumnos = {'Juan': 7, 'Ana': 9, 'Pedro': 6}
    promedio = 0
    nota_mayor = 0
    mayor = ''
    for alumno, nota in alumnos.items():
        promedio += nota
        if nota > nota_mayor:
            nota_mayor = nota
            mayor = alumno
    promedio = promedio / len(alumnos)
    return 'Promedio: ' + str(round(promedio, 2)) + ', Mejor estudiante: ' + mayor + ' con '+ str(nota_mayor)
resultado = calcular_alumnos()
print(resultado)