# Programa con matriz de 4x5
# Objetivo: Declarar, recorrer e imprimir una matriz

# Declarar matriz de 4x5 con números enteros
matriz = [
    [10, 20, 30, 40, 50], # 0
    [15, 25, 35, 45, 55], # 1
    [12, 22, 32, 42, 52], # 2
    [11, 21, 31, 41, 51]  # 3
    # 0   1   2   3   4
]
# Array 2D
# Array Tipo Lista
# Son indexables
# 4x5 = 20 elementos

# Recorrer la matriz con ciclos anidados
print("Valores de la matriz:")
print()

for i in range(4): # Bucle for para recorrer las filas
    for j in range(5): # Bucle for para recorrer las columnas
        print(f"matriz[{i}][{j}] = {matriz[i][j]}") # Imprimir el valor de cada elemento con su índice

print()
print("Matriz en formato tabular:")
print()

for i in range(4):
    for j in range(5):
        print(f"{matriz[i][j]:3}", end=" ")
    print()

