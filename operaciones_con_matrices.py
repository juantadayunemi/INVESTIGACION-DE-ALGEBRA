"""
* ALGORITMO PARA GENERAR SUAMA DE MATRICES
"""

def suma_matrices(matriz_a, matriz_b):
  # Verificar que las matrices tengan las mismas dimensiones
  if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
    return("Las matrices deben tener las mismas dimensiones")

  # Inicializar la matriz resultante
  matriz_resultado = [[0 for _ in range(len(matriz_a[0]))] for _ in range(len(matriz_a))]

  # Sumar los elementos de las matrices A y B en la matriz resultante
  for i in range(len(matriz_a)):
    for j in range(len(matriz_a[0])):
      matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

  # Retornar la matriz resultante
  return matriz_resultado

# Carga de datos
matriz_a = [[2,-1,-2], [4,3,-1]]
matriz_b = [[2,3,4], [-2,5,-3]]

matriz_resultado = suma_matrices(matriz_a, matriz_b)
print(matriz_resultado)





def resta_matrices(matriz_a, matriz_b):

  # Verificar que las matrices tengan las mismas dimensiones
  if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
    return ("Las matrices deben tener las mismas dimensiones")

  # Inicializar la matriz resultante
  matriz_resultado = [[0 for _ in range(len(matriz_a[0]))] for _ in range(len(matriz_a))]

  # Restar los elementos de las matrices A y B en la matriz resultante
  for i in range(len(matriz_a)):
    for j in range(len(matriz_a[0])):
      matriz_resultado[i][j] = matriz_a[i][j] - matriz_b[i][j]

  # Retornar la matriz resultante
  return matriz_resultado

# Carga de datos
matriz_a = [[3,5,-1], [2,-1,-2]]
matriz_b = [[2,-1,-2], [2,-1,4]]

# matriz_resultado = resta_matrices(matriz_a, matriz_b)
# print(matriz_resultado)



"""
Algoritmo para multiplicar dos matrices
"""
def multiplicacion_matrices(matriz_a, matriz_b):
 
  # Verificar que el número de columnas de A sea igual al número de filas de B
  if len(matriz_a[0]) != len(matriz_b):
    return ("El número de columnas de A debe ser igual al número de filas de B")

  # Inicializar la matriz resultante
  matriz_resultado = [[0 for _ in range(len(matriz_b[0]))] for _ in range(len(matriz_a))]

  # Multiplicar los elementos de las matrices A y B en la matriz resultante
  for i in range(len(matriz_a)):
    for j in range(len(matriz_b[0])):
      for k in range(len(matriz_b)):
        matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

  # Retornar la matriz resultante
  return matriz_resultado

# Carga de datos
matriz_a = [[2, -1], [3,-2]]
matriz_b = [[5],[3]]

# matriz_resultado = multiplicacion_matrices(matriz_a, matriz_b)
# print(matriz_resultado)


"""
* Algoritmo para multiplicar un escalr con una matriz
"""

def multiplicacion_escalar_matriz(escalar, matriz):


  # Verificar que la matriz tenga al menos una dimensión
  if not matriz:
    return ("La matriz no puede estar vacía")

  # Crear una matriz vacía con las mismas dimensiones que la matriz original
  matriz_resultado = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

  # Multiplicar cada elemento de la matriz por el escalar
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      matriz_resultado[i][j] = escalar * matriz[i][j]

  # Retornar la matriz resultante
  return matriz_resultado

# Carga de datos
escalar = 2
matriz = [[-1,-2,3], [2,-3,-4]]

# matriz_resultado = multiplicacion_escalar_matriz(escalar, matriz)
# print(matriz_resultado)


def generar_matriz_identidad(n):

  if n <= 0:
    raise ValueError("La dimensión de la matriz debe ser un entero positivo")

  # Crear una matriz vacía con las dimensiones especificadas
  matriz_identidad = [[0 for _ in range(n)] for _ in range(n)]

  # Establecer los elementos de la diagonal principal en 1
  for i in range(n):
    matriz_identidad[i][i] = 1

  return matriz_identidad


def potencia_matriz(A, k):

  # Validar la dimensión de la matriz
  if len(A) != len(A[0]):
    return ("La matriz debe ser cuadrada")

  n = len(A)  # Dimensión de la matriz

  # Si k es negativo, elevar a la potencia inversa absoluta
  if k < 0:
    k = abs(k)

  # Si k es 0, devolver la matriz identidad
  if k == 0:
    return generar_matriz_identidad(n)

  # Crear la matriz resultado solo una vez
  matriz_resultado = [[0 for _ in range(n)] for _ in range(n)]

  matriz_resultado = A

  # Elevar a la potencia utilizando multiplicación recursiva
  for _ in range(1, k):
    matriz_resultado = multiplicacion_matrices(matriz_resultado, A)

  return matriz_resultado

# Carga de datos
A = [[2,1,5],[2,-2,-4]]
k = 2

# matriz_resultado = potencia_matriz(A, k)
# print(matriz_resultado)

