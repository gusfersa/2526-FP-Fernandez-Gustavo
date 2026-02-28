# Tarea Semana 11 - Matriz 5x5 con ingreso por consola
# Gustavo Fernandez

# Crear una matriz de 5x5 (lista de listas vacía)
matriz = []

# Ingreso de datos por consola con bucles anidados
for fila in range(5):
    fila_actual = []
    for columna in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
        fila_actual.append(valor)
    matriz.append(fila_actual)

# Mostrar la matriz en forma de tabla
print("\nMatriz ingresada:")
for fila in range(5):
    for columna in range(5):
        print(f"{matriz[fila][columna]:6}", end="")
    print()
    